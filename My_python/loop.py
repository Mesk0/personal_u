FootballPlay=['messi','iniesta','busquets','xavi']
for player in FootballPlay:
   print(player.title()+"is one of the best football players")
   print("I can't wait to see his next game,"+player.title()+".\n")
print("thank everyone")

for value in range(1,5):
   print(value)

numbers=list(range(1,11))
print(numbers)

even_numbers=list(range(2,11,2))
print(even_numbers)

squares=[]
for value in range(1,11):
   square=value**2
   squares.append(square)
print(squares)

squares=[]
for value in range(1,11):
   squares.append(value**2)
print(squares)
print(max(squares))

squares=[value**2 for value in range(1,11)]
print(squares)

series_a=['inter','juventus','milan','caligari','troine','roma','lazio','florentina','atalanta','bolonga']
print(series_a[1:11])
print(series_a[:11])
print(series_a[1:])
print(series_a[-2:])
for club in series_a[-3:]:
   print(club.title())

MyClub=series_a[:]
print(MyClub)

dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])
for dimension in dimensions:
   print(dimension)

dimensionA=[500,400]
for dimensiona in dimensionA:
   print(dimensiona)
dimensionA=[300,200]
for dimensiona in dimensionA:
   print(dimensiona)

