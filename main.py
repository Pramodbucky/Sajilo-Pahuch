#!/usr/bin/env python3

from fire import Fire as fire
from easyAccess import webApp


def main(host='0.0.0.0', port=2580, debug=True):
    webApp.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
    fire(main)
