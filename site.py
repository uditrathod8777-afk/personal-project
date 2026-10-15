from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = "change-this-to-a-random-secret-key"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        flash("Please fill in all fields.", "error")
        return redirect("/")

    if len(name) > 100 or len(email) > 254 or len(message) > 3000:
        flash("Your submitted information is too long.", "error")
        return redirect("/")

    if "@" not in email or "." not in email.rsplit("@", 1)[-1]:
        flash("Please enter a valid email address.", "error")
        return redirect("/")

    # Demo: form data is processed but not saved or emailed.
    print("New contact message received")
    print("Name:", name)
    print("Email:", email)
    print("Message:", message)

    flash("Thank you! Your message was received by the demo server.", "success")
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)