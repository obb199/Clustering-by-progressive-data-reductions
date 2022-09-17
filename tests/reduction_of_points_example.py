import matplotlib.pyplot as plt
from cluster import points_reduction
from data_generation import circular_distribution_generator
from utils import separate_axis

if __name__ == '__main__':
    circles = circular_distribution_generator(radius=1,
                                              concentration_rate=5,
                                              n_points=300,
                                              center_position_x=-5,
                                              center_position_y=-5)

    circles += circular_distribution_generator(radius=1,
                                               concentration_rate=5,
                                               n_points=300,
                                               center_position_x=5,
                                               center_position_y=5)

    circles += circular_distribution_generator(radius=1,
                                               concentration_rate=5,
                                               n_points=300,
                                               center_position_x=-5,
                                               center_position_y=5)

    x, y = separate_axis(circles)

    i = 0
    while len(circles) > 3:
        i += 1
        circles = points_reduction(circles)
        x, y = separate_axis(circles)

        plt.subplot(6, 4, i)
        plt.title(f"Iteration: {i} with {len(x)} points")
        plt.scatter(x, y)

        if i == 24:
            break

    plt.savefig("points_reduction_example")
    plt.show()
