"""
Install the dependencies with
pip install matplotlib sklearn mlxtend  
"""


import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from mlxtend.plotting import plot_decision_regions

from sklearn.datasets import load_iris
from sklearn.svm import SVC
import numpy as np

def plot_boundaries(classifier, X, y, classmap=None):
    """
    classifier: an untrained classifier
    X: features matrix
    y: labels vector
    classmap: a dict where the key is the class index, the value is the class name. 
              For example {0: "setosa", 1: "versicolor", 2: "virginica"}
    """
    labels = None
    if classmap is not None:
        labels = classmap.values()
    # project X into 2d
    X = PCA(n_components=2).fit_transform(X)
    ax = plot_decision_regions(X, y.astype(np.uint8),
                          clf=classifier.fit(X, y),
                          legend=1
                          )
    handles, labels_ = ax.get_legend_handles_labels()
    ax.legend(handles, 
            labels, 
           framealpha=0.3, scatterpoints=1)
    plt.show()
    
    
if __name__ == '__main__':
    """Plot boundaries of SVM on the Iris dataset"""
    X, y = load_iris(return_X_y=True)
    clf = SVC(kernel='rbf')
    plot_boundaries(clf, X, y)