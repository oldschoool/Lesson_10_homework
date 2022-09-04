from flask import Flask
from utils import get_all, load_candidates, get_by_pk, get_by_skill

app = Flask(__name__)

@app.route("/")
def all_candidates():
    candidates = get_all()
    result = ''
    for candidate in candidates:
        result += "<br>"
        result += candidate["name"] + "<br>"
        result += candidate["position"] + "<br>"
        result += candidate["skills"] + "<br>"
        result += "<br>"
    return f"<pre> {result} </pre>"

app.run(debug=True)


@app.route("/candidate/<int:pk>")
def get_candidate(pk):
    candidate = get_by_pk(pk)
    result = ''
    result += "<br>"
    result += candidate["name"] + "<br>"
    result += candidate["position"] + "<br>"
    result += candidate["skills"] + "<br>"

    return f"""
      <img src="{candidate['picture']}"> 
      <pre> {result} </pre>
    """

app.run(debug=True)

@app.route("/candidate/<skills>")
def get_candidate_by_skills(skills):
    candidate = get_candidate_by_skills(skills)
    result = ''
    result += "<br>"
    result += candidate["name"] + "<br>"
    result += candidate["position"] + "<br>"
    result += candidate["skills"] + "<br>"

    return f"<pre> {result} </pre>"

app.run(debug=True)