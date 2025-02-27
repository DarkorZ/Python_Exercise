Question 
If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one byte will still use 4096 bytes of storage. A file made up of 4097 bytes will use 4096*2=8192 bytes of storage. 
Knowing this, can you fill in the gaps in the calculate_storage function below, which calculates the total number of bytes needed to store a file of a given size?


print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192


//------------------------------SPANISH-----------------------//

Pregunta 5
Si un sistema de archivos tiene un tamaño de bloque de 4096 bytes, esto significa que un archivo compuesto por un solo byte seguirá utilizando 4096 bytes de almacenamiento. 
Un archivo compuesto por 4097 bytes utilizará 4096*2=8192 bytes de almacenamiento. 
Sabiendo esto, ¿puede rellenar los huecos de la función calcular_almacenamiento que aparece a continuación, que calcula el número total de bytes necesarios para almacenar un archivo de un tamaño determinado?
print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192
