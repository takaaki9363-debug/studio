from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = "newcreatestudio-production-key"

@app.context_processor
def inject_year():
    return {"current_year": datetime.now().year}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/company")
def company():
    return render_template("company.html")

@app.route("/service")
def service():
    return render_template("service.html")

@app.route("/works")
def works():
    return render_template("works.html")

@app.route("/sample")
def sample():
    return render_template("sample.html")

@app.route("/price")
def price():
    return render_template("price.html")

@app.route("/staff")
def staff():
    return render_template("staff.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()
        if not name or not email or not message:
            flash("必須項目を入力してください。", "error")
            return redirect(url_for("contact"))
        # 本番ではここをメール送信・DB保存へ接続します。
        flash("お問い合わせありがとうございます。内容を確認のうえご連絡いたします。", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

if __name__ == "__main__":
    app.run(debug=True)
