import json
import re
import ast

all_courses_file = "../data/allCourses.json"
major_reqs_file = "../data/course_requirements.json"


def read_data_files(all_courses_file, major_reqs_file):
    with open(all_courses_file, 'r') as f:
        all_courses = json.load(f)
    with open(major_reqs_file, 'r') as f:
        major_reqs = json.load(f)
    return all_courses, major_reqs


def parse_condition(condition):
    if 'req' in condition:
        return condition['req']
    reqs = []
    if condition['connection-type'] == 'all':
        for subcondition in condition['reqs']:
            pass


def get_major_reqs(major):
    '''
    Give requirements for a major.
    :param major: major code, e.g. 'major18pm'
    :return: Requirements in an undetermined format?? {(course1, ... ): num_required}
    '''
    # idk????? smth to do w fireroad api?????
    # currently assuming this just returns a list of classes but unsure how to handle weird cases
    # (and most things are weird cases)
    reqs = {}
    req_dict = major_reqs[major]
    for condition in req_dict:
        pass

    return reqs


def get_minor_reqs(minor):
    # ignore minors for now
    return {}


def get_prereqs(course):
    # also sth to do with the fireroad api/our backend??
    # again will assume this just returns a nice list of prereqs even tho probably fake news
    prereq_str = all_courses[course]['pr']
    if prereq_str in ("None", "Permission of instructor"):
        return []
    GIR_courses = {"Calculus I (GIR)": "18.01", "Calculus II (GIR)": "18.02", "Physics I (GIR)": "8.01",
                   "Physics II (GIR)": "8.02", "Biology (GIR)": "(7.012, 7.013, 7.014, 7.015, or 7.016",
                   "Chemistry": "(3.091, 5.111, 5.112)"}
    for GIR in GIR_courses:
        prereq_str = prereq_str.replace(GIR, GIR_courses[GIR])
    prereq_str = prereq_str.replace(" or permission of instructor", "")
    prereq_str = re.sub("[\[\] ]", "", prereq_str)
    prereq_str = re.sub("and|or", ",", prereq_str)
    prereq_str = re.sub(",", ",,", prereq_str)
    prereq_str = "[" + prereq_str + "]"
    prereq_str = re.sub("([\[\]\(\),])([\w.]+)([\[\]\(\),])",
                        lambda x: x.group(1) + "'" + x.group(2) + "'" + x.group(3), prereq_str)
    prereq_str = re.sub(",,", ",", prereq_str)
    return ast.literal_eval(prereq_str)


def find_offerings(course, start_semester, end_semester):
    # returns a list of all semester numbers this class will be offered
    # again vaguely sketchy, this time bc mit can be sketchy abt this
    # but we will just assume for now that generally actual prereqs are not that sketchy
    semesters = []
    return semesters


def find_schedule(majors, minors, start_semester, end_semester = None, past_schedule = {}, existing_schedule = {}, cost_function = "classes"):
    # can prob just assume semesters are numbered as 2*(year - 2000) + (1 if fall) or sth
    # past_schedule is a dict from sem number to class we hardcode taking that sem
    # existing_schedule is a dict from sem number to class we want to hardcode taking that sem
    # start_semester is the "current" semester

    if end_semester == None:
        end_semester = start_semester + 7

    all_reqs = get_reqs("GIRS") #or sth girs hardcoded rn but maybe figure better out later

    for m in majors:
        all_reqs.append(get_major_reqs(major))

    for m in minors:
        all_reqs.append(get_major_reqs(major))

    all_reqs = list(set(all_reqs)) # idk but there's probably duplicates or sth???

    prereqs = {}
    for course in all_reqs:
        course_prereqs = get_course_prereqs(course)
        for c in course_prereqs:
            if c in past_schedule:
                continue
            if not c in all_reqs:
                all_reqs.append(c)
            prereqs.add((c, course))

    low = 0
    high = 1000
    currMidSchedule = None

    while (high - low > 1):
        # binary search, maybe refactor later to pass to other fn
        mid = (low + high) / 2
        if ()

if __name__ == "__main__":
    all_courses, major_reqs = read_data_files(all_courses_file, major_reqs_file)
    print(get_prereqs("9.016"))
