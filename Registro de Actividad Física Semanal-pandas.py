import pandas as pd
datos = {"Dias": ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado","Domingo"],
         "Actividad": ["Gimnasio","Nadar","Gimnasio","Descanso","Gimnasio","Bici","Correr"],
         "Minutos" : [70,40,55,0,65,90,35],
         "Calorias" : [400,450,350,0,400,800,450]
         }

df = pd.DataFrame(datos)
print(df)

minutos_entrenados = df["Minutos"].sum()
print(f"Esta semana has entrenado un total de {minutos_entrenados} minutos.")

calorias_quemadas = df ["Calorias"].sum()
print(f"Esta semana has quemado un total de {calorias_quemadas} kcal.")

dia_mas_tiempo = df ["Minutos"].max()
indice_mas_tiempo = df["Minutos"].idxmax()
dia_semana_max_tiempo = df.loc[indice_mas_tiempo,"Dias"]
print(f"El dia que mas entrenaste fue el {dia_semana_max_tiempo} entrenaste un total de {dia_mas_tiempo} minutos.")

mas_30_mins_entreno = df["Minutos"] >= 30
dias_mas_30_mins = df.loc[mas_30_mins_entreno,"Dias"]
print(f"Los dias: {list(dias_mas_30_mins)} entrenaste mas de 30 minutos, Enhorabuena!")
