def LerDinheiro(msg):
    valido = False
    while not valido:
        valor = str(input(msg)).replace(',','.').strip()
        if valor.isalpha() or valor == '':
            print(f'O valor "{valor}" não é válido!')
            continue
        else:
            valido = True
            return float(valor)
