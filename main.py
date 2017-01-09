import os
import obj
import random
import func
import var
import time


def main():
	func.create_console_map()	
	
	func.create_life()
	func.create_life()
	func.create_life()

	for i in range(1000):
		func.empty_console_map()
		func.update_console_map()

		func.print_map_on_console()

		func.all_life_move_1()
		print
		#time.sleep(0.1)

		os.system('cls')



if __name__ == '__main__':
	main()


