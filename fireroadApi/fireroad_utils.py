import requests
import json
import re


def get_course_requirements(course_id):
	link = "http://fireroad.mit.edu/requirements/get_json/" + course_id
	r = requests.get(link)
	j = r.json()["reqs"]
	return j


def get_all_course_requirements():
	major_reqs = {}
	major_id_link = "https://fireroad.mit.edu/requirements/list_reqs/"
	majors = requests.get(major_id_link).json()
	for major_id in majors:
		major_reqs[major_id] = get_course_requirements(major_id)
	return major_reqs


def get_all_major_titles():
	major_titles = []
	major_id_link = "https://fireroad.mit.edu/requirements/list_reqs/"
	majors = requests.get(major_id_link).json()
	for major_id, major_info in majors.items():
		if 'major' in major_id:
			major_titles.append(major_info['medium-title'].split()[0] + ': ' + major_info['title-no-degree'])
	major_titles.sort(key=major_sort_key)
	return major_titles

def major_sort_key(title):
	if title[0].isnumeric() and not title[1].isnumeric():
		return '0' + title.replace(":", " ")
	return title.replace(":", " ")

def save(data, file_name):
	with open(file_name, 'w') as f:
		json.dump(data, f)


if __name__ == "__main__":
	# course_id = input("Enter course id: ")
	# print(get_course_requirements(course_id))
	major_reqs = get_all_course_requirements()
	save(major_reqs, "../data/course_requirements.json")
	major_titles = get_all_major_titles()
	save(major_titles, "../data/major_titles.json")
