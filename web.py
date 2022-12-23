import os
import requests
from flask import Flask, render_template, render_template_string, request

app = Flask(__name__)
REST_URL = os.environ.get("REST_URL", "http://localhost/")

@app.route("/")
def start():
    return render_template("index.html")

def render_result(q=None):
    if q:
        query = f'{REST_URL}genre_all?where={{%22verb%22:%20%22{q.lower()}%22}}&max_results=50'
        items = requests.get(query).json().get("_items")
        if not items:
            return render_template_string(f'<div>Глагол "{q}" не найден.</div>')
        else:
            return render_template("result.html", items=items)
    else:
        return render_template_string("<div> </div>")   

@app.route("/search", methods=["GET"])
def search():
    q = request.values.get("q")
    result = render_result(q=q)
    return render_template("search.html", result=result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")