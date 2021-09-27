import csv
import pandas as pd
from collections import Counter
with open("SOCR-HeightWeight.csv",newline="") as f:
    reader=csv.reader(f) 
    filedata=list(reader)

filedata.pop(0)
newdata=[]
for i in range(len(filedata)):
    num=filedata[i][1]
    newdata.append(float(num))

n=len(newdata)
data=Counter(newdata)
modedataforrange={
    "50-60":0,
    "60-70":0,
    "70-80":0
}
for height,occurance in data.items():
    if 50 < float(height)<60:
        modedataforrange["50-60"]+=occurance

    elif 60 < float(height)<70:
        modedataforrange["60-70"]+=occurance

    elif 70 < float(height)<80:
        modedataforrange["70-80"]+=occurance
    
moderange,modeoccurance=0,0
for range,occurance in modedataforrange.items():
    if occurance>modeoccurance:
        moderange,modeoccurance=[int(range.split("-")[0]),int(range.split("-")[1])],occurance

mode=float((moderange[0]+moderange[1])/2)
print(mode)