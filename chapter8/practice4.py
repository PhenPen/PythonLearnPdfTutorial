from pathlib import Path

# Replace interactive input with hardcoded values for mbox-short.txt
fileName = "mbox-short"  # Instead of input()
fileFormat = "txt"
filePath = Path(r"C:\Users\HP\Documents")  # Use raw string for Windows path

# Create directory if it doesn't exist
filePath.mkdir(parents=True, exist_ok=True)

newFilePath = filePath / f"{fileName}.{fileFormat}"

# Add error handling when opening file
try:
    with open(newFilePath, mode="r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("From:"):
                print(line.rstrip().upper())  # Use rstrip() to remove trailing whitespace
except FileNotFoundError:
    print(f"Error: Could not find file {newFilePath}")
    exit()
except Exception as e:
    print(f"Error: {e}")
    exit()