from flask import Flask, request, render_template, send_file
import io, time
from gtts import gTTS as tts
from os import environ

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
  text = request.form.get("text")
  lang = (request.form.get("lang") or "en")
  
  buf = io.BytesIO()
  audio = tts(text=text, lang=lang)
  
  audio.write_to_fp(buf)
  buf.seek(0)
  
  return send_file(
    buf,
    as_attachment=True,
    download_name=f"Sun_tts_{str(time.time()).split('.')[0]}.mp3",
    mimetype="audio/mp3"
  )
  
  
app.run(host="0.0.0.0", port=int((environ.get("PORT") or 3000)), debug=False)