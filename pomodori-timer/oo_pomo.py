from time import sleep
from sys import argv
from os import system
from datetime import datetime
#make cfg, log, and maybe classes for timer and data
#not using either class yet
class pomo:
	def __init__(self):
		self.task = 'test'
		self.type = ['work' = False,'free'= Falsedd]
		self.work_minutes= int(0)
		self.free_minutes= int(0)
		self.ts = datetime.now()


def init_pomo():
	p = pomo() 

	p.task = input("Task? ")
	p.work_minutes = input("Work time? ")
	p.free_minutes= input("Free time? ")
	
	return p
de
def start_pomo(p):
	
	sleep_i = .25
def to_seconds(mins):
	return round(60+((_min - round(_min,0))*60))%60

def print_timer(mins):
	seconds = mins * 60
	for i in range(seconds):
		
		_ts = datetime.now()
		_min = (seconds - i)/60

		remaining_min = int(_min)
		remaining_sec = to_seconds(_min)
		if less_than_ten(remaining_min) == True and less_than_ten(remaining_sec) == True:
			countdown = '0'+str(remaining_min)+':0'+str(remaining_sec)
			
		elif less_than_ten(remaining_min) == True and less_than_ten(remaining_sec)== False:
			countdown = '0'+str(remaining_min)+':'+str(remaining_sec)

		elif less_than_ten(remaining_min) == False and less_than_ten(remaining_sec) == True:
			countdown = str(remaining_min)+':0'+str(remaining_sec)	

		elif less_than_ten(remaining_min) == False and less_than_ten(remaining_sec) == False:
			countdown = str(remaining_min)+':'+str(remaining_sec)
		print(name,'\t',i_ts,'\n',countdown)
		print('r_min',remaining_min)	
		print('r_sec',remaining_sec)	
		sleep(sleep_i)
		system('clear')
		#print_timer(minutes, name)

test = init_pomo()
print(test)
print(test.task, test.work_minutes, test.free_minutes)
start_pomo(test)

'''
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


'''
