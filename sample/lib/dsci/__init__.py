from . import env

BIN_PATH = env.var('DSI_PATH')
DATA_PATH = env.var('DSI_DATA_PATH')
LIB_PATH = env.var('DSI_LIB_PATH')

from . import data
from . import util


def main():
    """Entry point for the application script"""
    print("Call your main application code here")
