# -*- coding: utf-8 -*-

"""
All functions go here
"""

import pandas as pd
from typing import Dict
import matplotlib.pyplot as plt


def get_desc_stats(df: "pd.DataFrame", column: "str") -> "Dict[str, float]":
    return {
        "mean": df[column].mean(),
        "median": df[column].median(),
        "std": df[column].std(),
    }


def get_hist(df: "pd.DataFrame", column: "str") -> "None":
    plt.hist(df[column])
    plt.title("Histogram for Survived in Titanic")
    plt.xlabel("Survived")
    plt.ylabel("Count")
    plt.show()
    return None


def main():
    pass


if __name__ == "__main__":
    main()
