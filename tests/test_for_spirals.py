from test import algorithm_test
from data_generation import spirals_generator

if __name__ == '__main__':
    # spirals
    points1 = spirals_generator(radius=0.75,
                                radius_change_rate=0.1,
                                rotation_angle_change=5,
                                rotations=2,
                                noise=0.75,
                                angle_init=0)

    points2 = spirals_generator(radius=0.75,
                                radius_change_rate=0.1,
                                rotation_angle_change=5,
                                rotations=2,
                                noise=0.5,
                                angle_init=120)

    points3 = spirals_generator(radius=0.75,
                                radius_change_rate=0.1,
                                rotation_angle_change=5,
                                rotations=2,
                                noise=0.5,
                                angle_init=240)

    tests = [[1, 2, 3, 4, 5, 6],
             [1, 2, 3, 4, 5, 6],
             [1, 2, 3, 4, 5, 6]]

    inputs = [points1, points1+points2, points1+points2+points3]

    algorithm_test(tests, inputs, "spirals_test")
