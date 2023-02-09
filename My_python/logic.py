pad = 'Apple'
print(pad == 'apple')
print(pad == 'huawei')

print(pad.lower() != 'apple')
print(pad)

if pad != 'huawei':
    print(pad)

age=22
print(age==21)

age_1=22
age_2=24
print(age_1>=11 and age_2<=12)
print(age_1>=11 or age_2<=12)

province=['hunan','shanxi','hubei','hebei']
print('beijing' in province)
print('hunan' in province)
site1='california'
if site1 not in province:
    print(site1+"is not a province of china")
else:
    print(site1+"is a province of china")

Age=22
if age<4:
    price=0
elif age<18:
    price=4
elif age>=18:
    price=10
print("your admission cost is $"+str(price)+".")

barcelona=['messi','xavi','neymar jr','suarez','rakitic']
for barca in barcelona:
    if barca=="xavi":
        print(barca+" is retired.")
    else:
        print(barca+" is a starter.")
print("this is barcalona's starter list.")

requested_toppings=[]
if requested_toppings:
    for requested_topping in requested_toppings:
        print("adding"+requested_topping+".")
    print("\nfinished making your pizza")
else:
    print("Are you sure you want a plain pizza")


avaliable_toppings=['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings=['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in avaliable_toppings:
        print("Adding "+requested_topping+".")
    else:
        print("Sorry,we don't have "+requested_topping+".")
print("\nFinished making your pizza")

Age = 1
Age == 2
