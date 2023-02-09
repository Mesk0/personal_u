alien_0 = {'color':'green','point':5}
print(alien_0['color'])
new_point=alien_0['point']
print(new_point)
# 增加键-值对
alien_0['x_position'] = 23
alien_0['y_position'] = 56
print(alien_0)
# 修改键-值对
alien_1 = {'x_position':0,'y_position':0,'speed':'medium'}
print("Original x_position: "+str(alien_1['x_position']))
if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_1['x_position'] = alien_1['x_position'] + x_increment
print("new position: " + str(alien_1['x_position']))
del alien_1['y_position']
print(alien_1)
# 遍历字典
favorite_languages = {'liyang':'c','lyb':'matlab','hiyoung':'java'}
print("hiyoung's favorite language is "+favorite_languages['hiyoung'].title()+".")
for name,language in favorite_languages.items():
    print(name.title()+"'s favorite language is "+language+".")

# keys function
for name in favorite_languages.keys():
    print(name.title())

if 'enrique' not in favorite_languages.keys():
    print("enrique,please take our poll")
# sorted对键排序。
for name in sorted(favorite_languages.keys()):
    print(name.title()+",thank you for taking the poll.")

# value function
for language in favorite_languages.values():
    print(language.title())

# set
for language in set(favorite_languages.values()):
    print(language.title())

# nest
alien_1 = {'color':'green','point':5}
alien_2 = {'color':'red','point':8}
alien_3 = {'color':'black','point':9}
aliens = [alien_1,alien_2,alien_3]
for alien in aliens:
    print(alien)


aliens = []
for alien_number in range(30):
    new_alien = {'color':'green','point':5}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print("...")
print("Total number of aliens "+str(len(aliens)))

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['point'] = 10
for alien in aliens[0:5]:
    print(alien)
print("...")

# dict-dict
users = {'newton':{'first':'albert','last':'einstein','location':'princeton'},
       'mikey':{'first':'marie','last':'curie','location':'paris'}}
for username,user_info in users.items():
    print("\nUsername: "+username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tlocation: " + location.title())

