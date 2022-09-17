import matplotlib.pyplot as plt
from cluster import *
from utils import argmin
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans

if __name__ == '__main__':
    dataset = load_iris()
    classes = len(dataset.target_names)

    X_train, X_test, y_train, y_test = train_test_split(dataset.data,
                                                        dataset.target,
                                                        test_size=0.3,
                                                        shuffle=True,
                                                        random_state=42)

    cluster_points = cluster_generator(X_train, 3)
    k_means_model = KMeans(n_clusters=2, random_state=0).fit(X_train)

    matrix_confusion = [[0 for _ in range(classes)] for _ in range(classes)]
    matrix_confusion_kmeans = [[0 for _ in range(classes)] for _ in range(classes)]

    for x, y in zip(X_test, y_test):
        distances_from_clusters = distance_from_centroids(x, cluster_points)
        predict = argmin(distance_from_centroids(x, cluster_points))
        matrix_confusion[predict-1][y-1] += 1

        predict_kmeans = k_means_model.predict([x])
        matrix_confusion_kmeans[predict-1][y-1] += 1

    plt.figure(figsize=(15, 30))
    for i, target in enumerate(dataset.target_names):
        plt.subplot(2, 3, i+1)
        plt.title(f"target = {i}")
        for j, res in enumerate(matrix_confusion[i]):
            plt.bar(f"{dataset.target_names[j]}", res)

    for i, target in enumerate(dataset.target_names):
        plt.subplot(2, 3, i+4)
        plt.title(f"target = {i} with kmeans")
        for j, res in enumerate(matrix_confusion_kmeans[i]):
            plt.bar(f"{dataset.target_names[j]}", res)

    print(matrix_confusion)
    print(matrix_confusion_kmeans)
    plt.savefig("iris_dataset_comparison_with_kmeans_tests")
    plt.show()
