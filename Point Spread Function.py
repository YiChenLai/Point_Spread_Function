import numpy as np
import matplotlib.pyplot as plt
import time


class Point_Spread_Func():
    def __init__(self, wavelength, x, y, amp, phase, propagation_distance, grid_size):
        self.wavelength = wavelength
        self.x = x
        self.y = y
        self.amp = amp
        self.phase = phase
        self.propagation_distance = propagation_distance
        self.grid_size = grid_size

        if np.size(self.amp, 0) == 1 & np.size(self.amp, 1) > 1:
            self.amp = self.amp.T
            self.phase = self.phase.T

        self.x_size = np.size(self.amp, 0)
        self.x = x
        self.y_size = np.size(self.amp, 1)
        self.y = y
        self.z_size = int(np.around(propagation_distance/grid_size)+1)
        self.z = np.linspace(0, propagation_distance, self.z_size)

    def Huygens_Fresnel_principle(self):
        start = time.time()
        field = np.zeros((self.x_size, self.z_size), dtype=complex)
        # 1D Source
        if self.y_size == 1:
            for zi in range(int(self.z_size)):
                for xi in range(self.x_size):
                    distance = np.sqrt((self.x[xi]-self.x)**2+self.z[zi]**2)
                    field[xi, zi] = np.sum(
                        np.exp(1j*self.phase)*np.exp(1j*2*np.pi*distance/self.wavelength))
            self.power_field = abs(field)**2
        # 2D Source
        if self.y_size > 1:
            x_mesh, y_mesh = np.meshgrid(self.x, self.y)
            for zi in range(int(self.z_size)):
                for xi in range(self.x_size):
                    distance = np.sqrt(
                        (self.x[xi]-x_mesh)**2+y_mesh**2+self.z[zi]**2)
                    field[xi, zi] = np.sum(
                        np.exp(1j*self.phase)*np.exp(1j*2*np.pi*distance/self.wavelength))
            self.power_field = abs(field)**2
        end = time.time()
        print(end-start, 'Seconds')


def phase_mask(x, y, f, wavelength):
    if np.size(y) > 1:
        x_mesh, y_mesh = np.meshgrid(x, y)
        amp = np.ones((np.size(x), np.size(y)))
        phase = (-2*np.pi/wavelength)*(np.sqrt((x_mesh**2+y_mesh**2+f**2))-f)
        phase_wrap = np.mod(phase+np.pi, 2*np.pi)
        fig, ax = plt.subplots()
        im = ax.pcolormesh(x, y, phase_wrap, cmap='jet')
        fig.colorbar(im, ax=ax)
    else:
        amp = np.ones((np.size(x, 0), 1))
        phase = (-2*np.pi/wavelength)*(np.sqrt((x**2+f**2))-f)
        fig, ax = plt.subplots()
        ax.plot(x, phase)

    return amp, phase


# Phase Mask
x, y = np.linspace(-10, 10, 101), 1  # np.linspace(-10, 10, 101)
data = phase_mask(x, y, 100, 0.5)

# Field Calculate
run = Point_Spread_Func(0.5, x, y, data[0], data[1], 150, 1)
run.Huygens_Fresnel_principle()
maxi_x, maxi_z = np.where(run.power_field == np.max(run.power_field))

fig, ax = plt.subplots()
im = ax.plot([int(run.z[maxi_z]), int(run.z[maxi_z])],
             [np.min(x), np.max(x)], color='white')
im = ax.pcolormesh(run.z, x, run.power_field, cmap='gnuplot2')
fig.colorbar(im, ax=ax)

# just for test
