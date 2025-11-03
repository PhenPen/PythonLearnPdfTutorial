

from pathlib import Path
filePath = "learningDocs/mbox-short.txt"
count = 0

#Decorative Print Statements
print(f"{'*':*^50}")
print("Emails received from ")
print(f"{'*':*^50}")


with open(filePath,mode="r",encoding="utf-8") as f:
    for line in f:
        if line.startswith("From"):
            words = line.split()
            count += 1
            print(words[1])
print(f"{'*':*^50}") # Decorative Print Statement footer

print(f"You have {count} emails currently")