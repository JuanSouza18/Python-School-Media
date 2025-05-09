def calcular_media():
    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))
    nota3 = int(input("Digite a terceira nota: "))
    media = (nota1 + nota2 + nota3) / 3
    
    print(f"A média do aluno é: {media}")
    return media

def situacao_aluno(media):
    if media >= 7:
        print(f"Parabéns, você foi aprovado! Sua média foi: {media}")
    elif media >= 5.0:
        print(f"Você está de recuperação. Sua média foi: {media}")
    else:
        print(f"Você foi reprovado. Sua média foi: {media}")
    
media = calcular_media()
situacao_aluno(media)
    