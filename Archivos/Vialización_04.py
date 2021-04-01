#!/usr/bin/env python
# coding: utf-8

# # Visualización de datos
# 
# **Integrantes:**
# 
#     - 1802780, Ramírez Medellín, Sahori Verónica
#     - 1937834, Flores Guerra, Irlanda Victoria
#     - 1806559, Treviño Elizondo, Melenie Anahí
#     - 1802294, Núñez Márquez,Kevin Orlando
#     
# **Equipo: 04**
# 
# **Grupo: 003** 
# 
# ## Suicide Rates Overview 1985 to 2016
# 
# https://www.kaggle.com/russellyates88/suicide-rates-overview-1985-to-2016
# 
# 
# # Estadística Básica de los datos
# **Visualización del dataset:** Creación y visualización de un data frame con los datos del dataset obtenido después de la limpieza, así para poder determinar las columnas que utilizaremos para el análisis de los estadísticos básicos que mejor nos ayudan a entender los datos.

# In[1]:


import pandas as pd
import geopandas as gpd 
import plotly as plot

suicidios_limpieza=pd.read_csv("C:/Users/almag/Documents/7mo Semestre/Minería de Datos/suicidios-limpieza.csv")
df = pd.DataFrame(suicidios_limpieza)
df


# **Determinación de las columnas a análizar:**
# 
# - **Edad:** Número de Suicidios según el intervalo de edad en el que se cometieron. 
# 
# - **Número de Suicidios:** Número de suicidios cometidos de 1985 al 2016.
# 
# - **Población:** Población de los respectivos paises a través de 1985 al 2016.
# 
# - **Suicidios por cada 100K:** Indice de suicidios cometidos por cada 100 mil habitantes de 1985 al 2016.
# 
# - **PIB:** Producto Interno Bruto de los respectivos países a través de 1985 al 2016.
# 
# - **Generación:** Número de suicidios cometidos según la generación en la que se cometieron.
# 
# ## Edad

# In[2]:


edades=list(suicidios_limpieza['EDAD'].unique())
data = {'EDAD': edades}
dfe = pd.DataFrame(data, columns = [ 'EDAD'])
dfe


# In[3]:


i=0
suicidios_edades=suicidios_limpieza["EDAD"]==edades[i]
registros_edades=suicidios_limpieza[suicidios_edades]
datos_totaledades=pd.DataFrame()
suma_i = []
promedio_i = []
Resumen_estadístico_i = []
Elementos_nulos_i = []
Min_i = []
Max_i = []
Mediana_i = []
Varianza_i = []
Desv_i = []
Asimetria_i = []
Probabilidad_i = []
data = []

for i in range(len(edades)):  
    suicidios_edades=suicidios_limpieza["EDAD"]==edades[i]
    registros_edades=suicidios_limpieza[suicidios_edades]
    
    suma_i.append(registros_edades['NUM_SUICIDIOS'].sum())
    promedio_i.append(registros_edades['NUM_SUICIDIOS'].mean())
    Resumen_estadístico_i.append(registros_edades['NUM_SUICIDIOS'].describe())
    Elementos_nulos_i.append(registros_edades['NUM_SUICIDIOS'].count())
    Min_i.append(registros_edades['NUM_SUICIDIOS'].min())
    Max_i.append(registros_edades['NUM_SUICIDIOS'].max())
    Mediana_i.append(registros_edades['NUM_SUICIDIOS'].median())
    Varianza_i.append(registros_edades['NUM_SUICIDIOS'].var())
    Desv_i.append(registros_edades['NUM_SUICIDIOS'].std())
    Asimetria_i.append(registros_edades['NUM_SUICIDIOS'].skew())
    Probabilidad_i.append(registros_edades['NUM_SUICIDIOS'].kurt())
    
