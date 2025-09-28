# Practica 4 

- Creamos la funcion inicializar la tortuga para de esta manera definir los parametros de la pantalla, el titulo, el color del fondo y la velocidad de la tortuga.
- Colocamos las funciones ya previamente creadas en la practica 1, de igual manera su instrucciones en el dibujante.txt.
- Creamos la funcion ejecutar comando para de esta manera tomar la instruccion valida del dibujante.txt y este pueda ejecutarlo, si el usuario se equivoca al insertar la instruccion se le presentara una advertencia de "Comando no reconocido"
- Utilizamos try y un if, asi como elif anidado para los diversos comandos, al final con la exception, le arrojara al usuario un mensaje de "error ejecutando".
- Definimos la funcion en este caso sera el modo interactivo con el usuario, presentandole un menu pequeño sobre lo que quiere realizar, colocamos un bucle infinito.
- En este caso mientras sea verdad lo que el usuario decida, le arrojara un mensaje de comando ejecutado o comando invalido, al mismo tiempo si es valido el mensaje, se actualizara en la pantalla del turtle.
-Agregamos una excepcion si el usuario presiona Ctrl+C se saldra de la ventana y la dara un mensaje de Bye Bye en la terminal, saliendo del bucle con un break.
- La funcion leer el archivo, utilizara el dibujante.txt, para leer todas las lineas, y mostrar los comandos ejecutados, diciendo si hubo o no errores, contabilizandolos.
- Si el archivo ejecutado no se encuentra, tendra una excepcion FileNotFountError.
- La funcion mostrar ayuda, le dara las herramientas al usuario para poder ejecutar cada una de las intrucciones, siendo estas los comandos disponibles.
- Al final en la funcion main, vamos a imprimir al usuario que esta es la practica 4, y que a continuacion tenemos un menu con las funciones que le podemos ofrecer.
- Despues dependiendo del numero que ingrese el usuario con un condicional if ira recorriendo cada una de las opciones, si no interactua con una de la (1-4) le arrojaremos un else con la leyenda opcion invalida, y las opciones que puede utilizar.

**Esta practica fue creada con la version de python 3.11.9**