import sys

NumeroLista=[]

while True:
    numero=int(input("Digite um numero: "))
    verificador=str(input("Deseja contiuar? [S/N]").lower())
    while verificador!="s" or "n":

        if verificador=="n":
            print("Reiniciando ...")
            break

        elif numero in NumeroLista:
            print("Número já está na lista. Por favor, escolha outro")
            break

        elif verificador=="s":
            NumeroLista.append(numero)
            print(NumeroLista)
            break

    continuar=str(input("Deseja finalizar a lista? [S/N]").lower())
    if continuar=="s":
        print("Adeus")
        sys.exit(0)