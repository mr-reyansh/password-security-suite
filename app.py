from flask import Flask, render_template, request
from utils.hybrid import hybrid_crack
from utils.rainbow import rainbow_crack
from utils.brute import brute_force_crack
from utils.bcrypt_utils import hash_bcrypt
from utils.strength_check import check_strength

import hashlib
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/attack", methods=["GET", "POST"])
def attack():

    result = None

    if request.method == "POST":

        target_hash = request.form["target_hash"]
        method = request.form["method"]

        wordlist_file = request.files.get("wordlist")
        filepath = None

        if wordlist_file and wordlist_file.filename != "":
            filepath = os.path.join(UPLOAD_FOLDER, wordlist_file.filename)
            wordlist_file.save(filepath)

        try:

            if method == "hybrid" and filepath:
                result = hybrid_crack(target_hash, filepath)

            elif method == "rainbow":
                rainbow_path = "static/rainbow.txt"
                result = rainbow_crack(target_hash, rainbow_path)

            elif method == "brute":
                max_length = int(request.form.get("max_length", 4))
                result = brute_force_crack(target_hash, max_length)

            else:
                result = "Invalid configuration"

        except Exception as e:
            result = f"Error: {str(e)}"

        finally:
            if filepath and os.path.exists(filepath):
                os.remove(filepath)

    return render_template("attack.html", result=result)


@app.route("/defense", methods=["GET", "POST"])
def defense():

    strength = None
    hashed = None

    if request.method == "POST":

        password = request.form["password"]
        method = request.form["method"]

        strength = check_strength(password)

        if method == "sha256":
            hashed = hashlib.sha256(password.encode()).hexdigest()

        elif method == "bcrypt":
            hashed = hash_bcrypt(password)

    return render_template("defense.html", strength=strength, hashed=hashed)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)