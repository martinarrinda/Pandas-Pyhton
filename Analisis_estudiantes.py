import pandas as pd

datos = {
    "Nombre": ["Ana", "Luis", "Marta", "Javi", "Lucía"],
    "Edad": [21, 22, 20, 23, 21],
    "Nota": [7.5, 8.0, 6.5, 9.0, 5.5]
}

df = pd.DataFrame(datos)
print(df)

nota_media = df["Nota"].mean()
print(nota_media)

nota_mayor_7 = df[df["Nota"] >= 7]
print(nota_mayor_7)

ordenador_menor_mayor = df.sort_values(by="Nota",ascending=False)
print(ordenador_menor_mayor)
