import matplotlib.pyplot as plt
from cluster import *
from utils import argmin
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

if __name__ == '__main__':
    dataset = load_iris()
    classes = len(dataset.target_names)
    matrix_confusion = [[0 for _ in range(classes)] for _ in range(classes)]

    X_train, X_test, y_train, y_test = train_test_split(dataset.data,
                                                        dataset.target,
                                                        test_size=0.3,
                                                        shuffle=True,
                                                        random_state=42)

    cluster_points = cluster_generator(X_train, 3)

    for x, y in zip(X_test, y_test):
        distances_from_clusters = distance_from_centroids(x, cluster_points)
        predict = argmin(distance_from_centroids(x, cluster_points))
        matrix_confusion[predict-1][y-1] += 1

    for i, target in enumerate(dataset.target_names):
        plt.subplot(1, 3, i+1)
        plt.title(f"Results when target is {i}")
        for j, res in enumerate(matrix_confusion[i]):
            plt.bar(f"{dataset.target_names[j]}", res)

    print(matrix_confusion)
    plt.savefig("iris_dataset_tests")
    plt.show()
