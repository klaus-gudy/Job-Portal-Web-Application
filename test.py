
# Question: 1
numbers = ['',0,0,550,275,1100,550,1650,825,2200,1100,2750,1375,3300,1650,3850,1925,4400,2200]
n = int(input("Enter a number: "))
print(numbers[n])

# Question: 2
letters = ' abcdefghijklmnopqrstuvwxyz'
d = str(input("input: "))
e = str(input("string to be replaced: "))
b = str(input("string to be replaced with: "))
c = ''
for i in range(len(b)):
    c = c + str(letters.find(b[i]))
d = d.replace(e,b)
print('output: '+ d + ' ' + c)

# Question: 3
import random
a = str(input("Enter a String: "))
d = str(input("input: "))
b = a.lower()
print(f'Frequency of {d} = '+ str(b.count(d)))
letter = ['!','@','#','$','%','^','&','*','(',')','_','+','=','{','}','[',']','|',':',';','"','\'','<','>',',','.','?','/',' ']
print('Final String = '+b.title() +' '+ random.choice(letter))
