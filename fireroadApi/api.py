from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
# from flask_cors import CORS
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'qwertyuiop'
# app.config['CORS_HEADERS'] = 'Content-Type'

# cors = CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})

# # Flask app with basic template
# @app.route('/apiCall', methods=['POST'])
# @cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
# def get_road():
#   major = request.form['major']
#   year = request.form['year']

#   return {"Fall 2020": [{"name": "6.0001"}], "Spring 2021": [{"name": "6.0002"}]}

#   # desired form: list of 8 lists, e.g. [["6.006", "6.009"], ["a", "b"], ["c"] x 8 ]

# if __name__ == '__main__':
#    app.run(debug = True)

# # initialization
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
# app.config['CORS_HEADERS'] = 'Content-Type'

# cors = CORS(app, resources={r"/apiCall": {"origins": "http://localhost:8080"}})

# @app.route('/apiCall', methods=['POST'])
# @cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
# def get_road():
#   major = request.form['major']
#   year = request.form['year']

#   return {"Fall 2020": [{"name": "6.0001"}], "Spring 2021": [{"name": "6.0002"}]}

# if __name__ == '__main__':
#    app.run()

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
# app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)
# cors = CORS(app, resources={r"/apiCall": {"origins": "http://localhost:8080"}})

@app.route('/apiCall', methods=['POST'])
# @cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def get_road():
  print(request.form)
  major = request.form['major']
  year = request.form['year']

  data = {"Fall 2020": [{"name": "6.0001"}], "Spring 2021": [{"name": "6.0002"}]}
  response = jsonify(data)
  response.headers.add('Access-Control-Allow-Origin', '*')

  return response


if __name__ == '__main__':
   app.run()
