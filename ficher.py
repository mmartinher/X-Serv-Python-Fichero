#!/usr/bin/python
# -*- coding: utf-8 -*-

# Marina Martín Hernández
# Ejercicio 13.4:

fd = open('/etc/passwd','r')
data_list = fd.readlines()
dicc = {}

for line in data_list:
	element = line.split(':')
	user = element[0]
	aux = element[-1]
	shell = aux[0:-1]
	dicc[user] = shell
print dicc['root']
try:
	print dicc['imaginario']
except : 
	print ("\nUsuario Incorrecto")