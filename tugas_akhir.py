import random

def randnumber():
	print("Tebak angka antara 1 sd 100")
	number = random.randint(1,100)
	return number

def userinput():
	putar = True
	while putar:
		guest = input("Masukkan angka tebakan: ")
		try:
	   		number = int(guest)
		except ValueError:
		    print("Input harus berupa angka")
		else:
		    return int(guest)
		    putar = False
