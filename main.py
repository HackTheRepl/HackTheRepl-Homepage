from flask import Flask, render_template
app = Flask('app')

@app.route('/')
def index():
  return "placeholder for now."

app.run(host='0.0.0.0', port=8080)
