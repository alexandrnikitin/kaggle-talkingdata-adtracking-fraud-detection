# -*- coding: utf-8 -*-
import os
import click
import logging
import pandas as pd
from dotenv import find_dotenv, load_dotenv


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath_prefix', type=click.Path())
def main(input_filepath, output_filepath_prefix):
    logger = logging.getLogger(__name__)

    df = pd.read_csv(input_filepath)
    df['click_time'] = pd.to_datetime(df['click_time'])

    for (date, hour), df in df.groupby([df.click_time.dt.date, df.click_time.dt.hour]):
        output_filename = f"{output_filepath_prefix}_{date.strftime('%Y-%m-%d')}_{str(hour).rjust(2,'0')}00.csv"
        logger.info(f'writing {output_filename}')

        with open(output_filename, mode='w', encoding='utf-8') as f:
            df.to_csv(f, index=False)

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



