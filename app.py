from flask import Flask, render_template, request, url_for, flash, redirect
from datetime import datetime

app = Flask(__name__)
app.secret_key = "Hello_baquit"

messages = []
books_list = ["Туча", "И.И. Пущину"]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get('name', '').strip()
        text = request.form.get('text', '').strip()
        if name and text:
            messages.append({"name": name, "text": text, "time": datetime.now().strftime("%d.%m.%Y %H:%M")})
            flash("Спасибо, ваше сообщение добавленно", "success")
            return redirect(url_for("index"))
        flash("Заполните имя и текст сообщения", "error")
    return render_template("index.html", messages=messages)

@app.route("/about")
def about():
    return render_template("about.html", total = len(messages))

@app.route("/books")
def books():
    return render_template("books.html", count = len(books_list))

@app.route("/one")
def books2():
    return render_template("bookone.html")

@app.route("/two")
def books3():
    return render_template("booktwo.html")


@app.errorhandler(code_or_exception=404)
def page_not_found(error):
    return render_template(template_name_or_list="404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)