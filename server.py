from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route("/")
def index():
    mysql = connectToMySQL("c_r_pets")
    pets = mysql.query_db("SELECT * FROM pets;")
    print(pets)
    return render_template("index.html", all_pets = pets)

@app.route("/create_pet", methods=["POST"])
def add_pet_to_db():
    mysql = connectToMySQL("c_r_pets")
    query = "INSERT INTO pets (name, type, created_at, updated_at) VALUES (%(nm)s, %(tp)s, NOW(), NOW());"
    data = {
        "nm": request.form["name"],
        "tp": request.form["type"]
    }
    mysql.query_db(query, data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)