"""
Graham Harris
Summer Data Project
Edited version of stats.py that calculates the amount of people who participate in programs across academic years. Only designed for the all-year adjacency files
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

    # Get num of edges per person and list of events
    all_attendees = {}
    for line in lines_fixed:
      if line[0] not in all_attendees:
        all_attendees[line[0]] = []
      all_attendees[line[0]].append(line[1])

    # Eliminate anyone with ONLY  1 edge
    # Only 1 edge means only 1 program attendance
    mult_events = {k:v for k,v in all_attendees.items() if len(v) > 1}
  
    from19to20 = 0
    from20to21 = 0
    total2019 = 0
    total2020 = 0
    total2021 = 0
    for v in mult_events.values():
      # print(v) debug
      in2019 = 0
      in2020 = 0
      in2021 = 0
      for event in v:
        if "2019" in event:
          in2019 = 1
          total2019 += 1
        elif "2020" in event:
          in2020 = 1
          total2020 += 1
        elif "2021" in event:
          in2021 = 1
          total2021 += 1
      if in2019 == 1 and in2020 == 1:
        from19to20 += 1
      if in2020 == 1 and in2021 == 1:
        from20to21 += 1

    # Write numbers to file
    fd = open("../stats/followthrough_" + arg + ".txt", "w")
    fd.write("2019 to 2020: " + str(from19to20) + " (" + str((from19to20/total2019) * 100) + "%)\n")
    fd.write("2020 to 2021: " + str(from20to21) + " (" + str((from20to21/total2020) * 100) + "%)\n")

    print("Success")

  except:
    print("\n\tFailure reading argument: " + arg)