def metro_a_pulgadas(metros):
    return metros * 39.37


def pulgadas_a_pies(pulgadas):
    return pulgadas / 12

if __name__=="_main_":
    metros=int(input("ingese la cantidad en metros"))
    pulgadas=metro_a_pulgadas(metros)
    print(f"{metros}metros equivalente a {pulgadas:.2f}pulgadas")