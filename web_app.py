from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def start(name1 = None, name2 = None):
    return render_template("index.html", name1=name1, name2=name2)

@app.route("/results", methods=["POST"])
def results():
    player1 = str(request.form.get("name1"))
    player2 = str(request.form.get("name2"))
    return render_template("results.html", player1=player1, player2=player2)


if __name__ == "__main__":
    app.run(debug=True)
