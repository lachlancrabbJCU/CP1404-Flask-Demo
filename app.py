from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/f/<celsius>')
def display_fahrenheit(celsius):
    if validate_float(celsius):
        return f"{convert_celsius_fahrenheit(float(celsius))}"
    else:
        return "Invalid input e.g. /f/10.0"


@app.route('/c/<fahrenheit>')
def display_celsius(fahrenheit):
    if validate_float(fahrenheit):
        return f"{convert_fahrenheit_celsius(float(fahrenheit))}"
    else:
        return "Invalid input e.g. /c/10.0"


def validate_float(string):
    """Validate string can be cast to float type."""
    try:
        float(string)
        return True
    except ValueError:
        return False


def convert_fahrenheit_celsius(fahrenheit):
    """Convert fahrenheit to celsius."""
    return 5 / 9 * (fahrenheit - 32)


def convert_celsius_fahrenheit(celsius):
    """Convert celsius to fahrenheit."""
    return celsius * 9.0 / 5 + 32


if __name__ == '__main__':
    app.run()
