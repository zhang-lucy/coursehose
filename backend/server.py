def get_major_prereqs(major):
	# idk????? smth to do w fireroad api?????
	# currently assuming this just returns a list of classes but unsure how to handle weird cases 
	# (and most things are weird cases)
	prereqs = []
	return prereqs

def get_minor_prereqs(minor):
	# ignore minors for now
	return []

def get_course_prereqs(course):
	# also sth to do with the fireroad api/our backend??
	# again will assume this just returns a nice list of prereqs even tho probably fake news
	prereqs = []
	return prereqs

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
