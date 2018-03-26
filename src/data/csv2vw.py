# -*- coding: utf-8 -*-


def construct_line(row):
    label = 2 * int(row['is_attributed']) - 1
    str_vw = f"{label}"
    str_vw += f" |i {row['ip']}"
    str_vw += f" |a {row['app']}"
    str_vw += f" |d {row['device']}"
    str_vw += f" |o {row['os']}"
    str_vw += f" |c {row['channel']}"
    str_vw += '\n'
    return str_vw
