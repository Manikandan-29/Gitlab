from flask import Flask
import os
app = Flask(__name__)
@app.route("/")
def skill() :
  
    message="{name} is a gitlab pro "
    return message.format(name=os.getenv("NAME", "MANI"))
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8000)