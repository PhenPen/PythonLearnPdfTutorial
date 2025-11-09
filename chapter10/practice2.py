""" Making exercise 1 of chapter 10 a function"""

def email_MaxCount(filePath):
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
                addr = line[1]

                d[addr] = d.get(addr,0) + 1
            # print(d) #For debugging
            for email,count in d.items():
                lst.append((count,email))
            lst.sort(reverse=True)
            maxCount,Email = lst[0]
            print(Email,maxCount)
    except FileNotFoundError:
        print("File not found")


email_MaxCount("learningDocs/mbox-short.txt")