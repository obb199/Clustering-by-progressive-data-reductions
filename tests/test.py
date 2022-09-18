from cluster import Cluster
import matplotlib.pyplot as plt


def algorithm_test(clusters_matrix, points, name_output_figure):
    plt.figure(figsize=(15, 20))
    colors = ['blue', 'orange', 'pink', 'green', 'purple', 'black']

    j = 0
    for point_idx, line_of_clusters in enumerate(clusters_matrix):
        for i, number_of_clusters in enumerate(line_of_clusters):
            j += 1
            plt.subplot(len(clusters_matrix), len(clusters_matrix[0]), j)
            plt.title(f'Number of clusters:' + str(number_of_clusters))

            clusters = Cluster(number_of_clusters)
            clusters.fit(points[point_idx])
            predicts = clusters.predict(points[point_idx])
            for idx, p in enumerate(points[point_idx]):
                plt.scatter(p[0], p[1], color=colors[predicts[idx]], alpha=0.6)

            for c in clusters.centroids_positions:
                plt.scatter(c[0], c[1], color='red')

    plt.savefig(name_output_figure)
    plt.show()
