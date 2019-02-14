print("Digite dois numeros:")
y=int(input())
print("Escolha a operacao a ser feita:\n1-adicao\n2-subtracao\n3-multiplicacao\n4-divisao")
x=int(input())

if x==1:
    print("A soma eh: ",x+y)
elif x==2:
    print("A subtracao eh: ",x-y)
elif x==3:
    print("A multiplicacao eh: ",x*y)
elif x==4:
    print("A divisao eh: ",x/y)
else:
    print("A .... espera, nao entendi")