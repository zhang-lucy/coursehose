from flask import Flask, render_template
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
import server

# Flask app with basic template
@app.route('/apiCall', methods=['GET', 'POST'])
def hello_world():
  # return {"Fall 2020": [{"name": "6.0001"}], "Spring 2021": [{"name": "6.0002"}]}
  curr_semester = 41
  schedule = server.find_schedule("major6-3", curr_semester)
  schedule_list = []
  for i in range(len(schedule)):
      schedule_list.append(schedule[i+curr_semester])

  # [["6.006", "6.009"], ["a", "b"], ["c"] x 8 ]

if __name__ == '__main__':
   app.run(debug = True)
