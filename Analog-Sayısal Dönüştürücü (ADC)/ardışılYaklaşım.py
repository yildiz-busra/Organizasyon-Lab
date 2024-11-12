# ardışıl yaklaşım yöntemi
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

#####################################
# PARAMETRELER
Vmin    = -2.55
Vmax    = 2.55
Va      = 1.29        # giriş
n       = 9           # çözünürlük
#####################################

Vo = -1.        # başlangıçta çıkış (-)
rn = 4
i = n-1
                          
q = round((Vmax-Vmin)/(2**n - 1),rn)          # quantum

gr = 1      # grafik çizilecek mi?
grRampVd = np.zeros(n)
grRampVa = np.zeros(n)

print("Vmin",Vmin,sep="\t")
print("Vmax",Vmax,sep="\t")
print("n",n,sep="\t")
print("q",q,sep="\t")
print("\n")
print("Adım","Va","SB","\tHEX","Vd","Vo",sep='\t')
print("---------------------------------------------------------")

base = 0
while i>=0:
    bias = 2**i
    Vd = round((base + bias) * q + Vmin,rn)
    Vo = round(Vd - Va,rn)

    grRampVa[n-i-1] = Va
    grRampVd[n-i-1] = Vd

    print(n-i,Va,mybin(base+bias,n),hex(base+bias),Vd,Vo,sep='\t')
    i = i - 1
    if Vo <= 0:
        base = base + bias

# son değerler
grRampVa[n-i-2] = Va
grRampVd[n-i-2] = Vd

err = round(Va - Vd,rn+2)
print("Hata Miktarı:",err)

if gr == 1:
    axes = plt.gca()
    axes.set_ylim([Vmin,Vmax])
    plt.plot(grRampVd,'ro',grRampVa,'b--')