# -*- coding: utf-8 -*-
import os

import click
import csv
import logging

from glob import glob
from dotenv import find_dotenv, load_dotenv

if __name__ == '__main__':
    from csv2vw import construct_line
else:
    from .csv2vw import construct_line


@click.command()
@click.option('--input_filemask', '-i', type=click.STRING)
def main(input_filemask):
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    for input_filepath in sorted(glob(input_filemask)):
        name, ext = os.path.splitext(input_filepath)
        output_filepath = f"{name}.vw"
        logger.info(f"Processing {input_filepath}")
        logger.info(f"Writing {output_filepath}")
        convert(input_filepath, output_filepath)

    logger.info('finished')


def convert(input_file, output_file):
    with open(input_file, encoding='utf-8') as input_file:
        with open(output_file, mode='w', encoding='utf-8') as output_file:
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
