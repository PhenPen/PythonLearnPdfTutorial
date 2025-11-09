"""  Exercise2:This program counts the distribution of the hour of the day for each of the messages.You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon character. Once you have accumulated the counts for each hour,print out the counts,one per line sorted by hour as shown below.
 python time of day.py
 Enter a filename: mbox-short.txt
 043
 061
 071
 092
 103
 116
 141
 152
 164
 172
 181
 191"""


from pathlib import Path

filePath = Path(r"learningDocs/mbox-short.txt")
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