import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy import random
import scipy
from scipy import stats

from statsmodels.stats import multitest

data_files = {\
"GSM5268644":{'count':"GSM5268644_P1ShamD3_counts.csv",'metadata':"GSM5268644_P1ShamD3.metadata.csv",'scale':50},\
"GSM5268646":{'count':"GSM5268646_P1MID3_counts.csv",'metadata':"GSM5268646_P1MID3.metadata.csv",'scale':10},\
"GSM5268645":{'count':"GSM5268645_P1ShamD7_counts.csv",'metadata':"GSM5268645_P1ShamD7.metadata.csv",'scale':27},\
"GSM4983123":{'count':"GSM4983123_Count_matrix.csv",'metadata':"GSM4983123_metadata.csv",'scale':12}\
}

def main(argv):
    
    data_dir = "GSM5268646"
    count_file = "{0}/{1}".format(data_dir, data_files[data_dir]['count'])
    meta_file = "{0}/{1}".format(data_dir, data_files[data_dir]['metadata'])
    scatter_scale = data_files[data_dir]['scale']

    counts = pd.read_csv(count_file)
    meta = pd.read_csv(meta_file)
    t_counts = counts.T
    t_counts.index.rename('barcode', inplace = True)
    meta = meta.rename(columns = {'Unnamed: 0':'barcode'})
    meta.set_index('barcode', inplace = True)
    combined = pd.concat([t_counts, meta[['imagerow','imagecol']]], axis = 1)
    
    #the following will plot expression of the gene Sox17
    gene_name = 'Sox17'
    plt.figure(figsize=(5,5))
    plt.gca().set_aspect('equal')
    plt.scatter(np.max(combined['imagerow'])-combined['imagerow'], combined['imagecol'], c=combined[gene_name], cmap = 'Reds', s = scatter_scale)
    plt.clim(0, np.max(combined[gene_name]))
    plt.colorbar()
    plt.savefig(f'{gene_name}.pdf', format='pdf', dpi=300)
    plt.close()
    return 0
if __name__ == "__main__":
    sys.exit(main(None))
