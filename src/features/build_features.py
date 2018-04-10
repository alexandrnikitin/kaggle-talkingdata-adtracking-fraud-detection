# -*- coding: utf-8 -*-
import gc
import os
import logging

import pandas as pd
import featuretools as ft

from glob import glob

from dask import bag
from dask.diagnostics import ProgressBar
from dotenv import find_dotenv, load_dotenv
from featuretools.primitives import *

dtypes = {
    'ip': 'uint32',
    'app': 'uint16',
    'device': 'uint16',
    'os': 'uint16',
    'channel': 'uint16',
    'is_attributed': 'uint8'
}
to_read = ['ip', 'app', 'device', 'os', 'channel', 'click_time', 'is_attributed']
to_parse = ['click_time']


def create_entityset(filename, target_entity):
    df = pd.read_csv(filename, usecols=to_read, dtype=dtypes, parse_dates=to_parse)
    df['id'] = df.index

    es = ft.EntitySet(id='clicks')
    es = es.entity_from_dataframe(
        entity_id='clicks',
        dataframe=df,
        index='id',
        time_index='click_time',

        variable_types={
            'app': ft.variable_types.Categorical,
            'device': ft.variable_types.Categorical,
            'os': ft.variable_types.Categorical,
            'channel': ft.variable_types.Categorical,
            'is_attributed': ft.variable_types.Boolean,
        }
    )
    es = es.normalize_entity(base_entity_id='clicks', new_entity_id=target_entity, index=target_entity, make_time_index=False)
    es.add_last_time_indexes()
    return es


def calc_feature_matrix(es, entity_id, cutoff_time, training_window):
    feature_matrix, _ = ft.dfs(
        entityset=es,
        target_entity=entity_id,
        cutoff_time=cutoff_time,
        training_window=training_window,
        max_depth=3
    )

    return feature_matrix


def create_features(filename, entity_sets, target_entity, cutoff_time, training_window):
    tw_suffix = training_window.get_name().replace(' ', '').lower()

    b = bag.from_sequence(entity_sets)
    feature_matrices = b.map(
        calc_feature_matrix,
        entity_id=target_entity,
        cutoff_time=cutoff_time,
        training_window=training_window)
    out = feature_matrices.compute()
    feature_matrix = pd.concat(out)
    feature_matrix.columns = [str(col) + f"_{target_entity}_{tw_suffix}" for col in feature_matrix.columns]

    name, ext = os.path.splitext(os.path.basename(filename))
    output_file = os.path.dirname(filename) + '/features/' + f"{name}_{target_entity}_{tw_suffix}_features{ext}"
    feature_matrix.to_csv(output_file)

    del feature_matrix, feature_matrices, b
    gc.collect()


def main():
    logger = logging.getLogger(__name__)
    logger.info('creating a bunch of features')

    pbar = ProgressBar()
    pbar.register()

    target_entities = ['ip', 'app', 'device', 'os', 'channel']
    filenames_train = sorted(glob('../data/interim/train_2017-11-*00.csv'))
    training_windows = ['1 hours', '3 hours', '1 day']

    for target_entity in target_entities:
        filenames = glob(f"../data/interim/partitioned/{target_entity}/train_*.csv")
        b = bag.from_sequence(filenames)
        entity_sets = b.map(create_entityset, target_entity).compute()
        gc.collect()

        for filename in filenames_train:
            logger.info(f"Processing: {filename}")
            df = pd.read_csv(filename, usecols=['click_time'], parse_dates=to_parse)
            cutoff_time = df['click_time'].min()
            del df
            for training_window in training_windows:
                create_features(filename, entity_sets, target_entity=target_entity, cutoff_time=cutoff_time, training_window=ft.Timedelta(training_window))

        del entity_sets, b
        gc.collect()

    logger.info('finished')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
