nome = input("digite o nome ")
nota1 = int(input("digite um numero "))
nota2 = int(input("digite outro numero "))
nota3 = int(input("digite outro numero"))
nota4 = int(input("digite a ultimo numero"))
soma = nota1 + nota2 + nota3
print(soma)
media = soma/4
print(media)

if media > 7.0:
    print("aprovado")
elif media >= 5.0 < 7.0:
    print("recuperaçao")
else:
    print("reprovado")

                                                                                                                                                                