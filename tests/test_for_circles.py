from test import algorithm_test
from data_generation import circular_distribution_generator

if __name__ == '__main__':
    # gerando pontos
    points = []

    # circles
    points1 = circular_distribution_generator(r=2,
                                              concentration_rate=1.5,
                                              n_points=100,
                                              center_position_x=0,
                                              center_position_y=3)

    points2 = circular_distribution_generator(r=2,
                                              concentration_rate=1,
                                              n_points=100,
                                              center_position_x=5,
                                              center_position_y=8)

    points3 = circular_distribution_generator(r=2,
                                              concentration_rate=0.5,
                                              n_points=100,
                                              center_position_x=3,
                                              center_position_y=0)

    tests = [[1, 2, 3, 4, 5, 6],
             [1, 2, 3, 4, 5, 6],
             [1, 2, 3, 4, 5, 6]]

    inputs = [points1, points1 + points2, points1 + points2 + points3]

    algorithm_test(tests, inputs, "circles_tests")
