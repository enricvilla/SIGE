import sqlite3
import sys
import csv
import datetime

def guarda_Generacion(sensor_id,gen):
    conn=sqlite3.connect('/var/www/SIGE_app/SIGE_app.db')
    curs=conn.cursor()
    curs.execute("""INSERT INTO generacion values(datetime(CURRENT_TIMESTAMP, 'localtime'), (?), (?))""", (sensor_id,gen))
    conn.commit()
    conn.close()

def guarda_Consumo(sensor_id,cons):
    conn=sqlite3.connect('/var/www/SIGE_app/SIGE_app.db')
    curs=conn.cursor()
    curs.execute("""INSERT INTO consumo values(datetime(CURRENT_TIMESTAMP, 'localtime'), (?), (?))""", (sensor_id,cons))
    conn.commit()
    conn.close()

def guarda_Cons1(sensor_id,cons1):
    conn=sqlite3.connect('/var/www/SIGE_app/SIGE_app.db')
    curs=conn.cursor()
    curs.execute("""INSERT INTO cons1 values(datetime(CURRENT_TIMESTAMP, 'localtime'), (?), (?))""", (sensor_id,cons1))
    conn.commit()
    conn.close()

def guarda_Cons2(sensor_id,cons2):
    conn=sqlite3.connect('/var/www/SIGE_app/SIGE_app.db')
    curs=conn.cursor()
    curs.execute("""INSERT INTO cons2 values(datetime(CURRENT_TIMESTAMP, 'localtime'), (?), (?))""", (sensor_id,cons2))
    conn.commit()
    conn.close()

def guarda_Cons3(sensor_id,cons3):
    conn=sqlite3.connect('/var/www/SIGE_app/SIGE_app.db')
    curs=conn.cursor()
    curs.execute("""INSERT INTO cons3 values(datetime(CURRENT_TIMESTAMP, 'localtime'), (?), (?))""", (sensor_id,cons3))
    conn.commit()
    conn.close()

def guarda_TensionAC(sensor_id,vac):
    conn=sqlite3.connect('/var/www/SIGE_app/SIGE_app.db')
    curs=conn.cursor()
    curs.execute("""INSERT INTO vac values(datetime(CURRENT_TIMESTAMP, 'localtime'), (?), (?))""", (sensor_id,vac))
    conn.commit()
    conn.close()

def guarda_TensionDC(sensor_id,vdc):
    conn=sqlite3.connect('/var/www/SIGE_app/SIGE_app.db')
    curs=conn.cursor()
    curs.execute("""INSERT INTO vdc values(datetime(CURRENT_TIMESTAMP, 'localtime'), (?), (?))""", (sensor_id,vdc))
    conn.commit()
    conn.close()

def guarda_TensionBat(sensor_id,vbat):
    conn=sqlite3.connect('/var/www/SIGE_app/SIGE_app.db')
    curs=conn.cursor()
    curs.execute("""INSERT INTO vbat values(datetime(CURRENT_TIMESTAMP, 'localtime'), (?), (?))""", (sensor_id,vbat))
    conn.commit()
    conn.close()

def guarda_Frecuencia(sensor_id,frecuencia):
    conn=sqlite3.connect('/var/www/SIGE_app/SIGE_app.db')
    curs=conn.cursor()
    curs.execute("""INSERT INTO frecuencia values(datetime(CURRENT_TIMESTAMP, 'localtime'), (?), (?))""", (sensor_id,frecuencia))
    conn.commit()
    conn.close()


dt = datetime.date.today()
tm = datetime.datetime.today()
#tday = str(dt) + ' ' + str(tm.strftime("%H")) + ':' + str(tm.strftime("%M"))   #para cuando manejemos datos minutales
tday = str(dt) + ' ' + str(tm.strftime("%H")) + ':' + '00'   #mientras solo tengamos datos horarios en los csv

with open('/var/www/SIGE_app/Datos.csv','r') as Datos:
    Datos_reader = csv.DictReader(Datos)
    
    for line in Datos_reader:
        
        if line['Fecha'] == tday:
            gen = line['Generacion']
            guarda_Generacion("1", gen)
   
with open('/var/www/SIGE_app/Datos.csv','r') as Datos:
    Datos_reader = csv.DictReader(Datos)
    
    for line in Datos_reader:
        
        if line['Fecha'] == tday:
            cons = line['Consumo']
            guarda_Consumo("1", cons)

with open('/var/www/SIGE_app/Datos.csv','r') as Datos:
    Datos_reader = csv.DictReader(Datos)
    
    for line in Datos_reader:

        if line['Fecha'] == tday:
            cons1 = line['Cons1']
            guarda_Cons1("1", cons1)

with open('/var/www/SIGE_app/Datos.csv','r') as Datos:
    Datos_reader = csv.DictReader(Datos)
    
    for line in Datos_reader:

        if line['Fecha'] == tday:
            cons2 = line['Cons2']
            guarda_Cons2("1", cons2)

with open('/var/www/SIGE_app/Datos.csv','r') as Datos:
    Datos_reader = csv.DictReader(Datos)
    
    for line in Datos_reader:

        if line['Fecha'] == tday:
            cons3 = line['Cons3']
            guarda_Cons3("1", cons3)

with open('/var/www/SIGE_app/Datos.csv','r') as Datos:
    Datos_reader = csv.DictReader(Datos)
    
    for line in Datos_reader:

        if line['Fecha'] == tday:
            vac = line['TensionAC']
            guarda_TensionAC("1", vac)

with open('/var/www/SIGE_app/Datos.csv','r') as Datos:
    Datos_reader = csv.DictReader(Datos)
    
    for line in Datos_reader:

        if line['Fecha'] == tday:
            vdc = line['TensionDC']
            guarda_TensionDC("1", vdc)

with open('/var/www/SIGE_app/Datos.csv','r') as Datos:
    Datos_reader = csv.DictReader(Datos)
    
    for line in Datos_reader:

        if line['Fecha'] == tday:
            vbat = line['TensionBat']
            guarda_TensionBat("1", vbat)

with open('/var/www/SIGE_app/Datos.csv','r') as Datos:
    Datos_reader = csv.DictReader(Datos)
    
    for line in Datos_reader:

        if line['Fecha'] == tday:
            frecuencia = line['Freq']
            guarda_Frecuencia("1", frecuencia)

   

