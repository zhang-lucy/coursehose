import requests
import json

def get_course_requirements(course_id):
	link = "http://fireroad-dev.mit.edu/requirements/progress/" + course_id
	r = requests.get(link)
	j = r.json()["reqs"]
	return j

course_id = input()
print(get_course_requirements(course_id))
