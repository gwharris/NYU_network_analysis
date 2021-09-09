"""
Graham Harris
Summer Data Project
Splits the entries in the 2018-2019 BC applications into a person view.
"""

import re # Import Regex for string cleaning

# -------------- METHODS --------------

# Converts CSV to a 2D/nested Python list structure.
def csv_to_list(path):
  fd = open(path, "r")
  fd.readline() # get rid of title line
  rc = []
  for line in fd:
    line = line.split(",")
    rc.append(line)
  fd.close()
  return rc

def nyu_affiliated(fd, line, startup, num1, num2):
  fd.write(startup + ",")
  for i in range(num1, num2):
    fd.write(line[i] + ",")
  fd.write("Yes\n")

# -------------- MAIN --------------

apps = csv_to_list("../events/bootcamps/2018-2019/bc_2018_2019_raw.csv")
fd = open("../events/bootcamps/2018-2019/applications_18-19_person_view.csv", "w")
fd.write("What is your Team/Venture Name?,Full Name,Email,Net ID,School,NYU Status,Expected Year of Graduation,NYU Affiliated?\n")

for line in apps:
  # General items to everyone on team
  startup = line[0]
# Person 1
  for i in range(0, 7):
    fd.write(line[i] + ",")
  fd.write("Yes\n")
  if line[7] == "I  am a solo founder":
    continue
  # Person 2 if NYU
  elif line[7] == "Yes":
    nyu_affiliated(fd, line, startup, 8, 14)
    if line[14] == "Nope! We're a team of 2.":
      continue
    # Person 3 if NYU
    elif line[14] == "Yes (and they are NYU affiliated)":
      nyu_affiliated(fd, line, startup, 19, 25)
    # Person 3 if NOT NYU
    elif line[14] == "Yes (but they are NOT NYU affiliated)":
      fd.write(startup + "," + line[26] + "," + line[27] + ",,,,,No\n")
  # Person 2 if NOT NYU
  elif line[7] == "No":
    fd.write(startup + "," + line[15] + "," + line[16] + ",,,,,No\n")
    if line[18] == "Nope! We're a team of 2.":
      continue
    # Person 3 if NYU
    elif line[18] == "Yes (and they are NYU affiliated)":
      nyu_affiliated(fd, line, startup, 19, 25)
    # Person 3 if NOT NYU
    elif line[18] == "Yes (but they are NOT NYU affiliated)":
      fd.write(startup + "," + line[26] + "," + line[27] + ",,,,,No\n")

fd.close()