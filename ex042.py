a = int(input("Digite o tamanho da reta a: "))
b = int(input("Digite o tamanho da reta b: "))
c = int(input("Digite o tamanho da reta c: "))
if (a+b) > c:
    print("É possivel formar um triângulo com as medidas informadas")
    if a == b == c:
        print('Este triângulo é EQUILÁTERO')
    elif a == b != c or a != b == c or a == c != b:
        print('Este triângulo é ISÓCELES')
    elif a != b != c:
        print('Este triângulo é ESCALENO')

else:
    print("NÃO é possível formar um triângulo com as medidas informadas")