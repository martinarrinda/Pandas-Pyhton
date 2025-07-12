import pandas as pd
datos = {
    "Fecha": ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05',
             '2023-01-06', '2023-01-07', '2023-01-08', '2023-01-09', '2023-01-10'],
    "Cierre": [100, 101, 102, 101, 103, 104, 103, 105, 106, 107]
}

df = pd.DataFrame(datos)

#Calculo de la diferencia diaria del precio de cierre
x=0
y=1
z=1
count = 0
while count <= 8:
    diferencial = df.loc[x,"Cierre"] - df.loc[y,"Cierre"] 
    fecha = df.loc[z,"Fecha"]
    x +=1
    y +=1
    z +=1
    count +=1
    print(f"En la fecha {fecha} el cambio diferencial de acuerdo al dia anterior es de {diferencial}$.")
