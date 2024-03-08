# pruebas-unitarias
pruebas unitarias bajo la libreria de python pytest

""" calidad de software es vital que lo que programamos lo probamos porque asi nos daremos cuenta si en realidad 
programamos lo que en realidad esperabamos para inicial con una pruebra unitaria paso 1 debemos crear un archivo donde haremos el codigo
que vamos a probar en este caso se llama suma el archivo de prueba 2 todo archivo de prueba debe tener
el nombre como inicio de test gion bajo _ y el nombre del archivo que vamos a probar en este caso es suma
asi que debe llamarse test_suma.py despues importamos el archivo que deseamos probar 3 creamos
las funciones de prueba toda funcion debe tener el nombre test guion bajo _ y nombre del metodo que vamos a probar
ejemplo en este caso se llama suma asi que pondremos def test_suma() y despues ponemos el comando assert que es que hace la validacion
en este caso como es una suma ponemos assert suma(5,5) == 10 debemos poner siempre el igual y igual == y el resultado que 
esperamos de esa prueba para ejecutar el archivo de  las pruebas ponemos en la terminal de comandos pytest si queremos
que nos de mas detalle en especifico del los metodos de prueba ponemos pytest -v "
