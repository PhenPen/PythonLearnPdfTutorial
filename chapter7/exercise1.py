from pathlib import Path

fileName = input("Enter file name: ")
fileFormat = input("Enter file format: ")
filePath = Path(input("Enter file path: "))

filePath.parent.mkdir(parents=True,exist_ok=True)

newFilePath = Path(filePath)/f"{fileName}.{fileFormat}"


#file = C:\Coding\Projects\VsCode\tutsPhen\pdfTuts\pythonLearnpdf\chapter7\test.txt
#file2 = "C:\Users\HP\Documents\Wallchain_Klout_idOS_Wallchain.txt"
#file_path3 = C:\Users\HP\Documents
#fileName3 = mbox-short


#try:f = open(newFilePath,mode= "r", encoding = "utf-8")
#except FileNotFoundError: print("File not found"),exit()
#else: f.read(),f.close()


with open(newFilePath, mode="r", encoding="utf-8") as f :
    for line in f:
        print(line.upper().rstrip())



#Try:  Catch Exception as e: Print(f”Error thrown: {e}”)