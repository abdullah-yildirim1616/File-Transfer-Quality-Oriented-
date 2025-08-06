from flask import Flask, render_template, send_from_directory, request
import os

app = Flask(__name__)

# Paylaşılan kök dizin (burayı kendi sistemine göre ayarla)
BASE_DIR = os.path.expanduser("C:\\Users\\abdus\\OneDrive\\Masaüstü")  # örnek olarak Kullanıcı klasöründeki "Shared"

@app.route("/")
def index():
    # Belirli dizindeki alt klasörleri ve dosyaları listele
    folders = []
    files = []

    current_path = request.args.get("path", BASE_DIR)

    try:
        for entry in os.listdir(current_path):
            full_path = os.path.join(current_path, entry)
            if os.path.isdir(full_path):
                folders.append(entry)
            elif os.path.isfile(full_path):
                files.append(entry)
    except Exception as e:
        print("HATA:", e)

    return render_template("index.html", folders=folders, files=files, current_path=current_path)

@app.route("/download")
def download():
    path = request.args.get("path")
    directory = os.path.dirname(path)
    filename = os.path.basename(path)
    return send_from_directory(directory, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
