# -*- coding: utf-8 -*-

"""Console script for hyperopt_vw."""
import logging
import sys
from math import log

import click
from hyperopt import hp, Trials
from hyperopt.mongoexp import MongoTrials
from hyperopt_vw import Objective, search


@click.command()
@click.option('--train_data', type=click.Path())
@click.option('--validation_data', type=click.Path())
@click.option('--test_data', type=click.Path())
@click.option('--trials_output', type=click.Path(), default=None)
@click.option('--vw_args', type=click.STRING, default='')
@click.option('--max_evals', type=click.INT, default=100)
@click.option('--outer_loss_function',
              type=click.Choice(['logistic', 'roc-auc', 'pr-auc', 'hinge', 'squared']),
              default='logistic')
@click.option('--mongo', type=click.STRING, default=None)
@click.option('--timeout', type=click.INT, default=3600)
def main(train_data, validation_data, test_data, trials_output, vw_args, max_evals, outer_loss_function, mongo, timeout):
    space = {
        '--ftrl_alpha': hp.loguniform('ftrl_alpha', log(1e-5), log(1e-1)),
        '--ftrl_beta': hp.uniform('ftrl_beta', 0.01, 1.),
        '--l1': hp.loguniform('l1', log(1e-8), log(1e-1)),
        '--l2': hp.loguniform('l2', log(1e-8), log(1e-1)),
        # '--passes': hp.quniform('passes', 1, 5, 1),
        # '--learning_rate': hp.loguniform('learning_rate', log(0.01), log(10)),
        # '--classweight 1:': hp.loguniform('classweight_pos', log(1), log(1000)),
        # '--classweight -1:': hp.loguniform('classweight_neg', log(0.001), log(1)),
    }

    trials = MongoTrials(mongo) if mongo else Trials()

    objective = Objective(train_data=train_data, validation_data=validation_data, test_data=test_data,
                          vw_args=vw_args, outer_loss_function=outer_loss_function, timeout=timeout)

    search(space, objective, trials=trials, trials_output=trials_output, max_evals=max_evals)

    return 0


def vw(name, **kwargs):
    # optimizations = [
    #     ftrl(name + '.ftrl'),
    # ]
    # loss_funcs = ['squared', 'hinge', 'logistic', 'quantile', 'poisson']
    loss_funcs = ['squared', 'hinge', 'logistic', 'quantile']
    space = {
        '--bit_precision': hp.quniform(name + 'bit_precision', 18, 29, 1),
        '--learning_rate': hp.loguniform(name + 'learning_rate', log(0.01), log(10)),
        '--loss_function': hp.choice(name + 'loss_function', loss_funcs),
        '--hash': hp.choice(name + 'hash', ['strings', 'all']), 'passes': hp.quniform(name + 'passes', 1, 1, 10),
        '--leave_duplicate_interactions': hp.choice(name + 'leave_duplicate_interactions', [True, False]),
        '--classweight 1:': hp.loguniform(name + '_classweight_pos', log(1), log(1000)),
        '--classweight -1:': hp.loguniform(name + '_classweight_neg', log(0.001), log(1)),
        '--sgd': hp.choice(name + 'sgd', [True, False]), 'adaptive': hp.choice(name + 'adaptive', [True, False]),
        '--normalized': hp.choice(name + 'normalized', [True, False]),
        '--invariant': hp.choice(name + 'invariant', [True, False]),
        '--optimizations': hp.choice(name + 'optimizations', optimizations),
        '--l1': hp.loguniform(name + 'l1', log(1e-8), log(1e-1)),
        '--l2': hp.loguniform(name + 'l2', log(1e-8), log(1e-1)),
        '--decay_learning_rate': hp.uniform(name + 'decay_learning_rate', 0.1, 1),
        '--power_t': hp.uniform(name + 'power_t', 0.01, 1)}
    return space


if __name__ == "__main__":
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    sys.exit(main())  # pragma: no cover
