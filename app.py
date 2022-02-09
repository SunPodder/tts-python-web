from flask import Flask, redirect, url_for, request, render_template, send_file

import text2speech as tts

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/download", methods=["POST"])
def download():
  text = request.form['text']
  name = tts.convert(text)
  tts.delete()

  #return redirect(f"/download?name={name}")
  return send_file(f"audios/{name}", as_attachment=True)
  

app.run(host='0.0.0.0', port=3000)