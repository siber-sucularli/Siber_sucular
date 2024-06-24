from flask import Flask, render_template, request, redirect, url_for
import base64

app = Flask(__name__)

# Base64 ile kodlanmış flag
F = "SE0yMDI0e1doMF9AbV9JfQ=="

# Basit bir kullanıcı doğrulama sistemi için örnek kullanıcı verileri
users = {
    "admin": "password123",
    "user": "mypassword"
}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username] == password:
            return redirect(url_for("dashboard", username=username))
        else:
            return "Kullanıcı adı veya şifre yanlış", 401
    return render_template("login.html")

@app.route("/dashboard/<username>")
def dashboard(username):
    if username in users:
        return f"Merhaba, {username}! Dashboard'a hoş geldiniz."
    else:
        return "Yetkisiz erişim", 403

@app.route("/secret")
def secret():
    return f"Flag: {encoded_flag}"

if __name__ == "__main__":
    app.run(debug=True)
