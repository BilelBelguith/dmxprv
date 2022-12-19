import os

os.system("coverage run github_repo.py")
x = os.system("coverage report --fail-under=80 -m  github_repo.py ")

if x == 0:
    print("coverage test is succeed ! ")
else:
    print("Sozdzdzdrry!")
