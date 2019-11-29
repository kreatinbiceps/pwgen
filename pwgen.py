import random
import string


def randomString(stringLength, specialchar_yesno):
	letters = string.ascii_lowercase + string.ascii_uppercase
	number = string.digits
	if specialchar_yesno == "y":
		specialchar = string.punctuation
	elif specialchar_yesno == "n":
		specialchar = ""
	return ''.join(random.choice(letters+number+specialchar) for i in range (stringLength))




a=1
while a==1:
	value = False
	specialchar_yesno = ""
	try:
		stringLength = int(input("How long pw?: "))
		specialchar_yesno = input("Special chars? (y/n): ")


	except ValueError:
		print("Try Again...")
		value = True


	try:
		if specialchar_yesno == "y" or "n":

			print(randomString(stringLength, specialchar_yesno))
			break

		elif value == False:
			print("Try Again...")
	except:
		if value == False:
			print("Try Again...")
