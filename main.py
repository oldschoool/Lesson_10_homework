#import required functions
from flask import Flask
from utils import get_all, load_candidates, get_by_pk, get_by_skill

app = Flask(__name__)


@app.route("/")
def all_candidates():
    """function downloads all the candidates to website"""
    candidates = get_all()
    result = ''
    for candidate in candidates:
        result += "<br>"
        result += candidate["name"] + "<br>"
        result += candidate["position"] + "<br>"
        result += candidate["skills"] + "<br>"
        result += "<br>"
    return f"<pre> {result} </pre>"


@app.route("/candidate/<int:pk>")
def get_candidate(pk):
    """function put candidates to each website directory according to his/her id/pk"""
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



@app.route("/candidate/<skills>")
def get_candidate_by_skills(skills):
    """function put candidates to each website directory according to his/her skills"""
    candidates = get_by_skill(skills)
    for candidate in candidates:
        result = ""
        result += "<br>"
        result += candidate["name"] + "<br>"
        result += candidate["position"] + "<br>"
        result += candidate["skills"] + "<br>"

    return f"<pre> {result} </pre>"

app.run(debug=True)