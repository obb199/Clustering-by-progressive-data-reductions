from utils import *


def distance_of_two_points(p1, p2):
    distance = 0

    for dim in range(len(p1)):
        distance += (p1[dim] - p2[dim])**2

    return distance**0.5


def points_reduction(points):
    index_nearest_point = [-1 for _ in range(len(points))]
    distance_nearest_point = [-1 for _ in range(len(points))]

    for idx_point in range(len(points)):
        for idx_test in range(len(points)):
            if idx_test == idx_point:
                continue

            d = distance_of_two_points(points[idx_point], points[idx_test])
            if index_nearest_point[idx_point] == -1:
                index_nearest_point[idx_point] = idx_test
                distance_nearest_point[idx_point] = d
            else:
                if distance_nearest_point[idx_point] > d:
                    index_nearest_point[idx_point] = idx_test
                    distance_nearest_point[idx_point] = d

    new_points = []
    used_points = []
    for idx_point in range(len(points)):
        for idx_test in range(len(points)):
            if index_nearest_point[idx_point] == idx_test and index_nearest_point[idx_test] == idx_point:
                new_point = []
                for dim in range(len(points[idx_point])):
                    new_point.append((points[idx_point][dim] + points[idx_test][dim])/2)

                used_points.append(index_nearest_point[idx_point])

                if new_point not in new_points:
                    new_points.append(new_point)

    for i in range(len(points)):
        if i not in used_points:
            new_points.append(points[i])

    return new_points


def cluster_generator(initial_points, n_clusters):
    p = initial_points
    while len(p) > n_clusters:
        new_points = points_reduction(p)
        if len(new_points) >= n_clusters:
            p = new_points
        else:
            while len(p) != n_clusters:
                distance_matrix = [[-1 for _ in p] for _ in p]
                for idx_point in range(len(p)):
                    for idx_test in range(len(p)):
                        if idx_point != idx_test:
                            distance_matrix[idx_point][idx_test] = distance_of_two_points(p[idx_point], p[idx_test])

                idx_p1, idx_p2 = argmin_matrix(distance_matrix)
                new_point = [(p[idx_p1][0] + p[idx_p1][0])/2, (p[idx_p1][1] + p[idx_p1][1])/2]
                p.pop(idx_p1)
                p.pop(idx_p2)
                p.append(new_point)

    return p


def distance_from_centroids(point, centroids):
    d = []
    for centroid in centroids:
        d.append(distance_of_two_points(point, centroid))

    return d
