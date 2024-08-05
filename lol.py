from flask import Flask, request, flash, redirect, render_template

app = Flask(__name__)

@app.route("/")
def home():
  return render_template('index.html')

@app.route("/contact")
def tes():
  for k, v in request.args.items():
    print(k,v)
  return redirect("/")