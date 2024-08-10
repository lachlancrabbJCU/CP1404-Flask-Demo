from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    """Display Hello World with HTML formatting."""
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    """Display greeting to name in url."""
    return f"Hello {name}"


@app.route('/f/<celsius>')
def display_fahrenheit(celsius):
    """Display converted Fahrenheit from Celsius in url."""
    celsius = validate_float(celsius)
    if celsius:
        fahrenheit = convert_celsius_fahrenheit(celsius)
        return f"{celsius} C is {fahrenheit} F"
    return "Invalid input e.g. url/f/10.0"


@app.route('/c/<fahrenheit>')
def display_celsius(fahrenheit):
    """Display converted Celsius from Fahrenheit in url."""
    fahrenheit = validate_float(fahrenheit)
    if fahrenheit:
        celsius = convert_fahrenheit_celsius(fahrenheit)
        return f"{fahrenheit} F is {celsius} C"
    return "Invalid input e.g. url/c/10.0"


def validate_float(string):
    """Validate string can be cast to float type."""
    try:
        valid_float = float(string)
        return valid_float
    except ValueError:
        return None


def convert_fahrenheit_celsius(fahrenheit):
    """Convert fahrenheit to celsius."""
    return 5 / 9 * (fahrenheit - 32)


def convert_celsius_fahrenheit(celsius):
    """Convert celsius to fahrenheit."""
    return celsius * 9.0 / 5 + 32


if __name__ == '__main__':
    app.run()
