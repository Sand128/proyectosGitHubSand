import speech_recognition as sr
import subprocess
 
def abrir_programa(programa):
    try:
        subprocess.Popen(programa)
    except Exception as e:
        print(f"No se pudo abrir el programa {programa}. Error: {e}")
 
def reconocer_comando():
    recognizer = sr.Recognizer()
 
    with sr.Microphone() as source:
        print("Abrir el programa:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
 
    try:
        comando = recognizer.recognize_google(audio, language="es-ES").lower()
        print(f"Comando reconocido: {comando}")
        return comando
    except sr.UnknownValueError:
        print("No se pudo entender el comando.")
        return None
    except sr.RequestError as e:
        print(f"Error al hacer la solicitud a la API de reconocimiento de voz: {e}")
        return None
 
if __name__ == "__main__":
    while True:
        comando = reconocer_comando()
 
        if comando:
            if "abrir" in comando and "programa" in comando:
             
                abrir_programa("notepad.exe")  
            elif "salir" in comando or "terminar" in comando:
                print("Saliendo del programa.")
                break
            else:
                print("Comando no reconocido.")