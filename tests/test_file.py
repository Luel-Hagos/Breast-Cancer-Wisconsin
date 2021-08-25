import numpy as np
import pandas as pd
import unittest
import sys

import warnings
warnings.filterwarnings("ignore")


sys.path.append("../scripts/")

from scripts.dataloader import data_loader

df = data_loader('./data/data.csv')


class breastCancer(unittest.TestCase):

    def check_file_attributes(self):
       col_len = len(list(df.columns))
       assert col_len == 33, f"Function should return the value {33}, it is returning the value {col_len}"

    def data_shape(self):
        row_colmn = [df.shape[0], df.shape[1]]
        assert row_colmn == [569, 33] , f"Function should return the value {[569, 33]}, it is returning the value {row_colmn}"



if __name__ == '__main__':
    unittest.main()
