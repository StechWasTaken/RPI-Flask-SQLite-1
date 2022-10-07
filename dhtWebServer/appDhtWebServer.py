#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  appDhtWebServer.py
#  
#  Created by MJRoBot.org 
#  10Jan18

'''
	RPi Web Server for BME280 captured data  
'''

from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Retrieve data from database
def getData():
	conn=sqlite3.connect('../../sensorsData.db')
	curs=conn.cursor()
	for row in curs.execute("SELECT * FROM BME_data ORDER BY timestamp DESC LIMIT 1"):
		time = str(row[0])
		temp = row[1]
		hum = row[2]
		pres = row[3]
	conn.close()
	return time, temp, hum, pres

# main route 
@app.route("/")
def index():
	time, temp, hum, pres = getData()
	templateData = {
	  'time'	: time,
      'temp'	: temp,
      'hum'		: hum,
	  'pres'	: pres,
	}
	return render_template('index_gage.html', **templateData)


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)

