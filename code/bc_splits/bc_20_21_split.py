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

def nyu_affiliated(fd, line, startup, gen, num1, num2):
  fd.write(startup + "," + line[num1] + " " + line[num1 + 1] + ",")
  for i in range(num1, num2):
    fd.write(line[i] + ",")
  fd.write("Yes," + gen + "\n")

# -------------- MAIN --------------

apps = csv_to_list("../events/bootcamps/2020-2021/applications_2020_2021.csv")
fd = open("../events/bootcamps/applications_21_person_view.csv", "w")
fd.write("What is your Team/Venture Name?,Full Name,First,Last,Email,Net ID,School,NYU Status,Year in School,Expected Year of Graduation,Pronouns,Which of the following do you identify with? Select all that apply.,NYU Affiliated?,Is one of the founders First Gen?\n")

for line in apps:
  # General items to everyone on team
  startup = line[0]
  try:
    gen = line[55].strip("\n")
  except:
    print(startup + " is unable to be processed.")
# Person 1
  for i in range(0, 12):
    fd.write(line[i] + ",")
  fd.write("Yes," + gen + "\n")
  if line[12] == "I  am a solo founder":
    continue
  # Person 2 if NYU
  elif line[12] == "Yes":
    nyu_affiliated(fd, line, startup, gen, 13, 23)
    if line[23] == "Nope! We're a team of 2.":
      continue
    # Person 3 if NYU
    elif line[23] == "Yes (and they are NYU affiliated)":
      nyu_affiliated(fd, line, startup, gen, 31, 41)
    # Person 3 if NOT NYU
    elif line[23] == "Yes (but they are NOT NYU affiliated)":
      fd.write(startup + "," + line[42] + " " + line[43] + "," + line[42] + "," + line[43] + "," + line[44] + ",,,,,," + line[45] + "," + line[46] + ",No," + gen + "\n")
  # Person 2 if NOT NYU
  elif line[12] == "No":
    fd.write(startup + "," + line[24] + " " + line[25] + "," + line[24] + "," + line[25] + "," + line[26] + ",,,,,," + line[27] + "," + line[28] + ",No," + gen + "\n")
    if line[23] == "Nope! We're a team of 2.":
      continue
    # Person 3 if NYU
    elif line[23] == "Yes (and they are NYU affiliated)":
      nyu_affiliated(fd, line, startup, gen, 31, 41)
    # Person 3 if NOT NYU
    elif line[23] == "Yes (but they are NOT NYU affiliated)":
      fd.write(startup + "," + line[42] + " " + line[43] + "," + line[42] + "," + line[43] + "," + line[44] + ",,,,,," + line[45] + "," + line[46] + ",No," + gen + "\n")

fd.close()