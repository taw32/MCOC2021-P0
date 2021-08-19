import numpy as np 
from numpy import zeros,float32,half,single,double,longdouble
from time import perf_counter
from scipy import linalg

def matriz_laplaciana(N,dtype = float32):
    A =zeros((N,N),dtype =dtype)
    for i in range(N):
        for j in range(N):
            if i == j:
                A[i,j] = 2
            elif i+1 ==j:
                A[i,j] = -1
            elif i-1 == j:
                A[i,j] = -1
    return A
    
Nval = [2, 5, 10, 15, 20, 30, 35, 40, 45, 50, 55, 60, 75, 100, 110, 125, 160, 200, 230, 250, 350, 500, 600, 800, 1000]#, 2000, 5000, 10000]
#numpy_values =[]
#scipy_values = []
name = ("matmul1.txt") 
archivo=open(name,'w')    
memoria = []
for N in Nval:
    A = matriz_laplaciana(N,np.longdouble) 
    t1 = perf_counter()

    B = linalg.inv(A,overwrite_a=False)

    t2 = perf_counter()
    dt = t2 - t1
    print(f"Para N = {N}, el tiempo transcurrido numpy = {dt} s\n")
    size = 1*(N*N)*16
    memoria.append(size)
    archivo.write(f"{N} {dt}\n")
archivo.close()
tiempos = []
nombre = ("matmul1.txt")
archivo = open(nombre,"r")
resultados = [[(val) for val in linea.split(' ')]for linea in archivo]
for i in range(len(Nval)):
    ti = resultados[i][1]
    tiempos.append(float(ti))
archivo.close()

import matplotlib.pyplot as plt  
plt.figure()
plt.subplot(2,1,1)
x = [10,20,50,100,200,500,1000]
y = [0.1e-3,1e-3,1e-2,0.1,1.,10.,60,60*10, 60*100]
xlabel = ["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
ylabel = ["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"] 
ylabel2 = ["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","10 GB","100 GB"]
y2 = [10**3,10**4,10**5,10**6,10**7,10**8,10**9,10**10]
l1 = [0.1e-4,20000,1e-2,6000]
l2 = [0.1e-4,20000,1e-2,10000000000]
plt.loglog(Nval,tiempos,"-o")
plt.xticks(x,[])
plt.yticks(y,ylabel)
plt.grid(True) 
plt.title("Rendimiento A@B")
plt.ylabel("Tiempo Transcurrido (s)")
plt.subplot(2,1,2)
plt.loglog(Nval,memoria,"-o")  
plt.xticks(x,xlabel,rotation=45)
plt.yticks(y2,ylabel2)
plt.grid(True) 
plt.ylabel("Uso Memoria (BYTES)")
plt.xlabel("Tamaño de la matriz")


plt.savefig("timing_inv_caso_2_longdouble.png")