df2 = pd.DataFrame({"EDAD":edades,
                    "Suma":suma_i,"Promedio":promedio_i,
                   "Elementos nulos":Elementos_nulos_i,"Minimo":Min_i,
                    "Maximo":Max_i,
                   "Mediana":Mediana_i,
                   "Varianza":Varianza_i,
                   "Desviacion Estandar":Desv_i,
                   "Asimetria":Asimetria_i,
                   "Distribucion de Frecuencias":Probabilidad_i})
df2.T


# ## Número de Suicidios

# In[4]:


a="NUM_SUICIDIOS"

Suma=df[a].sum()
Promedio=df[a].mean()
Resumen_estadístico=df[a].describe()
Elementos_nulos=df[a].count()
Minimo=df[a].min()
Maximo=df[a].max()
Mediana=df[a].median()
Varianza=df[a].var()
Desv=df[a].std()
Asimetria=df[a].skew()
Probabilidad=df[a].kurt()

print("Suma= ",Suma)
print("Promedio= ",Promedio)
print("Resumen Estadistico= ",Resumen_estadístico)
print("Elementos nulos= ",Elementos_nulos)
print("Minimo= ",Minimo)
print("Maximo= ",Maximo)
print("Varianza= ",Varianza)
print("Desviacion Estandar= ",Desv)
print("Asimetria= ",Asimetria)
print("Probabilidad de Frecuencia= ",Probabilidad)


# ## Población

# In[5]:


b="POBLACION"

Suma=df[b].sum()
Promedio=df[b].mean()
Resumen_estadístico=df[b].describe()
Elementos_nulos=df[b].count()
Minimo=df[b].min()
Maximo=df[b].max()
Mediana=df[b].median()
Varianza=df[b].var()
Desv=df[b].std()
Asimetria=df[b].skew()
Probabilidad=df[b].kurt()

print("Suma= ",Suma)
print("Promedio= ",Promedio)
print("Resumen Estadistico= ",Resumen_estadístico)
print("Elementos nulos= ",Elementos_nulos)
print("Minimo= ",Minimo)
print("Maximo= ",Maximo)
print("Varianza= ",Varianza)
print("Desviacion Estandar= ",Desv)
print("Asimetria= ",Asimetria)
print("Probabilidad de Frecuencia= ",Probabilidad)


# ## Suicidios por cada 100k

# In[6]:


d="SUICIDIOS POR CADA 100K"

Suma=df[d].sum()
Promedio=df[d].mean()
Resumen_estadístico=df[d].describe()
Elementos_nulos=df[d].count()
Minimo=df[d].min()
Maximo=df[d].max()
Mediana=df[d].median()
Varianza=df[d].var()
Desv=df[d].std()
Asimetria=df[d].skew()
Probabilidad=df[d].kurt()

print("Suma= ",Suma)
print("Promedio= ",Promedio)
print("Resumen Estadistico= ",Resumen_estadístico)
print("Elementos nulos= ",Elementos_nulos)
print("Minimo= ",Minimo)
print("Maximo= ",Maximo)
print("Varianza= ",Varianza)
print("Desviacion Estandar= ",Desv)
print("Asimetria= ",Asimetria)
print("Probabilidad de Frecuencia= ",Probabilidad)


# ## PIB

# In[ ]:





# ## Generación

# In[7]:


generaciones=list(suicidios_limpieza['GENERACION'].unique())
data = {'Generacion': generaciones}
dfg = pd.DataFrame(data, columns = [ 'Generacion'])
dfg


# In[8]:


