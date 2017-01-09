import random
import os
import obj
import var


def create_life():
	var.life_list.append( obj.life(10, random.randrange(0,var.map_size), random.randrange(0,var.map_size)) )

def print_all_life_address():
	for i in range(len(var.life_list)):
		print var.life_list[i].show_x(), var.life_list[i].show_y()

def all_life_move_1():
	for i in range(len(var.life_list)):
		var.life_list[i].move(1)
		#print 'move ',i, var.life_list[i].show_x(), var.life_list[i].show_y()

def create_console_map():
	for i in range(var.map_size):
		var.console_map.append([])
		for j in range(var.map_size):
			var.console_map[i].append('   ')

def empty_console_map():
	for i in range(var.map_size):
		for j in range(var.map_size):
			var.console_map[i][j]='   '

def update_console_map():
	for i in range(len(var.life_list)):
		x=var.life_list[i].show_x()
		y=var.life_list[i].show_y()
		#print 'update ', i, x, y, '->', var.console_map[x][y], ' go'
		var.console_map[x][y]=' '+str(i)+' '


def print_map_on_console():
	for i in range(0,var.map_size):
		for j in range(0,var.map_size):
			print(var.console_map[i][j]),
		print
