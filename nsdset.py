import os
import time

def set():
	try:
		os.system('clear')
		print('''

Number Seperation and Differences set; classical division differences table.

''')
		n = int(input("Number: "))
		d = int(input("Difference: "))
		s = int(input("Seperation: "))
		try:
			f = n/s - ((d/2)+((d*s)/2)-d)
			print(f)
			for i in range(s-1):
				f += d
				print(f)
		except ZeroDivisionError:
			print("Sorry, Zero is Indenominable!")
			time.sleep(2)
			os.system('clear')
			set()

	except ValueError:
		print("Only number supported!")
		time.sleep(2)
		os.system('clear')
		set()

set()