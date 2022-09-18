import matplotlib.pyplot as plt
from cluster import *
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

    cluster_points = Cluster(3)
    cluster_points.fit(X_train)

    predict = cluster_points.predict(X_test)

    i = 0
    for x, y in zip(X_test, y_test):
        matrix_confusion[predict[i]-1][y-1] += 1
        i += 1

    for i, target in enumerate(dataset.target_names):
        plt.subplot(3, 1, i+1)
        plt.title(f"target = {i}")
        for j, res in enumerate(matrix_confusion[i]):
            plt.bar(f"{dataset.target_names[j]}", res)

    print(matrix_confusion)
    plt.savefig("iris_dataset_tests")
    plt.show()
