

print("Dados da primeira pessoa: ")
nome1 = input("Nome: ")
idade1 = int(input("idade: "))

print("Dados da segunda pessoa: ")
nome2 = input("Nome: ")
idade2 = int(input("idade: "))

media = (idade1 + idade2) / 2

print(f"A idade media de {nome1} e {nome2} é de {media:.1f} anos")