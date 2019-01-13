from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

from user import User

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/home/<username>")
def home(username=None):
    return render_template("home.html", name=username)

@app.route("/listen_music/<int:userid>")
def get_songs(userid):
    user = User()
    items = user.get_recommendations(userid)
    return jsonify(recommendations=items)


@app.route("/add_music", methods=['POST'])
def add_music():
    if request.method == "POST":
        json_dict = request.get_json()
        music_id = json_dict['id']
        music_title = json_dict['title']
        resp = jsonify(success=True)
        return resp

@app.route("/json/<int:value>", methods=['GET','POST'])
def test_jsonify(value):
    return jsonify(value=value)

if __name__ == '__main__':
    app.run(debug=True)
