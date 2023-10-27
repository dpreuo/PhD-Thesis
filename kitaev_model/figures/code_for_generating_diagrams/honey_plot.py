import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cbook, cm
from matplotlib.colors import LightSource

kx = np.linspace(-np.pi, np.pi, 800)
ky = np.linspace(-np.pi, np.pi, 800)

KX, KY = np.meshgrid(kx, ky)

kx_warped = (KX) - (KY)/2
ky_warped = (KY)*np.sqrt(3)/2
kx_warped,ky_warped = KX, KY

J = [1,1.1,1]
k = .1
dx = J[0]*np.sin(KX) + J[1]*np.sin(KY)
dy = J[0]*np.cos(KX) + J[1]*np.cos(KY) +J[2]
dz = k*(np.sin(KX) + np.sin(-KY)+ np.sin(KX-KY))

energy = np.sqrt(dx**2 + dy**2 + dz**2)
energy_before = np.sqrt(dx**2 + dy**2)



# plot both surfaces
fig = plt.figure(figsize = (20,10))
ax = [fig.add_subplot(1,2,1, projection='3d'),fig.add_subplot(1,2,2, projection='3d')]


ax[0].plot_surface(kx_warped,ky_warped,energy_before, cmap = 'seismic')
ax[0].plot_surface(kx_warped,ky_warped,-energy_before, cmap = 'seismic')
ax[0].set_title('Energy before perturbation')
ax[0].set_xlabel('kx')
ax[0].set_ylabel('ky')
# ax[0].set_xlim([-2*np.pi,2*np.pi])
# ax[0].set_ylim([-2*np.pi,2*np.pi])
ax[0].set_zlim([0,2])


ax[1].plot_surface(kx_warped,ky_warped,energy, cmap = 'seismic')
ax[1].plot_surface(kx_warped,ky_warped,-energy, cmap = 'seismic')
ax[1].set_title('Energy after perturbation')
ax[1].set_xlabel('kx')
ax[1].set_ylabel('ky')
# ax[1].set_xlim([-2*np.pi,2*np.pi])
# ax[1].set_ylim([-2*np.pi,2*np.pi])
ax[1].set_zlim([0,2])






# fig = plt.figure(figsize = (10,10))
# ax = plt.axes(projection='3d')
# ls = LightSource(azdeg=0,altdeg=65)
# # shade data, creating an rgb array.
# rgb = ls.shade(dz, cm.copper)
# surf = ax.plot_surface(dx,dy,dz, rstride=1, cstride=1, facecolors=rgb,
#                        linewidth=0, antialiased=False, shade=False, alpha = alph)

plt.show()