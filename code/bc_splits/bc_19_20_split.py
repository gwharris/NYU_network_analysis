"""
Graham Harris
Summer Data Project
Splits the entries in the 2021 BC applications into a person view.
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
  fd.write("Yes" + "\n")

# -------------- MAIN --------------

apps = csv_to_list("../../bootcamps/2019-2020/bootcamp_applications_2019_2020.csv")
fd = open("../../bootcamps/2019-2020/applications_20_person_view.csv", "w")
fd.write("What is your Team/Venture Name?,First,Last,Email,Net ID,School,NYU Status,Year in School,Expected Year of Graduation,Pronouns,Which of the following do you identify with? Select all that apply.,NYU Affiliated?\n")

for line in apps:
  # General items to everyone on team
  startup = line[0]
# Person 1
  for i in range(0, 11):
    fd.write(line[i] + ",")
  fd.write("Yes" + "\n")
  if line[11] == "I  am a solo founder":
    continue
  # Person 2 if NYU
  elif line[11] == "Yes":
    nyu_affiliated(fd, line, startup, 12, 22)
    if line[22] == "Nope! We're a team of 2.":
      continue
    # Person 3 if NYU
    elif line[22] == "Yes (and they are NYU affiliated)":
      nyu_affiliated(fd, line, startup, 30, 40)
    # Person 3 if NOT NYU
    elif line[22] == "Yes (but they are NOT NYU affiliated)":
      fd.write(startup + "," + line[41] + "," + line[42] + "," + line[43] + ",,,,,," + line[44] + "," + line[45] + ",No" + "\n")
  # Person 2 if NOT NYU
  elif line[11] == "No":
    fd.write(startup + "," + line[23] + "," + line[24] + "," + line[25] + ",,,,,," + line[26] + "," + line[27] + ",No" + "\n")
    if line[22] == "Nope! We're a team of 2.":
      continue
    # Person 3 if NYU
    elif line[22] == "Yes (and they are NYU affiliated)":
      nyu_affiliated(fd, line, startup, 30, 40)
    # Person 3 if NOT NYU
    elif line[22] == "Yes (but they are NOT NYU affiliated)":
      fd.write(startup + "," + line[41] + "," + line[42] + "," + line[43] + ",,,,,," + line[44] + "," + line[45] + ",No" + "\n")

fd.close()