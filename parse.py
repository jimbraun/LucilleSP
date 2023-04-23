#!/usr/bin/env python

import re

INFILE = "data/sp.csv"
KEY = "Shaker Number"
PRINT_COLS = [KEY, "Box/Tub Number", "Theme", "2"]
PAT = ''',(?=(?:[^"]|"[^"]*")*$)'''


lines = []
with open(INFILE, mode="r") as f:
  lines = f.readlines()

if len(lines) == 0:
  raise Exception("Input is empty")

headings = re.split(PAT, lines[0])

for name in PRINT_COLS:
  if name not in headings:
    raise Exception("Headings missing entry %s" % name)

database = {}
no_number_database = {}
for i in range(1, len(lines)):
  entry = {}
  fields = re.split(PAT, lines[i])
  if len(fields) != len(headings):
    raise Exception("Dimension error on line %d: Expected "
                    "%d fields, got %d: %s" % (i, len(headings), len(fields), lines[i]))
  for j in range(len(headings)):
    entry[headings[j]] = fields[j]
  try:
    database[int(entry[KEY])] = entry
  except:
    entry[KEY] = entry[KEY].replace("\"", "")
    no_number_database[entry[KEY]] = entry

output_format = "%29s %4s %15s %s"

maxIndex = max(database.keys())
for i in range(1, (maxIndex + 1)):
  if i in database:
    print(output_format % tuple([database[i][x] for x in PRINT_COLS]))
for entry in no_number_database:
  print(output_format % tuple([no_number_database[entry][x] for x in PRINT_COLS]))
