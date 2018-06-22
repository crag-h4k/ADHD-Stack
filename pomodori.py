from time import sleep
from sys import argv
from os import system
from datetime import datetime
#make cfg, log, and maybe classes for timer and data
#not using these classes yet
class data:
	name = ''
	work_iters = int(0)
	break_iters = int(0)
	date = datetime.now()
class timer_obj:
	hours = 0
	minutes = 0
	seconds = 0

def log():
	return

def get_info():
	return

def print_timer():
	minutes = 2
	seconds = minutes * 60
	remaining_min = int(minutes)
	remaining_sec = int((minutes - round(minutes))*60)
	print(remaining_min,':',remaining_sec)
	

def alert():
	answer = input('work or break?')
	if answer == 'b':
		return False
	else:
		return True 
	
def print_timer(minutes, name):
	seconds = minutes * 60
	for i in range(seconds):
		_min = (seconds - i)/60
		remaining_min = int(_min)
		remaining_sec = round(60+((_min - round(_min,0))*60))%60
		print(name,'\n',remaining_min,':',remaining_sec)
	
		sleep(1.0)
		system('clear')

def pomo(work_time, break_time):
	#_work_time = int(work_time)	
	#_break_time = int(break_time)

	while True:
		print("starting pomo")
		print_timer(work_time,'pomo')
		end_of_pomo = alert()
		if end_of_pomo == True:
			continue
		else:
			rprint_timer(break_time,'break')
			end_of_pomo
			continue
def main():	
	'''
	print(int(argv[0]))
	print(int(argv[1]))
	
	_work = int(argv[0])
	_break = int(argv [1])
	'''
	_work = 10
	_break = 2
	pomo(_work,_break)
	
	#print_timer()
main()
