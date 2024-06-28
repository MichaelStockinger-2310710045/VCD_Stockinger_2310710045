__doc__ = "ploting method \
           based on \
           https://www.geeksforgeeks.org/matplotlib-figure-figure-add_axes-in-python/"

#based on
#source: https://www.geeksforgeeks.org/matplotlib-figure-figure-add_axes-in-python/

#required imports
import matplotlib.pyplot as plt
import numpy as np
from scipy import constants as const


# constants
a_1Fx, a_2Fx, a_3Fx, a_4Fx = -21.3, 1144, 49.6, 226
a_5Fx, a_6Fx, a_7Fx, a_8Fx = 0.069, -0.006, 0.056, 0.486
a_1Fy, a_2Fy, a_3Fy, a_4Fy = -22.1, 1011, 1078, 1.82
a_5Fy, a_6Fy, a_7Fy, a_8Fy = 0.208, 0, -0.354, 0.707
a_1Mz, a_2Mz, a_3Mz, a_4Mz = -2.72, -2.28, -1.86, -2.73
a_5Mz, a_6Mz, a_7Mz, a_8Mz = 0.11, -0.07, 0.643, -4.04
a_9Fy, a_10Fy, a_11Fy, a_12Fy, a_13Fy = 0.028, 0, 14.8, 0.022, 0
a_9Mz, a_10Mz, a_11Mz, a_12Mz, a_13Mz = 0.015, -0.066, 0.945, 0.03, 0.07

#================================================
def exec_sample_plot_(slip, mass, mu, file_name_out):
  exec_sample_plot_.__doc__ = "call to mathplotlib"

  # kappa (variable)
  #kappa = np.arange(0.00, 1.01, 0.01)
  kappa = np.arange(0, 101, 1)

  # Slip angel - alpha (parameter)
  alpha = slip

  # Fz
  F_z = mass * const.g / 4

  # Camber angle
  gamma = 0

  # Break force - Fx
  E_x = a_6Fx * F_z * F_z + a_7Fx * F_z + a_8Fx
  D_x = a_1Fx * F_z * F_z + a_2Fx * F_z
  C_x = 1.65
  B_x = (a_3Fx * F_z * F_z + a_4Fx * F_z) / (C_x * D_x * np.exp(a_5Fx * F_z))
  Phi_x = (1-E_x) * kappa + (E_x / B_x) * np.arctan(B_x * kappa)
  F_x = D_x * np.sin(C_x * np.arctan(B_x * Phi_x))

  # Side force - Fy
  Delta_Sh_y = a_9Fy * gamma
  Delta_Sv_y = (a_10Fy * F_z * F_z + a_11Fy * F_z) * gamma
  E_y = a_6Fy * F_z * F_z + a_7Fy * F_z + a_8Fy
  D_y = a_1Fy * F_z * F_z + a_2Fy * F_z
  C_y = 1.30
  B_y = (a_3Fy * np.sin(a_4Fy * np.arctan(a_5Fy * F_z))) / (C_y * D_y) * (1 - a_12Fy * np.abs(gamma))
  Phi_y = (1 - E_y)*(alpha + Delta_Sh_y) + (E_y / B_y) * np.arctan(B_y*(alpha + Delta_Sh_y))
  F_y = D_y * np.sin(C_y * np.arctan(B_y * Phi_y)) + Delta_Sv_y

  print("F_x = ", F_x)
  print("\n")
  print("F_y = ", F_y)
  print("\n")
  #define figure
  fig = plt.figure()

  #add plot one
  ax1 = fig.add_subplot(2, 1, 1)
  #define plots
  ax1.plot(kappa, F_x, color ="green", lw = 2)
  #add axis label
  ax1.set_xlabel("kappa")
  ax1.set_ylabel("F_x")

  #add plot two
  #ax2 = fig.add_subplot(2, 1, 2)
  #define plots
  #ax2.plot(kappa, F_y, color ="green", lw = 2)
  #add axis label
  #ax2.set_xlabel("kappa")
  #ax2.set_ylabel("F_y")

  #add plot label
  fig.suptitle("Plot Sample\n\n", fontweight ="bold")

  #export as PDF
  plt.savefig(file_name_out)
  