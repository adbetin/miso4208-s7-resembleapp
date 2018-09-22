import os


def cypress_path():
    return os.path.dirname(os.path.realpath(__file__))


def screenshots_path():
    return os.path.join(cypress_path(), 'cypress', 'screenshots', 'palette.spec.js')
