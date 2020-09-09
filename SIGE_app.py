from flask import Flask, request, render_template
import time
import datetime
import sys
import Adafruit_DHT
import sqlite3

app = Flask(__name__)
app.debug = True # Make this False if you are no longer debugging

@app.route("/")
def SIGE_real_time():

        conn=sqlite3.connect('/var/www/SIGE_app/SIGE_app.db')
        curs=conn.cursor()
        curs.execute("SELECT * FROM consumo WHERE ROWID IN ( SELECT max( ROWID ) FROM consumo )");
        cons = curs.fetchall()
        curs.execute("SELECT * FROM generacion WHERE ROWID IN ( SELECT max( ROWID ) FROM generacion )");
        gen = curs.fetchall()
        curs.execute("SELECT * FROM cons1 WHERE ROWID IN ( SELECT max( ROWID ) FROM cons1 )");
        cons1 = curs.fetchall()
        curs.execute("SELECT * FROM cons2 WHERE ROWID IN ( SELECT max( ROWID ) FROM cons2 )");
        cons2 = curs.fetchall()
        curs.execute("SELECT * FROM cons3 WHERE ROWID IN ( SELECT max( ROWID ) FROM cons3 )");
        cons3 = curs.fetchall()
        curs.execute("SELECT * FROM vac WHERE ROWID IN ( SELECT max( ROWID ) FROM vac )");
        vac = curs.fetchall()
        curs.execute("SELECT * FROM vdc WHERE ROWID IN ( SELECT max( ROWID ) FROM vdc )");
        vdc = curs.fetchall()
        curs.execute("SELECT * FROM vbat WHERE ROWID IN ( SELECT max( ROWID ) FROM vbat )");
        vbat = curs.fetchall()
        curs.execute("SELECT * FROM frecuencia WHERE ROWID IN ( SELECT max( ROWID ) FROM frecuencia )");
        frec = curs.fetchall()

        conn.close()
        return render_template("SIGE_realT.html",cons=cons,gen=gen,cons1=cons1,cons2=cons2,cons3=cons3,vac=vac,vdc=vdc,vbat=vbat,frec=frec)

@app.route("/historico", methods=['GET']) 
def historico():
	temperatures, humidities, from_date_str, to_date_str = get_records()
	return render_template(	"SIGE_historico.html", 	temp 			= temperatures,
							hum 			= humidities,
							from_date 		= from_date_str, 
							to_date 		= to_date_str,
							temp_items 		= len(temperatures),
							hum_items 		= len(humidities))
	
def get_records():
	from_date_str 	= request.args.get('from',time.strftime("%Y-%m-%d 00:00")) #Get the from date value from the URL
	to_date_str 	= request.args.get('to',time.strftime("%Y-%m-%d %H:%M"))   #Get the to date value from the URL
	range_h_form	= request.args.get('range_h','');  #This will return a string, if field range_h exists in the request

	range_h_int 	= "nan"  #initialise this variable with not a number

	try: 
		range_h_int	= int(range_h_form)
	except:
		print ("range_h_form not a number")

	if not validate_date(from_date_str):			# Validate date before sending it to the DB
		from_date_str 	= time.strftime("%Y-%m-%d 00:00")
	if not validate_date(to_date_str):
		to_date_str 	= time.strftime("%Y-%m-%d %H:%M")		# Validate date before sending it to the DB

		# If range_h is defined, we don't need the from and to times
	if isinstance(range_h_int,int):	
		time_now		= datetime.datetime.now()
		time_from 		= time_now - datetime.timedelta(hours = range_h_int)
		time_to   		= time_now
		from_date_str   = time_from.strftime("%Y-%m-%d %H:%M")
		to_date_str	    = time_to.strftime("%Y-%m-%d %H:%M")
	
	conn=sqlite3.connect('/var/www/SIGE_app/SIGE_app.db')
	curs=conn.cursor()
	curs.execute("SELECT * FROM consumo WHERE rDateTime BETWEEN ? AND ?", (from_date_str, to_date_str))
	temperatures 	= curs.fetchall()
	curs.execute("SELECT * FROM generacion WHERE rDateTime BETWEEN ? AND ?", (from_date_str, to_date_str))
	humidities 		= curs.fetchall()
	conn.close()
	return [temperatures, humidities, from_date_str, to_date_str]

def validate_date(d):
    try:
        datetime.datetime.strptime(d, '%Y-%m-%d %H:%M')
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)
