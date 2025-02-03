# Music Mixer
Un script en Python que permite crear listas de reproducción a partir de carpetas seleccionadas por el usuario. Incluye opciones de personalización y guarda las preferencias para futuras ejecuciones.

[Haz clic aquí para la versión en inglés de este README](README-EN.md)

## Motivación y problema que resuelve
Este programa surgió de una necesidad real a la que me enfrenté: resolver el problema de tener una lista de canciones larga en un parlante que usa un pendrive y no permite navegar entre carpetas.  

El problema es que cada vez que se enciende el parlante, comienza con la primera canción del pendrive. Esto hace que la música se vuelva repetitiva y ademas, si hay muchas canciones, las últimas quizá nunca lleguen a sonar, en caso de que el parlante no esta encendido por el tiempo suficiente.  

Este programa permite generar automáticamente una mezcla de canciones en una nueva carpeta según las preferencias del usuario.  

La primera versión la creé para un negocio fisico de mi padre, donde se usaba un parlante con pendrive sin opción de navegar entre carpetas. Con el tiempo la mejoré hasta convertirla en una solución flexible y automatizada.


## Características principales
- Permite seleccionar múltiples carpetas de origen.
- Definir una carpeta de destino.
- Mantener el orden de las carpetas o mezclar las canciones.
- Opción de definir un total de canciones para la mezcla o por carpeta.
- Guarda las preferencias del usuario para futuras ejecuciones.


## Instalación y uso
1. Clonar el repositorio:  
    ```sh
    git clone https://github.com/Joaco-Femenia/music-mixer.git
    ```
2. Instalar las dependencias:  
    ```sh
    pip install -r requirements.txt
    ```
3. Navegar hasta la carpeta del proyecto:  
    ```sh
    cd ruta/del/proyecto
    ```
4. Ejecutar el programa con Python:  
    ```sh
    python main.py
    ```
    **En Windows, usa cmd o PowerShell. En macOS/Linux, usa la terminal.**


## Contribuciones y contacto
**Autor:** Joaquín Femenia  
**GitHub:** [Joaquin-Femenia](https://github.com/Joaquin-Femenia)  
**Contribuciones:** ¡Pull requests y sugerencias son bienvenidas!