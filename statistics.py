import pandas as pd
import numpy as np
import scipy.stats as stats

def generate_tval_and_pval(data_series, null_hypothesis, tail_count=1):
    t_val, p_val = stats.ttest_1samp(data_series, null_hypothesis)
    return (t_val, p_val)
