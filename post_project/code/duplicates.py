"""
Graham Harris
Post Project Analysis
Remove any duplicates that may have escaped.
"""

import sys

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
    lines = csv_to_list("../data/gender/" + arg + ".csv")
    clean = []
    [clean.append(line) for line in lines if line not in clean] # eliminate duplicates

    first = []
    last = []
    clean_final = []
    for line in clean:
      if line[1] in first and line[2] in last:
        pass
      else:
        clean_final.append(line)
        first.append(line[1])
        last.append(line[2])

    f = open("../data/gender_clean/" + arg + ".csv", "w")
    f.write("Teams:\n")
    for line in clean_final:
      f.write(str(line) + "\n")

    print(arg + " success\n")

  except:
    print(arg + " error\n")