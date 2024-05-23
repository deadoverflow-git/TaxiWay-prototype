from flask import Flask, send_file, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('test.html')

app.run(port=80)