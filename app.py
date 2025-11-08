# placeholder server
print('server running')
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Prime360Protection-Kit server is running ✅"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


