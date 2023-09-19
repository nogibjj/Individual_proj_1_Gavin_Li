# -*- coding:utf-8 -*-

"""Test for lib.py"""

from lib import get_desc_stats, get_hist
import pandas as pd

def test_get_desc_stats():
    df = pd.read_csv("./resources/train.csv")
    di = get_desc_stats(df, "Survived")
    assert round(di["mean"], 4) == 0.3838
    assert round(di["median"], 4) == 0.0
    assert round(di["std"], 4) == 0.4866

def test_get_hist():
    df = pd.read_csv("./resources/train.csv")
    get_hist(df, "Survived")
