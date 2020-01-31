import os
import sys

data=sys.argv[1]
dirlist = [ dir for dir in os.listdir('.status') if data in dir ]
info = {'total':0}
def skimTotal(path,fname):
    if os.path.isdir('%s/%s' % (path,fname)):
        path = '%s/%s' % (path,fname)
        for file in os.listdir(path): skimTotal(path,file)
        return
    elif '.out' in fname:
        with open('%s/%s' % (path,fname)) as file:
            for line in file.readlines():
                if 'Processesing Events:' in line:
                    events = float(line.strip().replace('Processesing Events:',''))
                    info['total'] += events
for dir in dirlist: skimTotal('.status',dir)
print data,info['total']
