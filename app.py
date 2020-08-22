# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import serial
import time

#ser = serial.Serial('/dev/ttyACM1', 9600)
ser = serial.Serial('/dev/arduino', 9600)
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/', methods=['POST'])
def post():
  arg = str(request.form.get('sel'))
  chname=''
  print('arg ===> '+ arg)
  argmsg = arg + ';'
  arg_byte=argmsg.encode('utf-8')
  ser.write(arg_byte)
  #ser.close()
  chname = 'Calling message ' + arg + ' ...'

  return render_template('index.html', message = chname)

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=5001)
