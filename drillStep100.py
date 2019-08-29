import os
import time

fPath = 'C:\\Drill File\\'

fList = os.listdir(fPath)
for i in fList:
    if i.endswith('.txt'):
        print(i + " was last modified " + time.strftime('%Y-%m-%dT%H:%M:%S', time.localtime(os.path.getmtime(os.path.join(fPath, i)))))
