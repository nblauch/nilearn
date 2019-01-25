"""
This module implements plotting functions useful to report analysis results.

Author: Martin Perez-Guevara, Elvis Dohmatob, 2017
"""
import warnings

try:
    import matplotlib
except ImportError:
    warnings.warn("Nistats' reporting module requires matplotlib to work. "
                  "Install it using:\n"
                  "pip install matplotlib"
                  )
else:
    # matplotlib backend must be set before importing  any of its functions.
    matplotlib.use('Agg')
    import nilearn.plotting  # overrides the backend on headless servers

from ._compare_niimgs import compare_niimgs
from ._get_clusters_table import get_clusters_table
from ._plot_matrices import plot_contrast_matrix, plot_design_matrix

__all__ = [compare_niimgs,
           get_clusters_table,
           plot_contrast_matrix,
           plot_design_matrix,
           ]
