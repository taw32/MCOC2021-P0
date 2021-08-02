from scipy import matrix, rand, loadtxt
from time import perf_counter

#Tamaño de matrices
Ns= [2,5,10,12,15,20,30,40,45,50,50,60,75,100,125,160,200,250,350,500,600,800,1000,2000,5000]#,10000]

Ncorridas=10

for i in range(Ncorridas):
    dts=[ ] #tiempos
    mem=[ ] #memoria
    
    name = f"matmul{i}.txt"
    fid= open( name , "w" )
    
    for N in Ns:
        
        print (f"N = {N}")
        
        A = rand(N,N)
        B = rand(N,N)

        t1 = perf_counter()
        C = A@B
        t2 = perf_counter()

        dt = t2 - t1
        size= 3 * ( N ** 2 ) * 8
        
        # KB = 10^3 Bytes
        # MB = 10^3 KB
        # GB = 10^3 MB
        
        dts.append(dt)
        mem.append(size)
        
        fid.write(f" {N}  {dt}  {size} \n")
        
        print (f"tiempo transcurrido: {dt} s")
        print (f"memoria: {size} bytes")
        fid.flush()
