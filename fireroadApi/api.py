from flask import Flask, render_template
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

# Flask app with basic template
@app.route('/apiCall', methods=['GET', 'POST'])
def hello_world():
  return {"Fall 2020": [{"name": "6.0001"}], "Spring 2021": [{"name": "6.0002"}]}

  # [["6.006", "6.009"], ["a", "b"], ["c"] x 8 ]

if __name__ == '__main__':
   app.run(debug = True)