i=0
suicidios_generaciones=suicidios_limpieza["GENERACION"]==generaciones[i]
registros_generaciones=suicidios_limpieza[suicidios_generaciones]
datos_totalgeneraciones=pd.DataFrame()
suma_i = []
promedio_i = []
Resumen_estadístico_i = []
Elementos_nulos_i = []
Min_i = []
Max_i = []
Mediana_i = []
Varianza_i = []
Desv_i = []
Asimetria_i = []
Probabilidad_i = []
data = []
for i in range(len(generaciones)):
    suicidios_generaciones=suicidios_limpieza["GENERACION"]==generaciones[i]
    registros_generaciones=suicidios_limpieza[suicidios_generaciones]
 
    suma_i.append(registros_generaciones['NUM_SUICIDIOS'].sum())
    promedio_i.append(registros_generaciones['NUM_SUICIDIOS'].mean())
    Resumen_estadístico_i.append(registros_generaciones['NUM_SUICIDIOS'].describe())
    Elementos_nulos_i.append(registros_generaciones['NUM_SUICIDIOS'].count())
    Min_i.append(registros_generaciones['NUM_SUICIDIOS'].min())
    Max_i.append(registros_generaciones['NUM_SUICIDIOS'].max())
    Mediana_i.append(registros_generaciones['NUM_SUICIDIOS'].median())
    Varianza_i.append(registros_generaciones['NUM_SUICIDIOS'].var())
    Desv_i.append(registros_generaciones['NUM_SUICIDIOS'].std())
    Asimetria_i.append(registros_generaciones['NUM_SUICIDIOS'].skew())
    Probabilidad_i.append(registros_generaciones['NUM_SUICIDIOS'].kurt())

df1 = pd.DataFrame({"Generacion":generaciones,
                    "Suma":suma_i,"Promedio":promedio_i,
                   "Elementos nulos":Elementos_nulos_i,"Minimo":Min_i,
                    "Maximo":Max_i,
                   "Mediana":Mediana_i,
                   "Varianza":Varianza_i,
                   "Desviacion Estandar":Desv_i,
                   "Asimetria":Asimetria_i,
                   "Distribucion de Frecuencias":Probabilidad_i})
df1.T


# ### Correlación y Covarianza entre Año, Número de Suicidios, Población y Suicidios por cada 100k

# - **Correlación**

# In[9]:


df.corr()


# - **Covarianza**

# In[10]:


df.cov()


# # Gráficas
# **Visualización de datos:** Visualización de un data frame con los datos obtenidos del resumen de la limpieza de datos en la práctica 1.

# In[11]:


import pandas as pd
import numpy as np

suicidios_limpieza=pd.read_csv("C:/Users/almag/Documents/7mo Semestre/Minería de Datos/suicidios-limpieza.csv")
df = pd.DataFrame(suicidios_limpieza)
df


# ## Gráficas de barras
# <!--  -->
# _Grafica de barras del total de suicidios por año de 1985 a 2016._

# In[12]:


suicidios_años= pd.DataFrame(suicidios_limpieza['AÑO'])
suicidios_años.insert(1,'NUM_SUICIDIOS',suicidios_limpieza['NUM_SUICIDIOS'])
datos_totalsuicidios= pd.Series()


for i in range(0,32):  
    suicidios_poraño=suicidios_años["AÑO"]==1985+int(i)
    registros_poraño=suicidios_años[suicidios_poraño]
    total_suicidios_poraño=registros_poraño['NUM_SUICIDIOS'].sum() 
    datos_totalsuicidios=datos_totalsuicidios.append(pd.Series(total_suicidios_poraño,index=[1985+int(i)]))

graficobarra=datos_totalsuicidios
graficobarra.plot.bar(title='TOTAL DE SUICIDIOS POR AÑO')


# In[13]:


import seaborn as sbs
sbs.countplot(datos_totalsuicidios)


# ## Gráfico Interactivo de Líneas
# _Gráfico de línea del número de suicidios por año de 1985 al 2016._ 

# In[14]:


import plotly.express as pl
grafico_totalsuicidios=pl.line(datos_totalsuicidios,
                               x=datos_totalsuicidios.index.values.tolist(),
                               y=datos_totalsuicidios.values.tolist(),title="NÚMERO DE SUICIDIOS POR AÑO")
grafico_totalsuicidios.show()


# ## Gráfico de Líneas Interactivo
# _Gráfica de línea Interactivo de la cantidad de suicidios por país en el año con mayor suicidios registrados entre 1985 al 2016._
# 
# 
# En base a la gráfica de barras, se puede observar a simple vista que existen 4 años (1999,2000,2002, 2003) en los que eixstió una mayor cantidad de suicidios, entre ellas se buscó el año que cuenta con una mayor cantidad de suicidios para así poder determinar el país con mayor número de suicidios en dicho año.

