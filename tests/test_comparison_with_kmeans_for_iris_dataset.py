import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from cluster import Cluster

if __name__ == '__main__':
    dataset = load_iris()
    classes = len(dataset.target_names)

    X_train, X_test, y_train, y_test = train_test_split(dataset.data,
                                                        dataset.target,
                                                        test_size=0.3,
                                                        shuffle=True,
                                                        random_state=42)

    cluster_points = Cluster(3)
    cluster_points.fit(X_train)
    k_means_model = KMeans(n_clusters=3, random_state=0)
    k_means_model.fit(X_train)

    matrix_confusion = [[0 for _ in range(classes)] for _ in range(classes)]
    matrix_confusion_kmeans = [[0 for _ in range(classes)] for _ in range(classes)]

    predict = cluster_points.predict(X_test)
    predict_kmeans = k_means_model.predict(X_test)

    i = -1
    for x, y in zip(X_test, y_test):
        i += 1
        matrix_confusion[predict[i]-1][y-1] += 1
        matrix_confusion_kmeans[predict_kmeans[i]-1][y-1] += 1

    plt.figure(figsize=(8, 8))
    for i, target in enumerate(dataset.target_names):
        plt.subplot(2, 3, i+1)
        plt.title(f"target = {i}")
        for j, res in enumerate(matrix_confusion[i]):
            plt.bar(f"{dataset.target_names[j]}", res)

    for i, target in enumerate(dataset.target_names):
        plt.subplot(2, 3, i+4)
        plt.title(f"target = {i} (kmeans)")
        for j, res in enumerate(matrix_confusion_kmeans[i]):
            plt.bar(f"{dataset.target_names[j]}", res)

    print(matrix_confusion)
    print(matrix_confusion_kmeans)
    plt.savefig("iris_dataset_comparison_with_kmeans_tests")
    plt.show()
