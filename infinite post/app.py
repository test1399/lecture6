from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")
	
@app.route("/posts", methods=["POST"])
def posts():
	start = int(request.form.get("start"))
	
	posts = []
	for i in range(start, start+40):
		posts.append("Post num#"+str(i))
	time.sleep(2)	
	return jsonify(posts)		