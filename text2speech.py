import gtts, time, os
import sqlite3 as sql

def insert(name, exp):
  try:
    conn = sql.connect("files.db")
    cur = conn.cursor()
    query = f"INSERT INTO files (name, expire) VALUES ('{name}', {exp})"
    
    cur.execute(query)
    print("inserted")
    conn.commit()
    cur.close()
  
  except sql.Error as e:
    print(e)
    return False
  finally:
    if conn:
      conn.close()

def convert(txt):
  #genrates a filename using current date and time
  filename = "Sun_tts_" + (str(time.time()).replace(".", "")) + ".mp3"
  
  tts = gtts.gTTS(txt)
  tts.save(f"audios/{filename}")
  
  exp = (int(time.time())) + 3600
  insert(filename, exp)
  
  return filename
  
def delete():
  try:
    conn = sql.connect("files.db")
    cur = conn.cursor()
    query = f"""
      SELECT * FROM files
    """
    
    cur.execute(query)
    results = cur.fetchall()
    cTime = int(time.time())
    
    for file in results:
      if file[1] < cTime:
        os.system(f"rm -rf audios/{file[0]}")
    
    cur.close()
  
  except sql.Error as e:
    print(e)
    return False
  finally:
    if conn:
      conn.close()