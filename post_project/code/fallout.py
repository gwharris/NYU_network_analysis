"""
Graham Harris
Summer Data Project
Copy of stats_copy.py from main project, except the program tracks the conversion/fallout rate between program to program.
"""

import sys

# -------------- METHODS --------------

def count_all(list1, list2, counter):
  for person in list1:
    if person in list2:
      counter += 1
  return counter

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

    # Create 2 empty list of events
    single_event = {line[1]:0 for line in lines_fixed}
    multiple_event = {line[1]:0 for line in lines_fixed}

    # Get num of edges per person and list of events
    all_attendees = {}
    for line in lines_fixed:
      if line[0] not in all_attendees:
        all_attendees[line[0]] = 1
      else:
        all_attendees[line[0]] += 1
  
    # Eliminate anyone with more than 1 edge
    # Only 1 edge means only 1 program attendance
    single_attendees = {k:v for k,v in all_attendees.items() if v == 1}
  
    htsas = []
    ff = []
    ss = []
    bc_app = []
    bc_att = []
    sp_app = []
    sp_att = []
    sl_app = []
    sl_att = []
    # Count individual instances
    for line in lines_fixed:
      if "htsas" in line[1]:
        htsas.append(line[0])
      elif "female" in line[1]:
        ff.append(line[0])
      elif "startup sch" in line[1]:
        ss.append(line[0])
      elif "bootcamp app" in line[1]:
        bc_app.append(line[0])
      elif "bootcamp part" in line[1]:
        bc_att.append(line[0])
      elif "sprint app" in line[1]:
        sp_app.append(line[0])
      elif "sprint part" in line[1]:
        sp_att.append(line[0])
      elif "slp app" in line[1]:
        sl_app.append(line[0])
      elif "slp part" in line[1]:
        sl_att.append(line[0])

    tof = htsas + ff + ss
    all_lists = [htsas, ff,     ss,     tof,    bc_app, bc_att, sp_app, sp_att, sl_app]
    list_org = [bc_app, bc_app, bc_app, bc_app, bc_att, sp_app, sp_att, sl_app, sl_att]

    # Count conversion
    htsas_to_bc = 0
    ss_to_bc = 0
    ff_to_bc = 0
    tof_to_bc = 0
    bc_app_to_att = 0
    bc_att_to_sp_app = 0
    sp_app_to_att = 0
    sp_att_to_slp_app = 0
    sl_app_to_att = 0
    all_nums = [htsas_to_bc, ss_to_bc, ff_to_bc, tof_to_bc, bc_app_to_att, bc_att_to_sp_app, sp_app_to_att, sp_att_to_slp_app, sl_app_to_att]
    descriptions = ["HTSAS to BC App",
          "FF to BC App",
          "SS to BC App",
          "All top-of-funnel to BC App",
          "BC App to BC Attendee",
          "BC Attendee to Sprint App",
          "Sprint App to Sprint Attendee",
          "Sprint Attendee to SLP App",
          "SLP App to SLP Attendee"]
    
    for i in range(0,9):
      if len(list_org[i]) != 0 and len(all_lists[i]) != 0:
        all_nums[i] = count_all(all_lists[i], list_org[i], all_nums[i])

    # Write numbers to file
    fd = open("../stats/" + arg + "_conversion.txt", "w")
    fd.write("Conversion rate between each program:\n")
    for i in range(0,9):
      if len(all_lists[i]) != 0:
        fd.write(descriptions[i] + ": " + str((all_nums[i]/len(all_lists[i])) *100) + "%\n")

    print("Success")

  except:
    print("\n\tFailure reading argument: " + arg)