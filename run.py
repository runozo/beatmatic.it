#! python3
# -*- coding: utf-8 -*-

from beatmatic import app


@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
