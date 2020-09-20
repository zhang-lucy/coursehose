import json
import re
import ast

all_courses_file = "../vue-app/data/allCourses.json"
major_reqs_file = "../vue-app/data/course_requirements.json"


def read_data_files(all_courses_file, major_reqs_file):
    with open(all_courses_file, 'r') as f:
        all_courses = json.load(f)
    with open(major_reqs_file, 'r') as f:
        major_reqs = json.load(f)
    return all_courses, major_reqs


def parse_condition(condition, threshold=None):
    if 'req' in condition:
        if condition.get('plain-string', False):
            return []
        return [condition['req']]
    reqs = []
    if condition['connection-type'] == 'all':
        for subcondition in condition['reqs']:
            reqs.extend(parse_condition(subcondition))
        return reqs
    elif condition['connection-type'] == 'any':
        if condition['threshold-desc'] in ('select either', 'select any'):
            threshold = 1
        else:
            threshold = condition['threshold']['cutoff']
        for subcondition in condition['reqs']:
            if threshold == 0:
                break
            reqs.extend(parse_condition(subcondition))
            threshold -= 1
        return reqs



def get_major_reqs(major):
    """
    Give requirements for a major.
    :param major: major code, e.g. 'major18pm'
    :return: Requirements in an undetermined format?? {(course1, ... ): num_required}
    """
    # idk????? smth to do w fireroad api?????
    # currently assuming this just returns a list of classes but unsure how to handle weird cases
    # (and most things are weird cases)
    req_dict = major_reqs[major]
    reqs = []
    for condition in req_dict:
        reqs.extend(parse_condition(condition))
    return reqs


def get_course_prereqs(course):
    # also sth to do with the fireroad api/our backend??
    # again will assume this just returns a nice list of prereqs even tho probably fake news
    print(course)
    prereq_str = all_courses[course].get("prerequisites", "None")
    if prereq_str in ("None", "''Permission of instructor''"):
        return []
    prereq_str = re.sub("(\(.*\))/''permission of instructor''", lambda x: x.group(1)[1:-1], prereq_str)
    prereq_str = re.sub("/''permission of instructor''", "", prereq_str)
    GIR_courses = {"GIR:CAL1": "18.01", "GIR:CAL2": "(18.02, 18.022)", "GIR:PHY1": "(8.01, 8.01L, 8.012)",
                   "GIR:PHY2": "(8.02, 8.022)", "GIR:BIOL": "(7.012, 7.013, 7.014, 7.015, 7.016)",
                   "GIR:CHEM": "(3.091, 5.111, 5.112)"}
    for GIR in GIR_courses:
        prereq_str = prereq_str.replace(GIR, GIR_courses[GIR])
    prereq_str = re.sub("''Coreq: ([\w\.]*)''", lambda x: x.group(1), prereq_str)
    prereq_str = re.sub(" ", "", prereq_str)
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
    semesters = list(range(start_semester, end_semester+1))
    course_info = all_courses[course]
    if not course_info["offered_fall"]:
        semesters = [semester for semester in semesters if semester % 2 == 0]
        season = 1
    elif not course_info["offered_spring"]:
        semesters = [semester for semester in semesters if semester % 2 == 1]
        season = 2
    if "not-offered-year" in course_info:
        excluded_semester = 2 * (course_info["not-offered-year"].split()[0] - 2000) + season
        for i in range(excluded_semester, end_semester + 1, 2):
            if i in semesters:
                semesters.remove(i)

    return semesters


def find_next_offering(course, start_semester):
    current_season = start_semester % 2
    current_season = current_season + 2 if current_season == 0 else current_season
    course_info = all_courses[course]
    if course_info["offered_fall"] and course_info["offered_spring"]:
        return start_semester
    elif course_info["offered_fall"]:
        course_season = 1
    else:
        course_season = 2
    offered_semester = start_semester + (current_season != course_season)
    if "not-offered-year" in course_info:
        excluded_semester = 2 * (course_info["not-offered-year"].split()[0] - 2000) + course_season
        if offered_semester == excluded_semester:
            offered_semester += 2
    return offered_semester


