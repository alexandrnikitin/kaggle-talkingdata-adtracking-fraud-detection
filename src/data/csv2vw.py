# -*- coding: utf-8 -*-


def construct_line(row):
    ignore = []
    categorical = ['ip', 'app', 'device', 'os', 'channel']
    numerical = []

    label = 2 * int(row['is_attributed']) - 1

    str_vw = f"{label}"
    for k, v in row.items():
        print(k)
        if k in ignore:
            continue

        if k in categorical:
            str_vw += f" |{k} {v}"
        elif k in numerical:
            str_vw += f" |{k} {k}:{v}"
        else:
            categorical_prefixes = ['MODE','DAY','YEAR','MONTH','WEEKDAY']
            numerical_prefixes = ['SUM','STD','MAX','SKEW','MIN','MEAN','COUNT','NUM_UNIQUE']
            if k.startswith(tuple(categorical_prefixes)):
                str_vw += f" |{k} {v}"
            elif k.startswith(tuple(numerical_prefixes)):
                str_vw += f" |{k} {k}:{v}"
            else:
                str_vw += f" |{k} {v}"

    str_vw += '\n'
    return str_vw
