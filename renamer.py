import os, time
from datetime import datetime

paths_to_watch = []
names = []
a = []

def fill_paths():
    with open('.paths','r') as file:
        for line in file:
            keys = line.split(':')
            paths_to_watch.append(keys[0].strip())
            names.append(keys[1].strip())

def compare(i):
    after = dict ([(f, None) for f in os.listdir (paths_to_watch[i])])
    added = [f for f in after if not f in a[i]]
#   removed = [f for f in before if not f in after]
    if added:
    #   print("Added: ", ", ".join(added))
      date = datetime.now().strftime('-%m-%d-%Y')
      file = added[0].split('.')
      if len(file) > 1 and file[1] == "PDF" or file[1] == "pdf":
        os.rename(paths_to_watch[i] + '/' + added[0], paths_to_watch[i] + '/' + names[i] + date + '.' + file[1])
      else: print('not pdf or PDF')
    # if removed: print "Removed: ", ", ".join (removed)
    a[i] = after

fill_paths()

for i in range(0, len(paths_to_watch)):
    a.append(dict([(f, None) for f in os.listdir(paths_to_watch[i])]))

while 1:
  with open('.flag','r') as file:
    for line in file:
        if line == 'stop' or line == 'Stop':
            exit(0)

  time.sleep(5)
  
  for i in range(0, len(paths_to_watch)):
      compare(i)