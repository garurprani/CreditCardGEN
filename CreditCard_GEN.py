import requests
from colorama import Fore, Back, Style, init
from pyfiglet import Figlet

f = Figlet(font='slant')
print(f.renderText('CC GEN'))
print(Fore.MAGENTA + "> Generate random credit card details")
print(Fore.WHITE + "> scripted by @garurprani")
print(Fore.MAGENTA + "GitHub link: github.com/garurprani/CreditCardGEN")
print()

url= ("https://backend.lambdatest.com/api/dev-tools/credit-card-generator?")

def print_section(card_details, details):
    print(Fore.BLACK + Back.YELLOW + f'{ card_details }')
    for key, value in details.items():
        print(Fore.GREEN + f'{key}:' + Fore.WHITE + f'{ value}')

init(autoreset=True)
#how to add type=American%20Express or etc when user choice??
#ax = type=American%20Express
#mc = type=MasterCard
#vi = type=visa
#jc = type=jc
        
card_names = {
    'American Express' : 'ax',
    'Master Card' : 'mc',
    'Visa Card' : 'vi',
    'JCM' : 'jc'

}
print_section(' Card Names ',card_names)
which_type = input(Fore.BLACK + Back.CYAN + "-> Enter Card Type: ")

if "ax" in which_type:
    new_url = url + 'type=American%20Express&'
elif "mc" in which_type:
    new_url = url + 'type=MasterCard&'
elif "vi" in which_type:
    new_url = url + 'type=Visa&'
elif "jc" in which_type:
    new_url = url + 'type=JCB&'
else:
    print(Fore.RED + 'Wrong type')


#kitna cc chaiye

#will add this feature later
# num = input("Enter No. of Cards: ")
# latest_url = new_url+'no-of-cards='+num
# print(latest_url)


#sending request
responce = requests.get(new_url)
if responce.status_code == 200:
    print(Fore.BLACK + Back.GREEN + "-> Request Success ")

    data = responce.json()
    for card in data:
        type_details = card ['type']
        name_details = card ['name']
        num_details = card ['number']
        cvv_details = card ['cvv']
        expiry_details = card ['expiry']

    card_details = {
        'Type' : type_details,
        'Name' : name_details,
        'Number' : num_details,
        'CVV' : cvv_details,
        'Expiry date' : expiry_details
    }
    card_selected = " Card name: "+type_details+" "
    print()
    print_section(card_selected, card_details)
    while True: 
       pass  # Do nothing, just keep looping 

else:
    print("-> Request False")
