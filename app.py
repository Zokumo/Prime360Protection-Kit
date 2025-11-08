# placeholder server
print('server running')
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Prime360Protection-Kit server is running ✅"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)


