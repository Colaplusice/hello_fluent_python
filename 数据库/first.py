import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

X1, y1 = datasets.make_circles(n_samples=5000, factor=0.6, noise=0.05)
X2, y2 = datasets.make_blobs(
    n_samples=1000,
    n_features=2,
    centers=[[1.2, 1.2]],
    cluster_std=[[0.1]],
    random_state=9,
)

X = np.concatenate((X1, X2))

plt.scatter(X[:, 0], X[:, 1], marker="o")
plt.show()
