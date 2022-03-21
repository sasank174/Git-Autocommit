import os

# path = "D:/wonder/HackerRank"

f = open("loc.txt", "r")
path = f.readline()

os.chdir(path)

os.system("git add . && git commit -m commit")
print("done commits")

os.system("git push origin main")
print("pushing")
os.system("exit")