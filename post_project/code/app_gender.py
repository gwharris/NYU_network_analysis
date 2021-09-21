"""
Graham Harris
Post Project Analysis
Find gender data for applications.
"""

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

def print_gender(gender, add_adj, f1, f2, f3):
  for line in add_adj:
    for a in f1:
      if line[0] == a[1]:
        gender.write(str(a).strip("[]") + ",2019\n")
    for b in f2:
      if line[0] == b[1]:
        gender.write(str(b).strip("[]") + ",2020\n")
    for c in f3:
      if line[0] == c[1]:
        gender.write(str(c).strip("[]") + ",2021\n")

# Bootcamp Apps
bc_2019 = csv_to_list("../../application_programs/bootcamps/applications_19_person_view.csv")
bc_2020 = csv_to_list("../../application_programs/bootcamps/applications_20_person_view.csv")
bc_2021 = csv_to_list("../../application_programs/bootcamps/applications_21_person_view.csv")
# JSprint
jsprint_2019 = csv_to_list("../../application_programs/jsprints/jsprint2019_apps.csv")
jsprint_2020 = csv_to_list("../../application_programs/jsprints/jsprint2020_apps.csv")
jsprint_2021 = csv_to_list("../../application_programs/jsprints/jsprint2021_apps.csv")
# Summer Sprint
summer_sprint_2019 = csv_to_list("../../application_programs/summer_accelerators/sprint/ssprint_applications_2019.csv")
summer_sprint_2020 = csv_to_list("../../application_programs/summer_accelerators/sprint/ssprint_applications_2020.csv")
summer_sprint_2021 = csv_to_list("../../application_programs/summer_accelerators/sprint/ssprint_applications_2021.csv")
# SLP
slp_2019 = csv_to_list("../../application_programs/summer_accelerators/SLP/slp_applications_2019.csv")
slp_2020 = csv_to_list("../../application_programs/summer_accelerators/SLP/slp_applications_2020.csv")
slp_2021 = csv_to_list("../../application_programs/summer_accelerators/SLP/slp_applications_2021.csv")

lines = csv_to_list("../data/added_adjacency_copy.csv")
add_adj = []
[add_adj.append(line) for line in lines if line not in add_adj] # eliminate

gender = open("../data/gender.csv", "w")

gender.write("Bootcamp:\n")
print_gender(gender, add_adj, bc_2019, bc_2020, bc_2021)
gender.write("\nJ Sprint:\n")
print_gender(gender, add_adj, jsprint_2019, jsprint_2020, jsprint_2021)
gender.write("\nSummer Sprint:\n")
print_gender(gender, add_adj, summer_sprint_2019, summer_sprint_2020, summer_sprint_2021)
gender.write("\nSLP:\n")
print_gender(gender, add_adj, slp_2019, slp_2019, slp_2021)

