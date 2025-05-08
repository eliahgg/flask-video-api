import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Willkommen bei meiner API!"

@app.route('/convert', methods=['POST'])
def convert_file():
    # Datei empfangen und speichern
    file = request.files['file']
    filename = "input.mp4"
    file.save(filename)

    # Ziel-Dateipfad für die konvertierte Datei
    output_file = "C:/Users/eliah/OneDrive/Bilder/Eliah.T/output.avi"

    # Lösche die vorhandene Datei, falls sie schon existiert
    if os.path.exists(output_file):
        os.remove(output_file)

    # FFmpeg-Befehl mit automatischem Überschreiben (-y)
    result = os.system(f'ffmpeg -y -i {filename} {output_file}')

    # Erfolgsprüfung
    if result == 0:
        return {"message": "Konvertierung abgeschlossen!", "output_file": output_file}
    else:
        return {"error": "Fehler bei der Konvertierung!"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
