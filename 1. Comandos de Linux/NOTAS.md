# Notas sobre línea de comandos de Linux

El shell por omisión se llama `bash`. Pueden usar la tecla `tab` para autocompletar nombres de programas, archivos y directorios. También pueden usar las flechas (arrba, abajo) para navegar en la historia de su shell.

## Comando `ls`

Obtener el listado un directorio.

    ls     # listado normal
    ls -l  # listado extendido
    ls -a  # listado de todos (all)
    ls carpeta
    ls --color # Listado con colores

## Comando `pwd`

Imprimir directorio en curso (_print current working directorio_).

    pwd

## Comando `cd`

Cambiar directorio.

    cd directorio
    cd ..  # Cambiar al directorio padre
    cd /   # Cambiar al directorio raiz
    cd     # Cambiar al directorio del usuario

## Comando `clear`

Limpiar la pantalla de la terminal (opcionalmente pueden usar Ctrl+L).

    clear

## Comando `less`

Visualizar contenido de un archivo por página. Presionar la tecla `q` (_quit_) para salir, para navegar usar flecha arriba, flecha abajo, barra espaciador, enter. Presionar Shift-G para ir al final del archivo y la tecla `g` para ir al principio.

    less archivo
    less /proc/cpuinfo

## Comando `mkdir`

Crear directorio.

    mkdir nombre

## Comando `rmdir`

Remover directorio. Directorio debe estar vacío.

    rmdir nombre

## Comando `rm`

Remover archivos y directorios.

    rm archivo
    rm -rf directorio # Borra directorio y todos sus archivos y subdirectorios.

## Comando `touch`

Crear archivos.

    touch archivo

## Comando `man` y `--help`

Obtener la documentación de algún programa instalado. También se puede obtener información de muchos comandos agregando la opción `--help` al ejecutar dichos comandos.

    man ls
    man man
    ls --help

## Comando `cp`

Copiar archivos.

    cp archivo_fuente directorio_destino
    cp archivo_fuente nuevo_nombre

## Comando `mv`

Mover de localidad a un archivo o cambiarle de nombre.

    mv archivo_fuente directorio_destino
    mv archivo_fuente nuevo_nombre

## Comando `find`

Encontrar un archivo en nuestros directorios de usuario.

    find -name ejemplo2.txt

## Comando `echo`

Desplegar mensaje en la consola.

    echo Hola todos
    echo $USER # Nombre del usuario
    echo $C9_USER # Usuario de Cloud9

## Comando `cat`

Concatenar archivos.

    cat archivo
    cat archivo1 archivo2 ... > salida.txt

## Compilar y correr un programa en C

    gcc archivo.c -o nombre_ejecutable  # Compilar archivo.c
    ./nombre_ejecutable                 # Correr el ejecutable

## Comando `sudo`

Ejecutar comando con privilegio de administrador.

    sudo apt install cowsay

    sudo

## Comodines (_wildcards_)

* Asterisco (`*`) hace _match_ con cualquier secuencia de caracteres.
* Signo interrogación (`?`) hace _match_ con un carácters.

        ls *.txt # Hace match con archivos cuyos nombres contienen la extensión .txt
        ls ???.txt  # Hace match con nombres de 3 caracteres.

## Editores

* vim (`vimtutor`). Para salir: `<Esc>`  `:` `q` `!`
* nano

## Operadores de redirección

* El menor que `<` redirecciona la _entrada estándar_ (teclado de la consola).
* El mayor que `>` redirecciona la _salida estándar_ (pantalla de la consola).
* El mayor que mayor que `>>` redirecciona la _salida estándar_ para hacer un “append”.

        ls > listado.txt
        echo Hola todos > saludos.txt
        python3 suma.py < numeros.txt > salida.txt
        echo Adios mundo cruel >> saludos.txt





