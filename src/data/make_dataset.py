# -*- coding: utf-8 -*-
import os
import click
import logging
import csv
from dotenv import find_dotenv, load_dotenv


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path(exists=False))
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    convert(input_filepath, output_filepath)

    logger.info('finished')


def construct_line(row):
    label = str(2 * int(row['is_attributed']) - 1)
    str_vw = f"{label}"
    importance = '$importance$' if label == 1 else ''
    str_vw += f" {importance} "
    str_vw += f" |i {row['ip']}"
    str_vw += f" |a {row['app']}"
    str_vw += f" |d {row['device']}"
    str_vw += f" |o {row['os']}"
    str_vw += f" |c {row['channel']}"
    str_vw += '\n'
    return str_vw


def convert(input_file, output_file):
    with open(input_file, encoding='utf-8') as input_file:
        with open(output_file, mode='x', encoding='utf-8') as output_file:
            for row in csv.DictReader(input_file):
                output_file.write(construct_line(row))


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