# In[41]:


PARTICION=datos_totalsuicidios.iloc[14:19]
mayor=0
for año in range(len(PARTICION)):
    menor=PARTICION.values[año]
    if menor>mayor:
        AÑO=PARTICION.index.values[año]
        mayor=menor
print('El año con mayor número de suicidios en el tiempo es:\t el año de',AÑO,'con un total de ',mayor, "suicidios.")


# __¿Qué países son los que no aparecen en 1999?__
# 
# En 1999 hay 83 de los 101 presentes en base de datos.

# In[42]:


suicidios_1999=suicidios_limpieza['AÑO']==1999
registros_1999=suicidios_limpieza[suicidios_1999]
paises_1999=list(registros_1999['PAIS'].unique())

paises_totales=list(suicidios_limpieza['PAIS'].unique())

paises_no_registrados1999=list()
for i in range(len(paises_totales)):
    if paises_totales[i] not in paises_1999:
        print('PAIS NO REGISTRADO EN 1999: ',paises_totales[i])
        paises_no_registrados1999.append(paises_totales[i])
datos_totalsuicidios_1999_ppais=pd.Series()
for i in range(len(paises_1999)):  
    suicidios_1999_ppais=registros_1999["PAIS"]==paises_1999[i]
    registros_1999_ppais=registros_1999[suicidios_1999_ppais] 
    total_registros_1999_ppais=registros_1999_ppais['NUM_SUICIDIOS'].sum() 
    datos_totalsuicidios_1999_ppais=datos_totalsuicidios_1999_ppais.append(pd.Series(total_registros_1999_ppais,index=[paises_1999[i]]))
    
grafico_totalsuicidios_1999=pl.line(datos_totalsuicidios_1999_ppais,
                               x=datos_totalsuicidios_1999_ppais.index.values.tolist(),
                               y=datos_totalsuicidios_1999_ppais.values.tolist(), title="1999 AÑO CON MAYOR NÚMERO DE SUICIDIOS")
grafico_totalsuicidios_1999.show()

grafico_linea=datos_totalsuicidios_1999_ppais
grafico_linea.plot.line(title="1999 AÑO CON MAYOR NÚMERO DE SUICIDIOS")


# ## Gráfico de Líneas Interactivo
# _Gráfico de líneas interactivo del país con mayor frecuencia de suicidios en el año de 1999 a través de los años de 1985 al 2016._

# In[46]:


suicidios_federacion_rusa=suicidios_limpieza["PAIS"]=='Russian Federation'

registros_federacion_rusa=suicidios_limpieza[suicidios_federacion_rusa] 

datos_totalsuicidios_federacion= pd.Series()

datos_totalpoblacion_federacion= pd.Series()

for i in range(0,32):  

    registros_federacion_poraño=registros_federacion_rusa["AÑO"]==1985+int(i)

    registros_poraño_federacion=registros_federacion_rusa[registros_federacion_poraño] 
    
    total_suicidios_poraño_federacion=registros_poraño_federacion['NUM_SUICIDIOS'].sum()
    
    datos_totalsuicidios_federacion=datos_totalsuicidios_federacion.append(pd.Series(total_suicidios_poraño_federacion,index=[1985+int(i)]))

    total_poblacion_poraño_federacion=registros_poraño_federacion['POBLACION'].sum()
    
    datos_totalpoblacion_federacion=datos_totalpoblacion_federacion.append(pd.Series(total_poblacion_poraño_federacion,index=[1985+int(i)]))
        
grafico_linea_federacion=pl.line(datos_totalsuicidios_federacion,
                               x=datos_totalsuicidios_federacion.index.values.tolist(),
                               y=datos_totalsuicidios_federacion.values.tolist(),title='NÚMERO DE SUICIDIOS, FEDERACION RUSA')
