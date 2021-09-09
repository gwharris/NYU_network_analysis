"""
Graham Harris
Summer Data Project
Compare the people who came to 1-2 coaching sessions to the people who came to 1-2 events.
"""

# -------------- METHODS --------------

# Converts CSV to a 2D/nested Python list structure.
def csv_to_list(path):
  fd = open(path, "r")
  fd.readline()
  rc = []
  for line in fd:
    line = line.split(",")
    rc.append(line)
  fd.close()
  return rc

# Compare whether someone attended events and coaching, or just one or the other
def compare_contrast(c, p):
  both = open("../analysis/coaching_and_eventbrite/both.csv", "w")
  only_coaching = open("../analysis/coaching_and_eventbrite/only_coaching.csv", "w")
  only_events = open("../analysis/coaching_and_eventbrite/only_events.csv", "w")
  for cline in c:
    printed_both = False
    for pline in p:
      # if the names are the same
      if pline[0].lower() == cline[0].lower():
        both.write(",".join(cline))
        printed_both = True
    if not printed_both:
      only_coaching.write(",".join(cline))
  # go the opposite way
  for pline in p:
    printed_both = False
    for cline in c:
      # if the names are the same again
      if pline[0].lower() == cline[0].lower():
        printed_both = True
    if not printed_both:
      only_events.write(",".join(pline))
  # close files
  both.close()
  only_coaching.close()
  only_events.close()

# -------------- MAIN --------------

coaching = csv_to_list("../coaching/data/people/all_people_under_2_apt.csv")
programs = csv_to_list("../eventbrite/data/low_events.csv")
compare_contrast(coaching, programs)