import random
from datetime import *


def random_time(date, hours=23, minutes=59):

	hours = random.randint(0,hours)
	minutes = random.randint(0,minutes)

	return date + timedelta(hours=hours, minutes=minutes)
