from arrays import Array

menu = Array(5)

for i in range (len(menu)):
    menu[i] = 1

menu.__damagevalues__()

print(menu)
print(menu.__sum__())
