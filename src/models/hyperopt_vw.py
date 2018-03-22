# -*- coding: utf-8 -*-

"""Console script for hyperopt_vw."""
import json
import logging
import sys
import click
import numpy as np
from hyperopt import hp, Trials, fmin, tpe, rand
from hyperopt.mongoexp import MongoTrials

from matplotlib import pyplot as plt
try:
    import seaborn as sns
except ImportError:
    print ("Warning: seaborn is not installed. "
           "Without seaborn, standard matplotlib plots will not look very charming. "
           "It's recommended to install it via pip install seaborn")

from hyperopt_vw import Objective


def ftrl(name, **kwargs):
    # loss_funcs = ['squared', 'hinge', 'logistic', 'quantile', 'poisson']
    loss_funcs = ['squared', 'hinge', 'logistic', 'quantile']
    space = {
        # '--ftrl_alpha': hp.loguniform(_name_func('ftrl_alpha'), log(5e-5), log(8e-1)),
        # '--ftrl_beta': hp.uniform(_name_func('ftrl_beta'), log(0.01), log(1.)),
        '--passes': hp.quniform(name + 'passes', 1, 10, 1),
        '--classweight 1:': hp.loguniform(name + '_classweight_pos', log(1), log(1000)),
        '--classweight -1:': hp.loguniform(name + '_classweight_neg', log(0.001), log(1)),
        '--loss_function': hp.choice(name + 'loss_function', loss_funcs),
    }
    return space


def get_space():
    return ftrl("ftrl")


@click.command()
@click.option('--train_data', type=click.Path())
@click.option('--test_data', type=click.Path())
@click.option('--trials_output', type=click.Path(), default='./trials.json')
@click.option('--vw_args', type=click.STRING, default='')
@click.option('--searcher', type=click.Choice(['tpe', 'rand']), default='tpe')
@click.option('--max_evals', type=click.INT, default=100)
@click.option('--outer_loss_function',
              type=click.Choice(['logistic', 'roc-auc', 'pr-auc', 'hinge', 'squared']),
              default='logistic')
@click.option('--mongo', type=click.STRING, default=None)
@click.option('--timeout', type=click.INT, default=3600)
def main(train_data, test_data, trials_output, vw_args, searcher, max_evals, outer_loss_function, mongo, timeout, plot):
    logger = logging.getLogger()
    algo = tpe.suggest
    if searcher == 'rand':
        algo = rand.suggest

    space = get_space()
    if mongo is None:
        trials = Trials()
    else:
        trials = MongoTrials(mongo)

    objective = Objective(train_data, test_data, test_data + '.pred', train_data + '.model', vw_args, outer_loss_function, timeout)
    best = fmin(
        objective,
        space=space,
        algo=algo,
        max_evals=max_evals,
        trials=trials)

    logger.debug("the best hyperopt parameters: %s" % str(best))

    json.dump(trials.results, open(trials_output, 'w'))
    logger.info('All the trials results are saved at %s' % trials_output)

    best_configuration = trials.results[np.argmin(trials.losses())]['train_command']
    best_loss = trials.results[np.argmin(trials.losses())]['loss']
    logger.info("\n\nA full training command with the best hyperparameters: \n%s\n\n" % best_configuration)
    logger.info("\n\nThe best holdout loss value: \n%s\n\n" % best_loss)

    return 0


if __name__ == "__main__":
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    sys.exit(main())  # pragma: no cover
