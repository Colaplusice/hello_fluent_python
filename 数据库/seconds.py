import numpy as np

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler


# #############################################################################
# Generate sample data
centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=0.4,
                            random_state=0)

X = StandardScaler().fit_transform(X)

X = StandardScaler().fit_transform(X)

db=DBSCAN(eps=3,min_samples=10).fit(X)

# 将0数组转换为false数组
core_samples_mask=np.zeros_like(db.labels_,dtype=bool)

core_samples_mask[db.core_sample_indices_] = True
