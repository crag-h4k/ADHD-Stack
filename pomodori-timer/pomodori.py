from time import sleep
from sys import argv
from os import system
from datetime import datetime
#make cfg, log, and maybe classes for timer and data
#not using either class yet
class pomo:
	name = ''
	work_iters = int(0)
	break_iters = int(0)
	date = datetime.now()

class timer:
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

def less_than_ten(x):
	if x < 10:
		return True
	else:
		return False

def print_timer(minutes, name):
	sleep_i = .25
	seconds = minutes * 60
	
	for i in range(seconds):
		ts = datetime.now()
		_min = (seconds - i)/60

		remaining_min = int(_min)
		remaining_sec = round(60+((_min - round(_min,0))*60))%60

		if less_than_ten(remaining_min) == True and less_than_ten(remaining_sec) == True:
			countdown = '0'+str(remaining_min)+':0'+str(remaining_sec)
			
		elif less_than_ten(remaining_min) == True and less_than_ten(remaining_sec)== True:
			countdown = str(remaining_min)+':0'+str(remaining_sec)	elif less_than_ten(remaining_min) == False and less_than_ten(remaining_sec)== True:
			countdown = str(remaining_min)+':0'+str(remaining_sec)

		elif less_than_ten(remaining_min) == False and less_than_ten(remaining_sec) == False:
			co		elif less_than_ten(remaining_min) == False and less_than_ten(remaining_sec)== True:
			countdown = str(remaining_min)+':0'+str(remaining_sec)untdown = str(remaining_min)+':'+str(remaining_sec)

		print(name,'\t',ts,'\n',countdown)
		print('r_min',remaining_min)	
		print('r_sec',remaining_sec)	
		sleep(sleep_i)
		system('clear')
		#print_timer(minutes, name)

def start_pomo(work_time, break_time):
	#_work_time = int(work_time)	
	#_break_time = int(break_time)

#while True:
	print("starting pomo")
	print_timer(work_time,'pomo')
	end_of_pomo = alert()
	if end_of_pomo == True:
		print_timer(work_time,'pomo')
	else:
		print_timer(break_time,'break')

def main():	
	'''
	print(int(argv[0]))
	print(int(argv[1]))
	
	_work = int(argv[0])
	_break = int(argv [1])
	'''
	_work = 10
	_break = 2
	start_pomo(_work,_break)
	
	#print_timer()
main()