def find_schedule(major, start_semester, end_semester = None, past_schedule = None, existing_schedule = None, cost_function = "classes"):
    # can prob just assume semesters are numbered as 2*(year - 2000) + (1 if fall) or sth
    # past_schedule is a dict from sem number to class we hardcode taking that sem
    # existing_schedule is a dict from sem number to class we want to hardcode taking that sem
    # start_semester is the "current" semester
    # for now let's just assume we minimize classes

    if end_semester is None:
        end_semester = start_semester + 7

    if past_schedule is None:
        past_schedule = {}

    if existing_schedule is None:
        existing_schedule = {}

    # TODO: comment the next few lines back in when we are not testing
    # all_reqs = get_reqs("GIRS")

    all_reqs = get_major_reqs(major)
    print(all_reqs)

    all_reqs.extend(["5.111", "7.012", "18.02", "8.02", "24.900", "24.917", "21M.301", "11.011", "21M.600", "14.01", "14.03", "21W.757"])

    new_reqs = list(set(all_reqs)) # idk but there's probably duplicates or sth???
    all_reqs = []

    prereqs = {} # maps course to a list of all its prereqs

    while (len(new_reqs) > 0):
        next_new_reqs = []
        # print(new_reqs, "help")
        for course in new_reqs:
            all_reqs.append(course)
            prereqs[course] = []
            course_prereqs = get_course_prereqs(course)
            # print("123", course_prereqs)
            for prereq in course_prereqs:
                while not type(prereq) == str:
                    prereq = prereq[0]
                    # print("zkdjhsdjflkd", prereq)
                # print("here", course, prereq)
                if prereq in past_schedule:
                    continue
                if not (prereq in all_reqs or prereq in next_new_reqs or prereq in new_reqs):
                    # all_reqs.append(prereq)
                    next_new_reqs.append(prereq)
                # print(course, prereqs[course])
                prereqs[course].append(prereq)
                # print(prereqs[course])
                # print("")
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

        # print("dskfjsdhfldksf", curr_level, next_level, levels[curr_level])

        for course in next_level:
            levels[curr_level].remove(course)

        # print("dskfjsdhfldksf", curr_level, next_level, levels[curr_level])

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

    no_prereqs = levels[0]
    for course in levels[0]:
        prereqs = get_course_prereqs(course)
        for prereq in prereqs:
            if prereq in no_prereqs:
                no_prereqs.remove(prereq)

    for course in levels[1]:
        prereqs = get_course_prereqs(course)
        for prereq in prereqs:
            if prereq in no_prereqs:
                no_prereqs.remove(prereq)

    for course in no_prereqs:
        levels[0].remove(course)

    print(no_prereqs)
    print(levels)

    for i in range(curr_level - 1, -1, -1):
        if (curr_semester > end_semester): 
            return -1
        # print("asjkshdj", i)
        level_courses = levels[i]
        # print("asjkshdj", level_courses)
        for course in level_courses:
            while len(ans[curr_semester]) >= 4:
                curr_semester += 1
                if (curr_semester > end_semester): 
                    return -1
            next_offering = find_next_offering(course, curr_semester)
            # print("here", ans[next_offering])
            ans[next_offering].append(course)
            # print(ans[next_offering])
        while len(no_prereqs) > 0 and len(ans[curr_semester]) < 4:
            course = no_prereqs[0]
            no_prereqs.remove(course)
            ans[curr_semester].append(course)
        curr_semester += 1

    return ans

if __name__ == "__main__":
    all_courses, major_reqs = read_data_files(all_courses_file, major_reqs_file)
    #print(find_schedule("major6-3", 0))
    print(find_schedule("major20", 41))
