def gather_credits(creds, *args):
    target = creds
    cur_creds = 0
    fin_courses = {}

    for course in args:
        if target <= cur_creds:
            break

        if course[0] not in fin_courses:
            fin_courses[course[0]] = course[1]
            cur_creds += course[1]

    if target <= cur_creds:
        fin_courses = sorted(fin_courses.keys(), key=lambda x: x[0])
        return f"Enrollment finished! Maximum credits: {cur_creds}.\nCourses: {', '.join(fin_courses)}"
    else:
        return f"You need to enroll in more courses! You have to gather {target - cur_creds} credits more."


print(gather_credits(
    80,
    ("Basics", 27),
))

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))