import dsci
import pandas as pd


def path(name):
    return '{:s}/{:s}'.format(dsci.DATA_PATH, name)


def read_csv(name):
    return pd.read_csv(path(name))


def fopen(name, mode='r', buffering=-1):
    return open(path(name), mode, buffering)
