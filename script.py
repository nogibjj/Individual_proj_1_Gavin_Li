# -*- coding: utf-8 -*-

"""
Same as notebook
"""

from lib import get_desc_stats, get_hist
import pandas as pd


def main():
    df = pd.read_csv("./resources/train.csv")
    # get_desc_stats(df, "Survived")
    di = get_desc_stats(df, "Survived")
    assert round(di["mean"], 4) == 0.3838
    assert round(di["median"], 4) == 0.0
    assert round(di["std"], 4) == 0.4866
    print("All descriptive statistics checked")
    get_hist(df, "Survived")
    return 0


if __name__ == "__main__":
    main()
