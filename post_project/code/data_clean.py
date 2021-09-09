"""
Graham Harris
Post Project Analysis
Further cleans the data from over the summer by removing duplicates and all coaching data.
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
    lines = csv_to_list("../../adjacency/data/" + arg + ".csv")
    print("\nFile found: " + arg)

    lines_fixed = []
    [lines_fixed.append(line) for line in lines if line not in lines_fixed and "coaching" not in line[1]] # eliminate duplicates

    fd = open("../data/" + arg + ".csv", "w")
    fd.write("Source,Target,Weight\n")
    for line in lines_fixed:
      fd.write(line[0].title() + "," + line[1].title() + "," + line[2])

    print("Success")

  except:
    print("\n\tFailure reading argument: " + arg)