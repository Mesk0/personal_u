import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)

with open(filename) as f_obj:
    nums = json.load(f_obj)

print(nums)

username = input("What is your name")
filename1 = "username.json"

with open(filename1,'w') as f1_obj:
    json.dump(username,f1_obj)
    print("we'll remember you when you come back, "+username+"!")

with open(filename1) as f2_obj:
    username = json.load(f2_obj)
    print("welcome back, "+username+"!")
