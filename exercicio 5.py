x=float(input())
y=float(input())
z=float(input())

if x+y<z or x+z<y or y+z<x:
    print("nao pode formar um triangulo")
else:
    if x==y or z==y or x==z:
        if x==y and x==z:
            print("Equilatero")
        else:
            print("Isoceles")
    else:
        print("Escaleno")