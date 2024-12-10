from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world() -> str:
    return "<p>Hello Boy</p>"


@app.route("/<name>")
def hello(name: str) -> str:
    return f"Hello, {escape(name)}!"


# def main() -> None:
#
#
# if __name__ == "__main__":
#     main()
