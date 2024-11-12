# rampa yöntemi
import numpy as np
import matplotlib.pyplot as plt

def mybin(num,n):
    s = ""
    while num > 0:
        m = num % 2
        num = num //2
        s = str(m) + s
        n = n - 1
    while n > 0:
        s = "0" + s
        n = n - 1
    return s

######################################################
# PARAMETRELER
Vmin    = 0
Vmax    = 5.0
Va      = 1.7                           # giriş
n       = 3                             # çözünürlük
######################################################

Vo = -1.        # başlangıçta çıkış (-)
i = 1
rn = 4          # yuvarlatma basamak sayısı
                       
#######################################################
# q = quantum                      
q = round((Vmax-Vmin)/(2**n - 1),rn)          
####################################################### 

gr = 1
grRampVd = np.zeros(2**n)
grRampVa = np.zeros(2**n)

print("Vmin",Vmin,sep="\t")
print("Vmax",Vmax,sep="\t")
print("n",n,sep="\t")
print("q",q,sep="\t")
print("\n")
print("Va","SB","Vd","Vo",sep='\t')
print("-----------------------------")
while Vo < 0:
    Vd = round(i*q + Vmin,rn)
    Vo = round(Vd - Va,rn)
    grRampVa[i-1] = Va
    grRampVd[i-1] = Vd
    print(Va,mybin(i,n),Vd,Vo,sep='\t')
    i = i+1
for i in range(i-1,2**n):
    grRampVa[i] = Va
    grRampVd[i] = Vd

err = round(Va - Vd,rn+2)
print("Hata",err)

if gr == 1:
    axes = plt.gca()
    axes.set_ylim([Vmin,Vmax])
    plt.plot(grRampVd,'ro',grRampVa,'b--')