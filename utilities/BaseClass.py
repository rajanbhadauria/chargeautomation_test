import logging

import pytest


@pytest.mark.usefixtures('setup')
class BaseClass:
    def myLogger(self):
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('logger.log')
        # formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        formatter = logging.Formatter("%(asctime)s [%(levelname)8s] %(message)s (%(filename)s:%(lineno)s)")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger
