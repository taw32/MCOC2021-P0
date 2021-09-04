# MCOC2020-P0

# Mi computador

* Modelo: MacBook Air (13-inch, Mid 2013)
+ Nombre del procesador:	Intel Core i5 de dos núcleos
+ Numero de núcleos: 2
+ Numero de hilos:

+ Memoria: 4 GB 1600 MHz DDR3 (frecuencia de RAM 1600 MHz)
+ Almacenamiento 251 GB Almacenamiento flach
+ Grafica Intel HD Graphics 5000 1536
+ Identificador del modelo:	MacBookAir6,2
+ Velocidad del procesador:	1,3 GHz
+ Cantidad de procesadores:	1
+ Cantidad total de núcleos:	2
+ Caché de nivel 2 (por núcleo):	256 KB
+ Caché de nivel 3:	3 MB
+ Tecnología Hyper-Threading:	Activado
+ Memoria:	4 GB


# Desempeño Matmul

* ¿en que difieren el gráfico del profesor con el del ayudante?
+ El gráfico del profesor pareciera que está hecho con un computador mas potente, el mio se demora mas en menos repeticiones 
* ¿a que se deben estas diferencias?
+ al cumputador, el mio tiene 2 nucleos y 4 GB de memoria RAM
+ Se deben a que son computadores distintos, y por ende difenrente memoria ram
* El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?
+ el grafico de uso de memoria es lineal porque a medida que aumenta el tamaño de la matriz, a si mismo aumenta la memoria, en cambio, cuando ya se esté usando un núcleo, para las matrices mas grandes, luego se va a demorar mas en  hacer los otros 
* ¿Qué versión de python está usando?
+ python 3.8
* ¿Qué versión de numpy está usando?
+ La por defecto de anaconda

![image](https://user-images.githubusercontent.com/69284354/131904732-4151314d-b47d-46db-afbe-4689d79a1b97.png)

# Desempeño INV
* ¿Qué algoritmo de inversión cree que utiliza cada método (ver wiki)? Justifique claramente su respuesta.

* ¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso? Justifique su comentario en base al uso de procesadores y memoria observado durante las corridas.  


# Desempeño de solve y eigh

* Los casos de este trabajo están en el mismo orden de el enunciado.
* ¿Como es la variabilidad del tiempo de ejecucion para cada algoritmo?
+ En el caso 1 para la 2da parte (eigh), los datos del tipo double se demoran mas que los float (yo usé float 32 para todos). Lo mismo para el operador solve, sin embargo en este caso para la primera matriz el caso solve double le costó considerablemente más partir.
+ La dispersión en todos los casos es bastante chica viendo las diferentes corridas varian desde el 1 ms a 0,1 s max 1,2 s en los casos mas extremos. 
+ En los casos 2 y 3 el tiempo varia muhco mas con el operador eigh, y con respecto al tipo de datos, muy similar float y double.
+ Para el caso 4 las disperciones son menores con un pico en la dimencion 40 para el operador eigh, el operador solve varia de 1ms a 0,1 seg aprox.
+ En este caso las diperciones se comportan muy parecidos al 4 siendo ligeramente mayores para los 2 operadores.
+ Para el caso 6 volvio una disperción mayor, en el operaador eigh principalmente.
+ Los 3 casos restantes 7 8 y 9 solo tiene operador eigh.

# Gráficos

![1 eigh double](https://user-images.githubusercontent.com/69284354/131425582-d1ca9df9-2d88-4058-afc9-19a5e7e96b10.png)
![1 eigh float](https://user-images.githubusercontent.com/69284354/131425682-8d201d20-3413-4a77-9e73-32941bf208ee.png)
![1 solve double](https://user-images.githubusercontent.com/69284354/131425730-318e49f8-e30b-4a35-809d-5e07064c362a.png)
![1 solve float](https://user-images.githubusercontent.com/69284354/131425746-5635d85e-4459-40dc-9a4c-6bbf57e8763c.png)


* ¿Qué algoritmo gana (en promedio) en cada caso?
+ Caso 1 gana solve considerablemente en los datos double y float.
+ Caso 2 gana solve considerablemente en los datos double y float.
+ Caso 3 gana solve considerablemente en los datos double y float.
+ Caso 4 gana solve pero muy equiparado, el max de eigh float es 0,11 s y el de solve es 0,93 s. en los datos tipo double, hay mas separacion ganando solve.
+ caso 5 gana solve considerablemente en los datos double y float.
+ Caso 6 están muy juntos en el caso de los datos double, y gana solve para los datos float. Float y double muy parecidos.
+ Caso 7 Caso 8 Caso 9 solo hay para casos eigh, muy parecidos los datos float y solve.

* ¿Depende del tamaño de la matriz?
+ Claramente depende de el tamaño, generalemente, el operador solve parte mas rápido resolviendo las matrices pequeñas, sin embargo cuando las matrices pasan la dimension 200, estas empiezan a igualarse hasta llegar a la 1000, ahí generalemente son iguales. Siendo el float 32 bastante mas rápido que el double.

* ¿A que se puede deber la superioridad de cada opción?
+ Para matrices chicas, sacar el inverso de la matriz A no toma tanto tiempo, sin embargo para matrices mas grandes ya empieza a ser una operación que ocupa mas tiempo, por eso, el operador eigh a partir de la dimención 200 ya empieza a pillarlo en tiempo.

* ¿Su computador usa más de un proceso por cada corrida?
+ Si, cambia con las matrices mayores a 200.

* ¿Que hay del uso de memoria (como crece)? 
+ La memoria va creciendo hasat la matriz dimención 200, luego baja. 

# (Entrega 5) El Código de ensamblaje es:

```def matriz_laplaciana_dispersa(N, dtype=np.double):
    A= lil_matrix((N,N))
    for i in range(N):
        for j in range(N):
            if i == j:
                A[i,j]=2
            if i +1== j:
                A[i,j] = -1
            if i - 1 == j:   
                A[i,j] = -1
    return csc_matrix(A)```
    

* Aquí se ve claramente que la matriz laplaciana es bastante mas rapida que la matriz normal, esto se ve reflejado en los gráficos.
+ ![image](https://user-images.githubusercontent.com/69284354/132101672-8d21d973-c994-452c-a37e-5c70e6f20669.png)
+ ![image](https://user-images.githubusercontent.com/69284354/132101678-d84ee4b9-3b1a-46bd-ba3a-d24ddd49fbfc.png)
