# PyTTS - Conversor de Texto a Voz

Una sencilla aplicación de línea de comandos en Python para convertir archivos de texto (.txt) a archivos de audio (.mp3) utilizando el servicio de texto a voz de Microsoft Edge.

## Características

- Lista las voces disponibles en múltiples idiomas y acentos.
- Guarda tu voz preferida para usos futuros.
- Detecta automáticamente los archivos `.txt` en el directorio.
- Permite nombrar el archivo de audio de salida.

## Requisitos

- Python 3.6 o superior.
- Las librerías listadas en `requirements.txt`.

## Instalación

1.  **Clona o descarga este repositorio.**

2.  **Navega al directorio del proyecto.**
    ```bash
    cd ruta/a/PyTTS
    ```

3.  **Crea un entorno virtual (recomendado).**
    ```bash
    python -m venv venv
    ```
    Y actívalo:
    - En Windows:
      ```bash
      venv\Scripts\activate
      ```
    - En macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4.  **Instala las dependencias.**
    ```bash
    pip install -r requirements.txt
    ```

## Modo de Uso

1.  **Prepara tus archivos de texto.**
    Asegúrate de que los archivos de texto que quieres convertir (con extensión `.txt`) se encuentren en la misma carpeta que el programa.

2.  **Ejecuta la aplicación.**
    ```bash
    python app.py
    ```

3.  **Selecciona una voz.**
    - La primera vez que lo ejecutes, o si no hay una voz guardada, el programa te mostrará una lista completa de voces disponibles. Deberás elegir una introduciendo su número.
    - Si ya has usado el programa antes, te preguntará si quieres reutilizar la última voz guardada. Si dices que no (`n`), te volverá a mostrar la lista para que elijas una nueva. La voz que elijas quedará guardada para la próxima vez.

4.  **Selecciona un archivo de texto.**
    El programa listará los archivos `.txt` disponibles en el directorio. Introduce el número correspondiente al archivo que deseas convertir.

5.  **Nombra el archivo de salida.**
    Escribe el nombre que quieres darle a tu archivo de audio. Por ejemplo, `mi_audio`. La extensión `.mp3` se añadirá automáticamente si no la incluyes.

6.  **¡Listo!**
    El programa generará el archivo de audio en el mismo directorio.

## Configuración

El archivo `config.json` se crea automáticamente para almacenar la última voz que seleccionaste. No necesitas editarlo manualmente, pero si lo eliminas, el programa te pedirá que elijas una voz de la lista completa en la siguiente ejecución.
