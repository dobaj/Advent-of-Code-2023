import os, datetime
spaces = 4
today = datetime.date.today()
if today.month == 12:
    for i in range(1,today.day+1):
        # Transfer old days
        if os.path.exists(f"Day {i}"):
            os.mkdir(f"Day {i:02}")
            try:
                os.rename(f"Day {i}/input.txt",f"Day {i:02}/input.txt")
            except:
                print("No input file")
            os.rmdir(f"Day {i}")
        if not os.path.exists(f"Day {i:02}"):
            os.mkdir(f"Day {i:02}")
            file = open(f"Day {i:02}/day{i:02}.py","w")
            file.write(f'with open("Day {i:02}/input.txt") as f:\n'+' '*spaces)
            file.close()
            file = open(f"Day {i:02}/input.txt","w")
            file.close()
            break
    print("All folders/files up to date")