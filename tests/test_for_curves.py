from test import algorithm_test
from data_generation import linear_curve, parabolic_curve, exponencial_curve, logarithmic_curve


if __name__ == '__main__':
    points1 = linear_curve(-50, 50, 1)
    points2 = parabolic_curve(-50, 50, 1)
    points3 = exponencial_curve(-50, 50, 1)
    points4 = logarithmic_curve(0.01, 100.01, 1)

    tests = [[1, 2, 3, 4, 5, 6],
             [1, 2, 3, 4, 5, 6],
             [1, 2, 3, 4, 5, 6],
             [1, 2, 3, 4, 5, 6]]

    inputs = [points1, points2, points3, points4]

    algorithm_test(tests, inputs, 'curves_tests')
