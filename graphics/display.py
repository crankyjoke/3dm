import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_3d_minefield(displaygrid, size_of_map):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')


    x_coords_mine = []
    y_coords_mine = []
    z_coords_mine = []

    x_coords_revealed = []
    y_coords_revealed = []
    z_coords_revealed = []

    x_coords_flagged = []
    y_coords_flagged = []
    z_coords_flagged = []

    x_coords_unrevealed = []
    y_coords_unrevealed = []
    z_coords_unrevealed = []

    for z in range(size_of_map):
        for y in range(size_of_map):
            for x in range(size_of_map):
                if displaygrid[z][y][x] == "*":
                    x_coords_unrevealed.append(x)
                    y_coords_unrevealed.append(y)
                    z_coords_unrevealed.append(z)
                elif displaygrid[z][y][x] == "?":
                    x_coords_flagged.append(x)
                    y_coords_flagged.append(y)
                    z_coords_flagged.append(z)
                elif displaygrid[z][y][x] == "^":
                    x_coords_mine.append(x)
                    y_coords_mine.append(y)
                    z_coords_mine.append(z)
                else:
                    x_coords_revealed.append(x)
                    y_coords_revealed.append(y)
                    z_coords_revealed.append(z)


    ax.scatter(x_coords_unrevealed, y_coords_unrevealed, z_coords_unrevealed, c='gray', marker='s', s=150, label='Unrevealed')
    ax.scatter(x_coords_revealed, y_coords_revealed, z_coords_revealed, c='cyan', marker='o', s=100, label='Revealed')
    ax.scatter(x_coords_mine, y_coords_mine, z_coords_mine, c='red', marker='^', s=150, label='Flagged Mine')
    ax.scatter(x_coords_flagged, y_coords_flagged, z_coords_flagged, c='yellow', marker='x', s=150, label='Marked')

    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.set_zlabel('Z Coordinate')

    ax.set_title("3D Minefield Visualization")
    ax.legend()

    ax.set_xlim(0, size_of_map - 1)
    ax.set_ylim(0, size_of_map - 1)
    ax.set_zlim(0, size_of_map - 1)

    plt.show()
# if __name__ == "__main__":
#     size_of_map = 2
#     displaygrid = [
#         [['*', '*'], ['*', '*']],
#         [['*', '*'], ['*', '*']]
#     ]
#     plot_3d_minefield(displaygrid, size_of_map)
