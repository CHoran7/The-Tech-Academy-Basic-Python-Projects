import os

fPath = 'C:\\Drill File\\'

fList = os.listdir(fPath)
for i in fList:
    if i.endswith('.txt'):
        print(i + " was last modified " + str(os.path.getmtime(fPath)) + " seconds ago.")
        

