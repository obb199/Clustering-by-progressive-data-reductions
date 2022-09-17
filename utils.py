def argmin(vec):
    min_value = vec[0]
    min_value_index = 0

    for idx, element in enumerate(vec):
        if element < min_value:
            min_value = element
            min_value_index = idx

    return min_value_index


def argmin_matrix(matrix):
    min_lin_and_col = [0, 0]
    min_element = matrix[0][0]

    for i, line in enumerate(matrix):
        for j, element in enumerate(line):
            if element < min_element and element != -1:
                min_lin_and_col = [i, j]
                min_element = element

    return min_lin_and_col


def separate_axis(points):
    x, y = [], []

    for p in points:
        x.append(p[0])
        y.append(p[1])

    return x, y
