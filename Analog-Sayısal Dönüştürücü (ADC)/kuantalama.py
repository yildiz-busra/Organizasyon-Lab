# kuantalama
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
sf = 10                 # kaç örnek alınacak
pi_n = 1                # grafikteki pi sayısı
A    = 1                # grafiğin dikey öteleme miktarı
rn = 2            # yuvarlama sayısı
#############################################################
# PARAMETRELER
n    = 4                # çözünürlük
Gmin = 0                # grafiğin min değeri    
Glen = 3.75             # grafiğin dikey büyüklüğü
Gmax = Gmin + Glen
#############################################################
scale = Glen/2.      # ölçekleme parametresi
q = round((Gmax-Gmin)/(2**n - 1),rn) 
minor_ticks = np.arange(Gmin, Gmax+1, q)
ax.set_yticks(minor_ticks, minor=True)
ax.grid(which='minor')
x2  = np.linspace(0,pi_n*2*np.pi,sf)
y2  = scale * (np.sin(x2) + A) + Gmin
plt.plot(x2,y2,"r.")
plt.show()