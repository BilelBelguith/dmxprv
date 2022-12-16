import os

os.system("coverage run github_repo.py")
x = os.system("coverage report --fail-under=80 -m  *.py ")

if x == 0:
    print("coverage test is succeed ! ")
else:
    print("Sorry!")
