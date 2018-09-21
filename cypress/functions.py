import os

def cypress_path():
    return  os.path.dirname(os.path.realpath(__file__))
    #http://masnun.com/2015/09/29/python-django-running-multiple-commands-in-subprocesses.html
