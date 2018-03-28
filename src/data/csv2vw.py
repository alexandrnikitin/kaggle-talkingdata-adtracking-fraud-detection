# -*- coding: utf-8 -*-


def construct_line(row):
    ignore = ['is_attributed', 'attributed_time', 'click_time']
    categorical = ['ip', 'app', 'device', 'os', 'channel']
    numerical = []
    categorical_prefixes = tuple(['MODE', 'DAY', 'YEAR', 'MONTH', 'WEEKDAY', 'HOUR', 'MINUTE', 'SECOND'])
    numerical_prefixes = tuple(['SUM', 'STD', 'MAX', 'SKEW', 'MIN', 'MEAN', 'COUNT', 'NUM_UNIQUE', 'PERCENT_TRUE'])

    label = 2 * int(row['is_attributed']) - 1

    str_vw = f"{label}"
    for k, v in row.items():
        if k in ignore:
            continue

        if k in categorical:
            str_vw += f" |{clean(k)} {clean(v)}"
        elif k in numerical:
            try:
                f = float(v)
                if f == 0.0:
                    continue
            except ValueError:
                continue
            str_vw += f" |{clean(k)} {clean(k)}:{f}"
        else:
            if k.startswith(categorical_prefixes):
                str_vw += f" |{clean(k)} {clean(v)}"
            elif k.startswith(numerical_prefixes):
                try:
                    f = float(v)
                    if f == 0.0:
                        continue
                except ValueError:
                    continue
                str_vw += f" |{clean(k)} {clean(k)}:{f}"
            else:
                str_vw += f" |{clean(k)} {clean(v)}"

    str_vw += '\n'
    return str_vw


def clean(item):
    return "".join(item.split()).replace("|", "").replace(":", "")
