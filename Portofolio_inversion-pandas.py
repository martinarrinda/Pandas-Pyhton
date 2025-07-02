import pandas as pd
datos = {"Empresa":["AAPL","TSLA","MSFT","AMZN","NVDA","META"],
        "Precio inicial($)": [192.45,173.25,322,120.8,130.5,305.7],
        "Precio final($)": [195.1,169.5,327.4,125.2,136,299],
        "Cantidad": [10,5,3,8,4,2] }

df = pd.DataFrame(datos)

#VARIACION TOTAL APPL
nombrar_APPL = df.loc[0,"Empresa"]
variacion_APPL = round ((df.loc[0,"Precio final($)"] - df.loc[0,"Precio inicial($)"]) * df.loc[0,"Cantidad"],1)
df.loc[0,"Variacion total"] = variacion_APPL

#VARIACION TOTAL TSLA
nombrar_TSLA = df.loc[1,"Empresa"]
variacion_TSLA = round ((df.loc[1,"Precio final($)"] - df.loc[1,"Precio inicial($)"]) * df.loc[1,"Cantidad"],1)
df.loc[1,"Variacion total"] = variacion_TSLA

#VARIACION TOTAL MSFT
nombrar_MSFT = df.loc[2,"Empresa"]
variacion_MSFT = round ((df.loc[2,"Precio final($)"] - df.loc[2,"Precio inicial($)"]) * df.loc[2,"Cantidad"],1)
df.loc[2,"Variacion total"] = variacion_MSFT

#VARIACION TOTAL AMZN
nombrar_AMZN = df.loc[3,"Empresa"]
variacion_AMZN= round ((df.loc[3,"Precio final($)"] - df.loc[3,"Precio inicial($)"]) * df.loc[3,"Cantidad"],1)
df.loc[3,"Variacion total"] = variacion_AMZN

#VARIACION TOTAL NVDA
nombrar_NVDA = df.loc[4,"Empresa"]
variacion_NVDA = round ((df.loc[4,"Precio final($)"] - df.loc[4,"Precio inicial($)"]) * df.loc[4,"Cantidad"],1)
df.loc[4,"Variacion total"] = variacion_NVDA

#VARIACION TOTAL META
nombrar_META = df.loc[5,"Empresa"]
variacion_META= round ((df.loc[5,"Precio final($)"] - df.loc[5,"Precio inicial($)"]) * df.loc[5,"Cantidad"],1)
df.loc[5,"Variacion total"] = variacion_META

#PORCENTAJE DE CAMBIO 
porcentaje_cambio_APPL = round (((df.loc[0,"Precio final($)"]- df.loc[0,"Precio inicial($)"]) /  df.loc[0,"Precio inicial($)"]) * 100,1)
porcentaje_cambio_TSLA = round (((df.loc[1,"Precio final($)"]- df.loc[1,"Precio inicial($)"]) /  df.loc[1,"Precio inicial($)"]) * 100,1)
porcentaje_cambio_MSFT = round (((df.loc[2,"Precio final($)"]- df.loc[2,"Precio inicial($)"]) /  df.loc[2,"Precio inicial($)"]) * 100,1)
porcentaje_cambio_AMZN = round (((df.loc[3,"Precio final($)"]- df.loc[3,"Precio inicial($)"]) /  df.loc[3,"Precio inicial($)"]) * 100,1)
porcentaje_cambio_NVDA= round (((df.loc[4,"Precio final($)"]- df.loc[4,"Precio inicial($)"]) /  df.loc[4,"Precio inicial($)"]) * 100,1)
porcentaje_cambio_META = round (((df.loc[5,"Precio final($)"]- df.loc[5,"Precio inicial($)"]) /  df.loc[5,"Precio inicial($)"]) * 100,1)
df.loc[0, "Porcentaje de cambio (%)"] = porcentaje_cambio_APPL
df.loc[1, "Porcentaje de cambio (%)"] = porcentaje_cambio_TSLA
df.loc[2, "Porcentaje de cambio (%)"] = porcentaje_cambio_MSFT
df.loc[3, "Porcentaje de cambio (%)"] = porcentaje_cambio_AMZN
df.loc[4, "Porcentaje de cambio (%)"] = porcentaje_cambio_NVDA
df.loc[5, "Porcentaje de cambio (%)"] = porcentaje_cambio_META
print(df)


#MEJOR INVERSION
mayor_ganacia = df["Variacion total"].max()
posicion_mayor_ganacia = df["Variacion total"].idxmax()
empresa_mayor_ganancia = df.loc[posicion_mayor_ganacia,"Empresa"]
print(f"Tu mejor inversion fue en la empresa {empresa_mayor_ganancia} con un beneficio total de {mayor_ganacia}$.")


#PEOR INVERSION
menor_ganacia = df["Variacion total"].min()
posicion_menor_ganacia = df["Variacion total"].idxmin()
empresa_menor_ganancia = df.loc[posicion_menor_ganacia,"Empresa"]
print(f"Tu peor inversion fue en la empresa {empresa_menor_ganancia} con una perdida total de {menor_ganacia}$.")

#RENDIMIENTO TOTAL DE LA CARTERA
rendimiento = round(df["Variacion total"].sum(),1)
print(f"El rendimiento total de la cartera es de {rendimiento}$.")

#EMPRESAS CON RENDIMIENTO POSITIVO
print("Las empresas con rendimiento positivo son las siguentes: ")
positivos = df[df["Variacion total"] >= 0]["Empresa"].values
print(positivos)

#GUARDAR EN FORMATO CSV
df.to_csv("Portfolio.csv",index=False)