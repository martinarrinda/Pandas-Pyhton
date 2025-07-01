import pandas as pd
datos = {"Dia": ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"],
        "Categoria":["Comida","Ocio","Personal","Transporte","Salud","Viajes","Pagos"],
        "Concepto":["Restaurante","Cine","Dentista","Bus","Gimnasio","Hotel","Bizum"],
        "Costo":[50,7,65,4,34,125,30]}

df = pd.DataFrame(datos)

gasto_total_semana = df["Costo"].sum()
print(f"El gasto total de la semana es de {gasto_total_semana} euros.")

gasto_comida = df.loc[0,"Costo"]
print(f"En comida te has gastado un total de {gasto_comida} euros.")

gasto_ocio = df.loc[1,"Costo"]
print(f"En ocio te has gastado un total de {gasto_ocio} euros.")

gasto_personal = df.loc[2,"Costo"]
print(f"En personal te has gastado un total de {gasto_personal} euros.")

gasto_transporte = df.loc[3,"Costo"]
print(f"En transporte te has gastado un total de {gasto_transporte} euros.")

gasto_salud = df.loc[4,"Costo"]
print(f"En salud te has gastado un total de {gasto_salud} euros.")

gasto_viajes = df.loc[4,"Costo"]
print(f"En viajes te has gastado un total de {gasto_viajes} euros.")

gasto_pagos = df.loc[4,"Costo"]
print(f"En pagos te has gastado un total de {gasto_pagos} euros.")

cantidad_mas_gastada = df["Costo"].max()
posicion_dia_mas_gastado = df["Costo"].idxmax()
dia_mas_gastado = df.loc[posicion_dia_mas_gastado,"Dia"]
print(f"El dia que mas dinero gastaste fue el {dia_mas_gastado}, gastaste un total de {cantidad_mas_gastada} euros.")

concepto_mas_gastado = df.loc[posicion_dia_mas_gastado,"Concepto"]
print(f"En el concepto que mas dinero has gastdo es en: {concepto_mas_gastado}.")

esenciales = ["Comida","Transporte"]
df["Esenciales"] = df["Categoria"].apply(lambda x: "Si" if x in esenciales else "No")

df.to_csv("gastos_semanles.csv", index = False)
