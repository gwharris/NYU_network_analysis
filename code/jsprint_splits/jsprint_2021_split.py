"""
Graham Harris
Summer Data Project
Splits the entries in the 2021 JSprint application into Female Founders Fellows, First Gen Fellows, and applicants for the sprint.
"""

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

def print_range(file, line, num1, num2):
  file.write(line[0] + "," + line[1] + ",")
  for i in range(num1, num2):
    file.write(line[i] + ",")
  file.write("\n")

# -------------- MAIN --------------

apps = csv_to_list("../../jsprints/2021/2021_all3_apps.csv")
ff = open("../../jsprints/2021/female_founders_fellow_apps.csv", "w")
gg = open("../../jsprints/2021/first_gen_fellow_apps.csv", "w")
ss = open("../../jsprints/2021/jsprint_2021_apps.csv", "w")
ff.write("Which program are you applying for?,Team/Venture Name,First Name,Last Name,Email (ENTER AN NYU; NYU STERN; or NYU LANGONE EMAIL ADDRESS ONLY),NYU Affiliation,NYU Net ID (ex. jcc23),NYU School/College - Selected Choice,Expected Graduation Year (If graduated 1+ year ago; please indicate graduating year in 'other'),Pronoun(s),If you identify with an under-represented population in STEM; please describe.\n")
gg.write("Which program are you applying for?,Team/Venture Name,First Name,Last Name,Email (ENTER AN NYU; NYU STERN; or NYU LANGONE EMAIL ADDRESS ONLY),NYU Affiliation,NYU Net ID (ex. jcc23),NYU School/College - Selected Choice,Expected Graduation Year (If graduated 1+ year ago; please indicate graduating year in 'other'),Pronoun(s),If you identify with an under-represented population in STEM; please describe.\n")
ss.write("Which program are you applying for?,Team/Venture Name,First Name,Last Name,Email (ENTER AN NYU; NYU STERN; or NYU LANGONE EMAIL ADDRESS ONLY),NYU Affiliation,NYU Net ID (ex. jcc23),NYU School/College - Selected Choice,Expected Graduation Year (If graduated 1+ year ago; please indicate graduating year in 'other'),Pronoun(s),If you identify with an under-represented population in STEM; please describe.\n")

for line in apps:
  # Assign to a file
  files = []
  if "NYU J-Term Startup Sprint 2021" in line[0]:
    files.append(ss)
  if "NYU Female Founders Fellowship - Spring 2021" in line[0]:
    files.append(ff)
  if "NYU First Generation to College" in line[0]:
    files.append(gg)
  for file in files:
    print_range(file, line, 2, 11)
    if line[11] == "Yes":
      print_range(file, line, 12, 21)
    if line[21] == "Yes":
      print_range(file, line, 22, 31)
    if line[31] == "Yes":
      print_range(file, line, 32, 41)
  
ff.close()
gg.close()
ss.close()