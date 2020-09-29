import os
import time


class GtFileStats:
	
	'Class to simplfy file stats'

	# MAC - Return date created in yyyy_mm_dd
	
	def mac_date_created(pth):

		'Given a path as a string, return date created in yyyy_mm_dd'
		
		stats = os.stat(pth)
		return time.strftime('%Y_%m_%d', time.gmtime(stats.st_birthtime))


	# Windows - Return date created in yyyy_mm_dd
	
	def windows_date_created(pth):

		'Given a path as a string, return date created in yyyy_mm_dd'

		stats = os.stat(pth)
		return time.strftime('%Y_%m_%d', time.gmtime(stats.st_ctime))