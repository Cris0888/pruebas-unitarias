from suma import *

def test_menor():
    assert menor(9,10)

def test_mayor():
    assert mayor(10,5)

def test_suma():
    assert suma(5,5) == 10

def test_resta():
    assert resta(9,9) == 0



""" calidad de software es vital que lo que programemos lo probemos porque asi nos daremos cuenta si en realidad 
programamos lo que esperabamos para inicial con una pruebra unitaria paso uno crear un archivo donde haremos el codigo
que vamos a probar en este caso se llama suma el archivo despues todo archivo de prueba debe tener
el nombre como inicio de test gion bajo y el nombre del archivo que vamosa probar en este caso es uma
asi que debe llamarse test_suma.py despues importamos el archivo que deseamos probar despues creamos
las funciones de prueba todo funcion debe tener el nombre de test guion bajo y nombre del metodo que vamos a probar
ejemplo suma entonces ponemos def test_suma() y despues ponemos el comando assert que es que hace la validacion
en este caso como es una suma ponemos assert suma(5,5) ==10 debemos poner siempre el igual y igual y el resultado que 
esperamos de esa prueba para ejecutar las pruebas ponemos en la terminal de comando pytest si queremos
que nos de mas detalle en especifico del los metodos de prueba ponemos pytest -v """