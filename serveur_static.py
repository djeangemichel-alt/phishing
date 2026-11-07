from sqlite3 import Date
from flask import Flask, render_template_string, request
from datetime import datetime 
import csv 
import os # une bibliothèque pour gérer les fichiers et les chemins de fichiers

app = Flask(__name__)

PAGE = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>laboratoire</title>
</head>
<body>
   <h1>Laboratoire de cybersécurité</h1>
    <p>Cette expérience permet d'observer votre adresse IP
       dans le cadre d'un test réseau.</p>

    <form method="POST" action="/consentement">
        <label>
            <input type="checkbox" name="consentement"
                   value="oui" required>
            J'accepte que mon adresse IP soit enregistrée
            pour cette expérience.
            <br><br>
            <input type ="text" name = "verifie" required>
            mentionné  lu et approuvé
        </label>
        <br><br>
        <button type="submit">Participer au test</button>
    </form>
</body>
</html>
    """

PAGE2 = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>laboratoire</title>
</head>
<body>
   <h1> Merci pour votre participation ! </h1>
</body>
</html>

"""
@app.route("/")
def accueil():
    return render_template_string(PAGE)

@app.route("/consentement", methods=["POST"])
def consentement():
    if request.form.get("consentement") != "oui":
        return "consentement requis", 400
    
    ip = request.remote_addr
    navigateur = request.headers.get("User-Agent", "Inconnu")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    fichier = "visiteurs.csv"
    nouveau_visiteurs = not os.path.exists(fichier)

    with open(fichier, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if nouveau_visiteurs:
            writer.writerow(["Date", "Adresse IP", "Navigateur"])

        writer.writerow([date, ip, navigateur])

    return render_template_string(PAGE2)    

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
