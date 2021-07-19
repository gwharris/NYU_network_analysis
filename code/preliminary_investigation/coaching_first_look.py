"""
Graham Harris
Summer Data Project
A first look through the newly-organized coaching data.
"""

# -------------- METHODS --------------

# Converts CSV to a 2D/nested Python list structure.
def csv_to_list(path):
  fd = open(path, "r")
  fd.readline()
  rc = []
  for line in fd:
    line = line.split(",")
    if len(line) != 9:
      print(line, path)
    else:
      rc.append(line)
  fd.close()
  return rc

# Calculate the total amount of time spent coaching
def total_time(csv):
  counter = 0
  for i in csv:
    # Check if the meeting actually happened
    if i[5] != "Completed":
      continue
    # Strip hour or min
    if "min" in i[0]:
      i[0] = i[0].strip(" min")
      counter += int(i[0])
    elif "hr" in i[0]:
      i[0] = i[0].strip(" hr")
      counter += (60 * int(i[0]))
    else:
      try:
        counter += int(i[0])
      except:
        # Debug
        # print(item[0])
        pass
  return counter

# Get a list of all the items at the specified index, print to file
def list_at_index(csv, folder, newfile, index):
  fd = open("../coaching/data/" + folder + newfile + ".csv", "w")
  items = []
  for i in csv:
    if i[index] not in items:
      items.append(i[index])
  items.sort()
  for c in items:
    fd.write(c + "\n")
  fd.close()

# Similar to list_at_index, takes a tally of items at a specific index, prints to file
def tally(csv, index):
  dict = {}
  counter = 0
  for i in csv:
    if i[5] != "Completed":
      continue
    if i[index] not in dict:
      dict[i[index]] = 1
    else:
      dict[i[index]] += 1
    counter += 1
  dict["Total"] = counter
  return dict

# Add people and companies CSV in Affinity-readable format
def affinity(all_csvs, newfile):
  fd = open("../coaching/data/for_affinity/" + newfile + ".csv", "w")
  fd.write("Full Name,Email,Company\n")
  printed = []
  for csv in all_csvs:
    for i in csv:
      if i[1] not in printed:
        fd.write(i[1] + "," + i[2] + "," + i[6] + "\n")
        printed.append(i[1])
  fd.close()

# Creates a dictionary linking full names to emails
def find_emails(csv, fullname, email):
  rc = {}
  for line in csv:
    if line[fullname] not in rc:
      rc[line[fullname]] = line[email]
  return rc

# -------------- MAIN --------------

# Read in CSVs
csv_17_18 = csv_to_list("../coaching/csv/2017_2018_coaching.csv")
csv_18_19 = csv_to_list("../coaching/csv/2018_2019_coaching.csv")
csv_19_20 = csv_to_list("../coaching/csv/2019_2020_coaching.csv")
csv_20_21 = csv_to_list("../coaching/csv/2020_2021_coaching.csv")
csvs = [csv_17_18, csv_18_19, csv_19_20, csv_20_21] # list

# Macro Files
data = open("../coaching/data/data.csv", "w")

# Total time spent coaching
tot_time = 0
for c in csvs:
  t = total_time(c)
  tot_time += t
remainder = tot_time % 60
tot_hours = int((tot_time - remainder)/60)
data.write("Coaching: " + str(tot_time) + " minutes, ~" + str(tot_hours) + " hours\n\n")

# List companies from each year
comps = ["comp_17_18", "comp_18_19", "comp_19_20", "comp_20_21"]
for i in range(0, 4):
  list_at_index(csvs[i], "companies/", comps[i], 6)
# List emails from each year
emails = ["emails_17_18", "emails_18_19", "emails_19_20", "emails_20_21"]
for i in range(0, 4):
  list_at_index(csvs[i], "emails/", emails[i], 2)

# Tally purpose for coming
purposes = []
for c in csvs:
  purposes.append(tally(c, 3))
choices = [] # list of possible choices for purpose
# Make sure that every purpose is in every list
for p in purposes:
  for i in p.keys():
    if i not in choices:
      choices.append(i)
choices.pop(choices.index("Total"))
data.write("*Why do people come to coaching?*\nChoice,17-18,18-19,19-20,20-21\n")
for choice in choices:
  data.write(choice + ",")
  for i in range(0, 4):
    try:
      data.write(str(purposes[i][choice]))
    except:
      data.write(str(0))
    if i != 3:
      data.write(",")
  data.write("\n")
data.write("Totals:,")
for i in range(0, 4):
  data.write(str(purposes[i]["Total"]) + ",")
data.write("\n\n")

# People who only came once or twice
people = ["people_17_18", "people_18_19", "people_19_20", "people_20_21"]
for i in range(0, 4):
  dict = tally(csvs[i], 1)
  f = open("../coaching/data/people/" + people[i] + ".csv", "w")
  f.write("Full Name,# Attended,Coach\n")
  for person in sorted(dict.keys()):
    coaches = ""
    for line in csvs[i]:
      if person in line[1]:
        coaches = coaches + " " + line[4]
    if dict[person] <= 2:
      f.write(person + "," + str(dict[person]) + "," + coaches + "\n")
  f.close()

# ALL PEOPLE w EMAILS - DATA IS CLEANED
# People who only came once or twice
# a = open("../coaching_data/people/all_people_under_2_apt.csv", "w")
# a.write("Full Name,Email,Year,# Attended,Coach\n")
# acad_year = ["17-18", "18-19", "19-20", "20-21"]
# for i in range(0, 4):
#   dict = tally(csvs[i], 1)
#   email = find_emails(csvs[i], 1, 2)
#   for person in sorted(dict.keys()):
#     coaches = ""
#     for line in csvs[i]:
#       if person in line[1]:
#         coaches = coaches + " " + line[4]
#     if dict[person] <= 2:
#       a.write(person + "," + email[person] + "," + acad_year[i] + "," + str(dict[person]) + "," + coaches + "\n")


# Create Affinity-friendly CSV
affinity(csvs, "coaching_startups")

# close files
data.close()