import edge_tts
import asyncio
import os
import json

CONFIG_FILE = "config.json"

# -----------------------------------
# Función para cargar la configuración
# -----------------------------------
def cargar_config():
    """Carga la configuración desde un archivo JSON."""
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Advertencia: El archivo de configuración está dañado. Se reiniciará.")
            return {}
    return {}

# -----------------------------------
# Función para guardar la configuración
# -----------------------------------
def guardar_config(config):
    """Guarda la configuración actual en un archivo JSON."""
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)

# -----------------------------------
# Función para listar las voces
# -----------------------------------
async def listar_voces():
    """Obtiene y muestra la lista de voces disponibles."""
    print("Obteniendo lista de voces disponibles...\n")
    voces = await edge_tts.list_voices()

    for idx, voz in enumerate(voces):
        short_name = voz.get("ShortName", "Desconocido")
        gender = voz.get("Gender", "Desconocido")
        locale = voz.get("Locale", "Desconocido")
        friendly_name = voz.get("FriendlyName", short_name)

        print(f"{idx + 1}. {short_name} - {gender} - {locale} - {friendly_name}")

    return voces

# -----------------------------------
# Función para convertir texto a audio
# -----------------------------------
async def texto_a_audio(voz, texto, archivo_salida):
    """Convierte texto a audio usando la voz seleccionada."""
    comunicador = edge_tts.Communicate(texto, voz)

    print("\nGenerando archivo de audio, por favor espera...")
    with open(archivo_salida, "wb") as f:
        async for chunk in comunicador.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])

    print(f"\nArchivo generado correctamente: {archivo_salida}")

# -----------------------------------
# Listar archivos .txt en la carpeta
# -----------------------------------
def listar_archivos_txt():
    """Lista todos los archivos .txt en el directorio actual."""
    archivos = [f for f in os.listdir('.') if f.lower().endswith('.txt')]

    if not archivos:
        print("No se encontraron archivos .txt en el directorio actual.")
        return []

    print("\nArchivos de texto disponibles:")
    for idx, archivo in enumerate(archivos, start=1):
        print(f"{idx}. {archivo}")

    return archivos

# -----------------------------------
# Selección de voz con configuración
# -----------------------------------
async def seleccionar_voz(config):
    """
    Permite seleccionar la voz a usar.
    Si existe una voz guardada en config.json, pregunta si se quiere reutilizar.
    """
    if "voz" in config:
        usar_guardada = input(
            f"\n¿Quieres usar la voz guardada anteriormente '{config['voz']}'? (s/n): "
        ).strip().lower()
        if usar_guardada == "s":
            print(f"Usando voz guardada: {config['voz']}")
            return config["voz"]

    # Si no hay voz guardada o el usuario quiere elegir otra
    voces = await listar_voces()
    eleccion = int(input("\nSelecciona el número de la voz que deseas usar: "))

    if eleccion < 1 or eleccion > len(voces):
        print("Error: selección inválida.")
        return None

    voz_elegida = voces[eleccion - 1]["ShortName"]
    config["voz"] = voz_elegida
    guardar_config(config)  # Guardar la voz seleccionada
    print(f"\nVoz seleccionada y guardada: {voz_elegida}")
    return voz_elegida

# -----------------------------------
# Función principal
# -----------------------------------
async def main():
    config = cargar_config()

    # 1. Seleccionar voz (usando config si existe)
    voz_elegida = await seleccionar_voz(config)
    if not voz_elegida:
        return

    # 2. Listar archivos de texto
    archivos_txt = listar_archivos_txt()
    if not archivos_txt:
        return

    eleccion_txt = int(input("\nSelecciona el número del archivo de texto a convertir: "))

    if eleccion_txt < 1 or eleccion_txt > len(archivos_txt):
        print("Error: selección inválida.")
        return

    archivo_txt = archivos_txt[eleccion_txt - 1]

    # 3. Leer contenido del archivo
    with open(archivo_txt, "r", encoding="utf-8") as f:
        texto = f.read()

    if not texto.strip():
        print("Error: el archivo está vacío.")
        return

    # 4. Preguntar nombre de archivo de salida
    archivo_salida = input("\nNombre del archivo de salida (ejemplo: resultado.mp3): ")
    if not archivo_salida.lower().endswith(".mp3"):
        archivo_salida += ".mp3"

    # 5. Convertir texto a audio
    await texto_a_audio(voz_elegida, texto, archivo_salida)

# -----------------------------------
# Ejecutar el programa
# -----------------------------------
if __name__ == "__main__":
    asyncio.run(main())
