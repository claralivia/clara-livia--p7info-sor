#!/usr/bin/python
import cgitb, cgi
cgitb.enable()

form = cgi.FieldStorage()

valorDigitado = int(form.getvalue('value')) 


print("Content-Type:text/html\r\n\r\n")
print("Hello, ", valorDigitado)