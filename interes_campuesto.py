
def calcular_meses_duplicacion(capital):
    meses = 0
    while capital < 2 * capital_inicial:
        meses += 1
        capital *= 1.05
    print("El capital se duplica en", meses, "meses.")
capital_inicial = float(input("Ingrese el capital inicial: "))
calcular_meses_duplicacion(capital_inicial)