grafico_linea_federacion.show()


# ## Histograma
# 
# _Histograma por intervalos de años._

# In[18]:


suicidios_limpieza['AÑO'].plot.hist(title="Cantidad de suicidios por intervalo de años")


# ## Scatter Plot

# In[44]:


#--------------------SCATTER PLOT -----
 #COMPARATIVA 1: RELACION CON EL PIB Y NUM. SUICIDIOS
'''
APARTIR DEL PAIS CON MAYOR NUM DE SUICIDIOS DEL AÑO CON MAYOR NUM DE SUICIDIOS REGISTRADOS,
SE HACE UNA COMPARATIVA DEL PAIS PARA ANALIZAR SI EL NIVEL DE RIQUEZA DEL MISMO ESTA RELACIONADO CON 
LA CANTIDAD DE SUICIDIOS
'''

suicidios_años_federacion=datos_totalsuicidios_federacion.iloc[4:31]
pip_federacion=registros_federacion_rusa['PIB'].unique()
grafico_scatter1=pd.DataFrame(suicidios_años_federacion)

#crendo grafico scatter plot
grafico_scatter1.insert(1,'PIB',pip_federacion)
grafico_scatter1.sample(15).plot.scatter(x='PIB',y=0) #checa este el sample hace que cambie son 27 registros en tota


# In[49]:


#--------------------SCATTER PLOT -----
#COMPARATIVO 2: RELACION CON LA POBLACION Y NUM.SUICIDIOS
'''
APARTIR DEL PAIS CON MAYOR NUM DE SUICIDIOS DEL AÑO CON MAYOR NUM DE SUICIDIOS REGISTRADOS,
SE HACE UNA COMPARATIVA DEL PAIS PARA ANALIZAR SI EL NIVEL DE POBLACION DEL MISMO ESTA RELACIONADO CON 
LA CANTIDAD DE SUICIDIOS
'''
poblacion_años_federacion=datos_totalpoblacion_federacion.iloc[4:31]
grafico_scatter2=pd.DataFrame(suicidios_años_federacion)
grafico_scatter2.insert(1,'POBLACION',poblacion_años_federacion)


# In[48]:


#CREADNO COMPARATIVA 2 
grafico_scatter2.plot.scatter(x='POBLACION',y=0)
grafico_scatter2.sample(15).plot.scatter(x=0,y='POBLACION')


# ## Stacked Plot Interactivo
# _Stacked Plot Interactivo del total de suicidios por intervalo de edad según el sexo del individuo._

# In[22]:


lista_intervalos_edades=list(suicidios_limpieza['EDAD'].unique())
datos_totalregistros_porintervalo=pd.Series()
datos_totalregistros_porintervalo_genero1=pd.Series()
datos_totalregistros_porintervalo_genero2=pd.Series()

for i in range(0,len(lista_intervalos_edades)):  
    suicidios_porintervalo=suicidios_limpieza["EDAD"]==lista_intervalos_edades[i]
    registros_porintervalo=suicidios_limpieza[suicidios_porintervalo] 
    total_suicidios_porintervalo=registros_porintervalo['NUM_SUICIDIOS'].sum() 
    datos_totalregistros_porintervalo=datos_totalregistros_porintervalo.append(pd.Series(total_suicidios_porintervalo,index=[lista_intervalos_edades[i]]))

    suicidios_porintervalo_genero1=registros_porintervalo["SEXO"]=='female'
    suicidios_porintervalo_genero2=registros_porintervalo["SEXO"]=='male'
    
    registros_porintervalo_genero1=registros_porintervalo[suicidios_porintervalo_genero1]
    registros_porintervalo_genero2=registros_porintervalo[suicidios_porintervalo_genero2]

    
    total_suicidios_porintervalo_genero1=registros_porintervalo_genero1['NUM_SUICIDIOS'].sum()
    total_suicidios_porintervalo_genero2=registros_porintervalo_genero2['NUM_SUICIDIOS'].sum()
    
    datos_totalregistros_porintervalo_genero1=datos_totalregistros_porintervalo_genero1.append(pd.Series(total_suicidios_porintervalo_genero1,index=[lista_intervalos_edades[i]]))
    datos_totalregistros_porintervalo_genero2=datos_totalregistros_porintervalo_genero2.append(pd.Series(total_suicidios_porintervalo_genero2,index=[lista_intervalos_edades[i]]))


