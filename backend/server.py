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
            reqs.append(parse_condition(subcondition))
        return (reqs, len(condition['reqs']),)
    elif condition['connection-type'] == 'any':
        pass



def get_major_reqs(major):
    """
    Give requirements for a major.
    :param major: major code, e.g. 'major18pm'
    :return: Requirements in an undetermined format?? {(course1, ... ): num_required}
    """
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


def get_course_prereqs(course):
    # also sth to do with the fireroad api/our backend??
    # again will assume this just returns a nice list of prereqs even tho probably fake news
    prereq_str = all_courses[course].get("prerequisites", "None")
    if prereq_str in ("None", "''Permission of instructor''"):
        return []
    GIR_courses = {"GIR:CAL1": "18.01", "GIR:CAL2": "(18.02, 18.022)", "GIR:PHY1": "(8.01, 8.01L, 8.012)",
                   "GIR:PHY2": "(8.02, 8.022)", "GIR:BIO": "(7.012, 7.013, 7.014, 7.015, or 7.016)",
                   "GIR:CHEM": "(3.091, 5.111, 5.112)"}
    for GIR in GIR_courses:
        prereq_str = prereq_str.replace(GIR, GIR_courses[GIR])
    prereq_str = re.sub("(.*)/''permission of instructor''", lambda x: x.group(1)[1:-1], prereq_str)
    prereq_str = re.sub("[\[\] ]", "", prereq_str)
    prereq_str = re.sub("/", ",", prereq_str)
    prereq_str = re.sub(",", ",,", prereq_str)
    prereq_str = "[" + prereq_str + "]"
    prereq_str = re.sub("([\[\]\(\),])([\w\.]+)([\[\]\(\),])",
                        lambda x: x.group(1) + "'" + x.group(2) + "'" + x.group(3), prereq_str)
    prereq_str = re.sub(",,", ",", prereq_str)
    return ast.literal_eval(prereq_str)


def find_offerings(course, start_semester, end_semester):
    # returns a list of all semester numbers this class will be offered
    # again vaguely sketchy, this time bc mit can be sketchy abt this
    # but we will just assume for now that generally actual prereqs are not that sketchy
    semesters = []
    course_info = all_courses[course]
    if course_info['nx'] == "false":
        semesters = [start_semester, start_semester+2]
    return semesters

def find_next_offering(course, start_semester):
    return start_semester

def find_schedule(majors, minors, start_semester, end_semester = None, past_schedule = {}, existing_schedule = {}, cost_function = "classes"):
    # can prob just assume semesters are numbered as 2*(year - 2000) + (1 if fall) or sth
    # past_schedule is a dict from sem number to class we hardcode taking that sem
    # existing_schedule is a dict from sem number to class we want to hardcode taking that sem
    # start_semester is the "current" semester
    # for now let's just assume we minimize classes

    if end_semester == None:
        end_semester = start_semester + 7

    # TODO: comment the next few lines back in when we are not testing
    # all_reqs = get_reqs("GIRS")

    # for m in majors:
    #     all_reqs.append(get_major_reqs(major))

    # for m in minors:
    #     all_reqs.append(get_major_reqs(major))

    all_reqs = ["6.046", "6.852", "6.031"]

    new_reqs = list(set(all_reqs)) # idk but there's probably duplicates or sth???
    all_reqs = []

    prereqs = {} # maps course to a list of all its prereqs

    while (len(new_reqs) > 0):
        next_new_reqs = []
        print(new_reqs, "help")
        for course in new_reqs:
            all_reqs.append(course)
            prereqs[course] = []
            course_prereqs = get_course_prereqs(course)
            print("123", course_prereqs)
            for prereq in course_prereqs:
                print("here", course, prereq)
                if prereq in past_schedule:
                    continue
                if not (prereq in all_reqs or prereq in new_reqs):
                    next_new_reqs.append(prereq)
                print(course, prereqs[course])
                prereqs[course].append(prereq)
                print(prereqs[course])
                print("")
        new_reqs = next_new_reqs

    levels = []
    levels.append(all_reqs)

    curr_level = 0

    while len(levels[curr_level]) > 0:
        curr_level_courses = levels[curr_level]
        next_level = []

        for course in curr_level_courses:
            for prereq in prereqs[course]:
                if not prereq in next_level:
                    next_level.append(prereq)

        levels.append(next_level)

        for course in next_level:
            levels[curr_level].remove(course)

        curr_level += 1

    level_lookup = {}
    for level in levels:
        for course in level:
            level_lookup[course] = level

    ans = {}

    for i in range(start_semester, end_semester + 1):
        ans[i] = []

    # added = []

    # assume existing_schedule is sorted, btw idk how to sort a dictionary but can add code later
    # also assume that none of these are terrible or sth
    # for sem in existing_schedule:
    #     sem_courses = existing_schedule[sem]
    #     for course in sem_courses:
    #         ans[sem].append(course)
    #         course_prereqs = get_course_prereqs(course)
    #         for prereq in course_prereqs:

    # temporarily assume four classes a semester, later can "binary search" or sth
    curr_semester = start_semester

    for i in range(curr_level - 1, -1, -1):
        level_courses = levels[i]
        for course in level_courses:
            if len(ans[curr_semester]) >= 4:
                curr_semester += 1
            next_offering = find_next_offering(course)
            ans[next_offering].append(course)

    return ans

if __name__ == "__main__":
    all_courses, major_reqs = read_data_files(all_courses_file, major_reqs_file)
    print(find_schedule(0, 0, 0, 0))
>>>>>>> 0d909f07bb33e34cd185854dd0e07ff8334884d8
