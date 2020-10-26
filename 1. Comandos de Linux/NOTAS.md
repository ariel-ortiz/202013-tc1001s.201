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

Visualizar contenido de un archivo por página. Presionar la tecla `q` (_quit_) para salir, para navegar usar flecha arriba, flecha abajo, barra espaciador, enter, Shift-G para ir al final del archvivo.

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