# In[23]:


datos_H_M=datos_H_M={'FEMENINO':datos_totalregistros_porintervalo_genero1,'MASCULINO':datos_totalregistros_porintervalo_genero2}
datos_H_M=pd.DataFrame(datos_H_M)

grafico_stackedplot=pl.bar(datos_H_M.T,title='SUICIDIOS TOTALES POR INTERVALO DE EDAD')
grafico_stackedplot.show()

grafico_stackedplotarea=pl.area(datos_H_M.T,title='SUICIDIOS TOTALES POR INTERVALO DE EDAD')
grafico_stackedplotarea.show()

grafico_stackedplotline=pl.line(datos_H_M.T,title='SUICIDIOS TOTALES POR INTERVALO DE EDAD')
grafico_stackedplotline.show()


# ## Gráfico Interactivo de Barra

# In[24]:


grafico_barra_intervalos=pl.bar(datos_totalregistros_porintervalo,title='SUICIDIOS TOTALES POR INTERVALO DE EDAD')
grafico_barra_intervalos.show()


# ## Blox Plot
# 
# 

# In[25]:


generaciones=list(suicidios_limpieza['GENERACION'].unique())
datos_totalgeneraciones=pd.Series()
for i in range(len(generaciones)):  
    suicidios_generaciones=suicidios_limpieza["GENERACION"]==generaciones[i]
    registros_generaciones=suicidios_limpieza[suicidios_generaciones] 
    total_registros_generaciones=registros_generaciones['NUM_SUICIDIOS'].sum() 
    datos_totalgeneraciones=datos_totalgeneraciones.append(pd.Series(total_registros_generaciones,index=[generaciones[i]]))
    
    if generaciones[i]=='Generation X':
        serie1=pd.Series(registros_generaciones['NUM_SUICIDIOS'])
    elif generaciones[i]=='Boomers':
        serie2=pd.Series(registros_generaciones['NUM_SUICIDIOS'])
    elif generaciones[i]=='Silent':
        serie3=pd.Series(registros_generaciones['NUM_SUICIDIOS'])
    elif generaciones[i]=='G.I. Generation':
        serie4=pd.Series(registros_generaciones['NUM_SUICIDIOS'])
    elif generaciones[i]=='Millenials':
        serie5=pd.Series(registros_generaciones['NUM_SUICIDIOS'])
    elif generaciones[i]=='Generation Z':
        serie6=pd.Series(registros_generaciones['NUM_SUICIDIOS'])
import seaborn as sbs

sbs.boxplot(serie1)
print('BOXPLOT DE: GENERACION X')


# In[26]:


print('BOXPLOT DE: BOOMERS')
sbs.boxplot(serie2)


# In[27]:


print('BOXPLOT DE: SILENT')
sbs.boxplot(serie3)


# In[28]:


print('BOXPLOT DE: G.I. GENERATION')
sbs.boxplot(serie4)


# In[29]:


print('BOXPLOT DE: MILENIALS')
sbs.boxplot(serie5)


# In[30]:


print('BOXPLOT DE: GENERACION Z')
sbs.boxplot(serie6)


# # PUNTOS EXTRA
# ## Gráfica de pastel
# _Gráfica de pastel del porcentaje de suicidios por generación._
# 

# In[31]:


grafico_generaciones_pastel=datos_totalgeneraciones
grafico_generaciones_pastel.plot.pie(autopct='%1.1f%%',title='PORCENTAJE DE SUICIDIOS POR GENERACIÓN')


# In[ ]:





# In[ ]:




