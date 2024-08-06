from flask import Flask, request, flash, redirect, render_template, send_file

app = Flask(__name__)


@app.route("/")
def home():
  return render_template('index.html')

@app.route("/contact")
def contact():
  for k, v in request.args.items():
    print(k,v)
  return redirect("/")

@app.route("/image")
def image():
  return send_file("image.png")

if __name__ == "__main__":
    app.run()