from cropclass import tsmask
from cropclass import tsclust
from cropclass import ndvicalc
from os import listdir
import re
import matplotlib.pyplot as plt
import numpy as np

pg = {
    'time_seriesdf': [cropdf],
    'n_samples': [10],
    'cluster_alg': ['GAKM', 'TSKM'],
    'n_clusters': list(range(2, 4)),
    'smooth': [True],
    'ts_var': ['ndvi'],
    'window': [7],
    'poly': [3],
    'cluster_metric': ['dtw', 'softdtw'],
    'score': [True]
}

def main(param_grid, df):




if __name__ == "__main__":
    main()