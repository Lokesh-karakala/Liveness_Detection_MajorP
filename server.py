from flask import Flask, render_template
import subprocess
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/project/')
def my_link():
  subprocess.Popen("python livelines_net.py 1", shell=True) 

  return 'Loading....'

if __name__ == '__main__':
  app.run(debug=True)