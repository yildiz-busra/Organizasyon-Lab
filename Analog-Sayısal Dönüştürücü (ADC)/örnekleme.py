# ÖRNEKLEME
import numpy as np
import matplotlib.pyplot as plt

sf      = 100                    # kaç örnek alınacak

pi_n    = 1                     # grafikteki pi sayısı
A       = 1                     # grafiğin dikey öteleme miktarı
Gmin    = 0                     # grafiğin min değeri    
Glen    = 3.75                  # grafiğin dikey büyüklüğü
Gmax    = Gmin + Glen
scale   = Glen/2.               # ölçekleme parametresi

x   = np.linspace(0,pi_n*2*np.pi,1000)      # 0 ile 2*pi arasında 1000 nokta, örnek alınacak fonk.
y   = scale * (np.sin(x) + A) + Gmin
x2  = np.linspace(0,pi_n*2*np.pi,sf)
y2  = scale * (np.sin(x2) + A) + Gmin
plt.plot(x,y,"b-",x2,y2,"ro")
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.show()