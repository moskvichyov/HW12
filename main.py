from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open('settings.json') as f:
        settings = json.load(f)
    return render_template('index.html', **settings)


@app.route('/candidate/<id>')
def candidate(id):
    with open('candidates.json') as f:
        candidates = json.load(f)
        for candidate in candidates:
            if candidate['id'] == int(id):
                return render_template('candidate.html', **candidate)


@app.route('/list/')
def list():
    with open('candidates.json', "r", encoding="UTF-8") as f:
        candidates = json.load(f)
    return render_template('list.html', users = candidates)

@app.route('/search/')
def search():
    name = request.args.get('name')

    with open('candidates.json') as f:
        search = json.load(f)
    with open('settings.json') as f:
        settings = json.load(f)
    users = []
    if name:
        for candidate in search:
            if name.lower() in candidate['name']:
                users.append((candidate['id'], candidate['name']))

    return render_template('search.html', users=users, count_users = len(users))



#

@app.route('/skills/')
def search_skill():
    skill = request.args.get('skill')
    with open('candidates.json') as f:
        candidates = json.load(f)
    users = []

    for candidate in candidates:
        if skill in candidate['skills']:
            users.append((candidate['id'], candidate['name']))
    return render_template('skills.html', users=users, count_users = len(users))




if __name__ == '__main__':
    app.run(debug=True)