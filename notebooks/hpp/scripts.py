"""Module for listing down additional custom functions required for the notebooks."""

import pandas as pd
from numpy import inf
def binned_median_income(df):
    """Bin the selling price column using quantiles."""
    return pd.cut(df["median_income"],
                               bins=[0., 1.5, 3.0, 4.5, 6., inf],
                               labels=[1, 2, 3, 4, 5])
