import os
# path = "D:/wonder/temp"
path = "D:/wonder/HackerRank"
os.chdir(path)

import random
n = random.randint(3,10)

for i in range(0,n):
    os.system("git commit -m 'commit' --allow-empty")
    os.system('git commit --amend --date="2022-01-27 12:12:45" -m "commit message" --allow-empty')
    print("done commits")

os.system("git push origin main")
print("pushing")


# git commit --amend --date="Sat Dec 25 10:06:28 2021 +0530"
# name 
# esc :wq
