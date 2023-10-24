# parte_1
tupla_1 = (
    "Valor_1",
    2,
    3.1,
    "Kenzie Academy",
    ["Elemento1", "Elemento2"],
    "Kenzie Academy",
)

# print(tupla_1)

# parte_2
# print(tupla_1[-1])

# parte_3
# print(len(tupla_1))

# parte_4
# print(tupla_1.count("Kenzie Academy"))

# parte_5
# print(tupla_1.index(3.1))

# parte_6
# tupla_1[-1] = "Ultimo Elemento"
# tuplas não são alteráveis!!! (a menos que você converta em array e faça a desconversão com a alteração feita) # noqa

tupla_list = list(tupla_1)

tupla_list[-1] = "Ultimo Elemento"

tupla_1 = tuple(tupla_list)

print(tupla_1)
