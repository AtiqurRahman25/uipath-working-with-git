from flask import Flask, request, render_template
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("landing-page.html")


@app.route("/form", methods=["GET"])
def form():
    return render_template("form.html")


@app.route("/submit", methods=["GET", "POST"])
def submit():

    if request.method == "GET":
        return "Please submit the form using the Submit Request button."

    # Receive form data
    name = request.form.get("name")
    email = request.form.get("email")
    service = request.form.get("service")
    message = request.form.get("message")

    print("New Form Submission")
    print("Name:", name)
    print("Email:", email)
    print("Service:", service)
    print("Message:", message)

    # Selenium configuration
    options = Options()
    options.add_argument("--start-maximized")

    driver = None

    try:
        driver = webdriver.Chrome(options=options)

        # Open test website
        driver.get("https://example.com")

        print("Selenium started successfully!")

    except Exception as e:
        print("Selenium Error:", str(e))

    finally:
        if driver:
            driver.quit()

    return f"""
    <html>
    <body style="font-family: Arial; text-align:center; padding:60px;">
        <h1>Request Submitted Successfully!</h1>
        <h3>Welcome, {name}!</h3>
        <p>Email: {email}</p>
        <p>Service: {service}</p>
        <a href="/">Back to Home</a>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True, port=5000)
