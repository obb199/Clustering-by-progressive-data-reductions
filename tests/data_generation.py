import random
import math


def random_points_generator(n_points, min_x, max_x, min_y, max_y, coordinates=False):
    points = []
    x = []
    y = []
    for k in range(n_points):
        point = [random.randint(min_x, max_x), random.randint(min_y, max_y)]
        if coordinates:
            x.append(point[0])
            y.append(point[1])
        else:
            points.append(point)

    if coordinates:
        return x, y

    return points


def circular_distribution_generator(radius=1, concentration_rate=1, n_points=100, center_position_x=0, center_position_y=0):
    points = []
    angle = 0

    rotation_rate = 360/n_points
    while len(points) < n_points:
        angle += rotation_rate
        rad = math.pi*angle/180
        x = (radius-radius*random.random()*concentration_rate)*math.cos(rad) + center_position_x
        y = (radius-radius*random.random()*concentration_rate)*math.sin(rad) + center_position_y
        points.append([x, y])

    return points


def spirals_generator(radius=1, radius_change_rate=0.1, rotation_angle_change=1, rotations=2, noise=0, angle_init=0):
    points = []

    for angle in range(angle_init, int(rotations*360)+angle_init, rotation_angle_change):
        rad = math.pi*angle/180
        radius = radius + radius_change_rate

        x = radius*math.cos(rad) + random.random()*noise
        y = radius*math.sin(rad) + random.random()*noise

        points.append([x, y])

    return points


def linear_curve(init, end, step):
    points = []
    i = init
    while end > i:
        points.append([i, i*2 + 3])
        i += step

    return points


def parabolic_curve(init, end, step):
    points = []
    i = init
    while end > i:
        points.append([i, i**2])
        i += step

    return points


def exponencial_curve(init, end, step):
    points = []
    i = init
    while end > i:
        points.append([i, 2**i])
        i += step

    return points


def logarithmic_curve(init, end, step):
    points = []
    i = init
    while end > i:
        points.append([i, math.log(i, 2)])
        i += step

    return points
