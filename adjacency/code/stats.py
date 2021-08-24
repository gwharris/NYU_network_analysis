"""
Graham Harris
Summer Data Project
Calculates numerical information about adjacency lists. Runs with command line arguments.
"""

import sys

# -------------- METHODS --------------

# Converts CSV to a 2D/nested Python list structure.
def csv_to_list(path):
  fd = open(path, "r")
  fd.readline() # get rid of title line
  rc = []
  for line in fd:
    line = line.lower() # make sure all casing is the same
    line = line.split(",")
    rc.append(line)
  fd.close()
  return rc

for arg in sys.argv:
  try:
    lines = csv_to_list("../data/" + arg + ".csv")
    print("\nFile found: " + arg)

    lines_fixed = []
    [lines_fixed.append(line) for line in lines if line not in lines_fixed] # eliminate duplicates

    # Create 2 empty list of events
    single_event = {line[1]:0 for line in lines_fixed}
    multiple_event = {line[1]:0 for line in lines_fixed}

    # Get num of edges per person and list of events
    all_attendees = {}
    for line in lines_fixed:
      if line[0] not in all_attendees:
        all_attendees[line[0]] = 1
      else:
        all_attendees[line[0]] += 1
  
    # Eliminate anyone with more than 1 edge
    # Only 1 edge means only 1 program attendance
    single_attendees = {k:v for k,v in all_attendees.items() if v == 1}
  
    # Counters
    for line in lines_fixed:
      if line[0] in single_attendees:
        single_event[line[1]] += 1
      multiple_event[line[1]] += 1

    # Write numbers to file
    fd = open("../stats/" + arg + ".txt", "w")
    for e in single_event:
      fd.write(e + ": " + str(single_event[e]) + " people (" + str((single_event[e]/multiple_event[e]) * 100) + "%)\n")

    print("Success")

  except:
    print("\n\tFailure reading argument: " + arg)