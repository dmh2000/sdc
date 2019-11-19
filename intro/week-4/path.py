import numpy as np
import matplotlib.pyplot as plt


class Fig8:
    def __init__(self):
        pass

    def path(self, t, dt, L, r):
        alen = int(t / dt)
        d = np.arctan(L / r)

        delta = np.zeros(alen)
        y_offset = np.zeros(alen)
        x_offset = np.zeros(alen)

        # all circle offset by +r
        y_offset.fill(r)

        # first section
        delta[0:375] = +d
        # right circle
        delta[375:1875] = -d
        x_offset[375:1875] = r * 2.0
        # second circle
        delta[1875:3000] = +d

        return delta, x_offset, y_offset


if __name__ == "__main__":
    f = Fig8()
    delta, x_offset, y_offset = f.path(30.0, 0.01, 2.0, 8.0)
    plt.ylim(-1.0, 1.0)
    plt.grid()
    plt.plot(delta, 'r')
    plt.show()
