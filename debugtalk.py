import time

from httprunner import __version__


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)

def int_to_str(arg):
    return str(arg)

def str_to_int(arg):
    return int(arg)