import os, time
from datetime import datetime

names = [
    "renamer",
    "scripts"
]
paths_to_watch = [
    "/Users/ryanharrington/Development/python-scripts/renamer",
    "/Users/ryanharrington/Development/python-scripts"
]
a = []

for i in range(0, len(paths_to_watch)):
    a.append(dict([(f, None) for f in os.listdir(paths_to_watch[i])]))

def compare(i):
    after = dict ([(f, None) for f in os.listdir (paths_to_watch[i])])
    added = [f for f in after if not f in a[i]]
#   removed = [f for f in before if not f in after]
    if added:
    #   print "Added: ", ", ".join(added)
      date = datetime.now().strftime('-%m-%d-%Y')
      file = added[0].split('.')
      if len(file) > 1 and file[1] == "PDF" or file[1] == "pdf":
        os.rename(paths_to_watch[i] + '/' + added[0], paths_to_watch[i] + '/' + names[i] + date + '.' + file[1])
      else: print('not pdf or PDF')
    # if removed: print "Removed: ", ", ".join (removed)
    a[i] = after

while 1:
  time.sleep(5)
  
  for i in range(0, len(paths_to_watch)):
      compare(i)