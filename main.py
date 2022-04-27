from flask import Flask, render_template

from utils import *
from jinja2 import Template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('list.html')


@app.route('/candidates/<candidate_name>')
def candidate_page_name(candidate_name):
    candidat_raw = load_candidates_from_json('candidates.json')

    return format_candidates(get_candidates_by_name(candidat_raw, candidate_name))


@app.route('/candidates/<int:candidate_id>')
def candidate_page(candidate_id):
    candidat_raw = load_candidates_from_json('candidates.json')
    candidate = get_candidate_id(candidat_raw, candidate_id)

    template_context = dict(name=candidate["name"], id=candidate["id"], skills=candidate["skills"])
    return render_template('card.html', **template_context)


@app.route('/skills/<skill>')
def skills(skill):
    candidat_raw = load_candidates_from_json('candidates.json')

    return format_candidates(get_candidates_skills(candidat_raw, skill))

# @app.route('/skills/<skill>')
# def skills(skill):
#     candidat_raw = get_candidates('candidates.json')
#
#     return format_candidates(get_candidates_skills(candidat_raw, skill))


@app.route('/search/<candidate_name>')
def candidate_search_name(candidate_name):
    candidat_raw = load_candidates_from_json('candidates.json')
    candidates = get_candidates_by_name(candidat_raw, candidate_name)

    return render_template('search.html', num=len(candidates), name=candidates)

@app.route('/search_skill/<skill>')
def candidate_search_skill(skill):
    candidat_raw = load_candidates_from_json('candidates.json')
    candidates = get_candidates_skills(candidat_raw, skill)

    return render_template('skill_py.html', num=len(candidates), skill=candidates)


app.run()
