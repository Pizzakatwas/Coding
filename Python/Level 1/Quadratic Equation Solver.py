import math
print('Hello and welcome to my second degree equation solver, please state your parameters (ax^2+bx+c)')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
determinant = pow(b,2)-4*a*c
print('The determinant of this equation is: '+str(determinant))
if determinant>0:
    print('your equation has two real solutions')
    solution1 = -b+math.sqrt(determinant)/2*a
    solution2 = -b-math.sqrt(determinant)/2*a
    print(solution1,solution2)
elif determinant==0:
    print('your equation has 1 unique real solution')
    solution=-b/2*a
    print(solution)
else:
    print('ew, your equation has no real solutions.')