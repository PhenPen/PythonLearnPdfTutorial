""" Converting Chapter 10, Exercise 2 to a function"""

def time_Count(filePath):
    from pathlib import Path

    d = dict()
    lst = list()

    try:
        with open(filePath,"r",encoding = "utf-8") as file:
            for line in file:
                line = line.strip()
                if not line.startswith("From") : continue
                if line.startswith("From:") : continue
                # print(line) #For debugging
                line = line.split()
                time = line[5]
                hour,mins,secs = time.split(":")

                d[hour] = d.get(hour,0) + 1
            # print(d) #For debugging
            for hour,count in d.items():
                lst.append((hour,count))
            lst.sort()
            for hour,count in lst:
                print(hour,count)
    except FileNotFoundError:
        print("File not found")
        

time_Count("learningDocs/mbox-short.txt")