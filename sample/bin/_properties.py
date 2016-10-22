import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))


def _localpath(name):
    return dir_path + '/' + name


def _get_properties_path(path, filename):
    return path + '/' + filename


def _local_properties_path(path = _localpath('..')):
    return _get_properties_path(path, 'local.properties')


def _read_properties(filename = _local_properties_path()):
    d = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            if line == '':
                continue
            tokens = line.split('=')
            d[tokens[0]] = '='.join(tokens[1:])
    return d


def main(argv):
    d = _read_properties()
    if len(argv) > 1:
        print d[argv[1]]

if __name__ == "__main__":
    main(sys.argv)
