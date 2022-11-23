from flask import Flask,render_template
from searcher import searcher
app = Flask(__name__)
@app.route("/")
def main():
	return render_template("search.html")
@app.route("/<string:id>")
def result(id):
	query = id.replace("+"," ")
	result = searcher(query)
	return render_template("result.html",**locals())