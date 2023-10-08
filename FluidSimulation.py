import matplotlib as mpt
import numpy as np

def main():
    Nx = 1600
    Ny = 400
    tau = 0.53
    Nt = 3000

    Nl = 9
    cxs = np.array([0, 0, 1, 1, 1, 0, -1, -1, -1])
    cys = np.array([0, 1, 1, 0, -1, -1, -1, 0, 1])
    weights = np.array([4/9, 1/9, 1/36, 1/9, 1/36, 1/9, 1/36, 1/9, 1/36])

    F = np.ones((Nx, Ny, Nl)) + 0.01 * np.random.randn(Nx, Ny, Nl)
    F[:, :, 3] = 2.3

    Cylinder = np.full((Nx, Ny), False)