from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        return f"Thank you for registering, {name}!"
    return '''
        <form method="post">
            Name: <input name="name"><br>
            Email: <input name="email"><br>
            <input type="submit">
        </form>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)