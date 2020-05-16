from flask import Flask, render_template, session, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/hi")
@app.route("/hi/")
def hindi():
    return render_template('home hindi.html')

@app.route("/team")
def team():
    return render_template('team.html')

@app.errorhandler(404) 
def not_found(e):
  return render_template("coming-soon.html") 


if __name__=='__main__':
    app.run()
