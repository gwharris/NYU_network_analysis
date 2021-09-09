"""
Graham Harris
Summer Data Project
Data from Eventbrite events dating back to Fall 2017.
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

# Create a list of unique entries in a column
def column(csv, index):
  rc = []
  for line in csv:
    if line[index] not in rc:
      rc.append(line[index])
  return rc
  
# Same as column(), used mostly for getting full name
# Event, first, and last are indexes
def attendance(csv, event, first, last):
  rc = {}
  for line in csv:
    fullname = line[first] + " " + line[last]
    fullname = re.sub(r'[^a-zA-Z ]', '', fullname)
    if fullname not in rc:
      rc[fullname] = []
    rc[fullname].append(line[event])
  return rc

# Creates a dictionary linking full names to emails
def emails(csv, first, last, email):
  rc = {}
  for line in csv:
    fullname = line[first] + " " + line[last]
    fullname = re.sub(r'[^a-zA-Z ]', '', fullname)
    if fullname not in rc:
      rc[fullname] = line[email]
  return rc

# -------------- MAIN --------------

eventbrite = csv_to_list("../eventbrite/all_events_2017_2021.csv")
events = column(eventbrite, 0)
att = attendance(eventbrite, 0, 4, 5)
name_emails = emails(eventbrite, 4, 5, 6)

# DATA IS CLEANED - DO NOT UNCOMMENT
# Write people to file
fd = open("../eventbrite/data/low_event_attendance.csv", "w")
fd.write("Full Name,Email,# Event Attended,Event Names\n")
for i in att.keys():
  print_events = ""
  if len(att[i]) == 1:
    print_events = att[i][0]
  elif len(att[i]) == 2:
    print_events= att[i][0] + "/" + att[i][1]
  if len(att[i]) <= 2:
    fd.write(i + "," + name_emails[i] + "," + str(len(att[i])) + "," + print_events + "\n")

  



