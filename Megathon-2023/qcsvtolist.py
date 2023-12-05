import csv

with open("q_file.csv","r") as q:
    file= csv.reader(q)
    
    q_list = []
    count=0
    for rows in file:
        if(count==0):
            count+=1
            continue
        q_list.append(rows)
print(q_list)