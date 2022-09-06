# This is a program to store new vehicle inventory and assist with monthly payments
# Create variable of your favorite car brand
message='hyundai'
# Create list of 5 of their models from cheapest to most expensive
car_price= ['Hyundai Tucson','Hyundai Tucson Hybrid','Hyundai Santa Fe HEV', 'Hyundai Palisade' ,'Hyundai Santa Fe Plug-In Hybrid']
# Append a 6th model to the list
car_price.append('Hyundai NEXO')
# Create list of 5 standard colors for all models
car_colors = ['black', 'red', 'white', 'yellow', 'blue']
# Replace your last color with a different color
car_colors[4]='silver'
# Create variable of the current new year models
car_year= '2022'
# Create MSRP constant number (not string) of each of the models
Hyundai_Tucson= '26,450'
Hyundai_Tucson_Hybrid= '29,750'
Hyundai_Santa_Fe_HEV= '34,300'
Hyundai_Palisade='34,950'
Hyundai_NEXO= '59,435'
# Create a constant number (not string) for total months in 4yr, 5yr, and 6yr loans
four_yr='48 months'
five_yr='60 months'
six_yr= '72 months'
# Create a variable for the guest's name. Be courteous in your upcoming messages :)
r= 'Rhyan'
# Create message variable (with f-string) welcoming customer to your new car store
first_name= 'Rhyan'
last_name= "Armstead"
full_name= f'{first_name} {last_name}'
# Create awesome banner with your brand/name/dealership, however you want to welcome customers
banner='       _                       _\n'             \
       '      | |                     | |\n'            \
    ' ___  | |  __ _ _  __ __     _| |_    ____  ___ __\n'\
   '/ _ \ | | /  _` | | `_  \ \  |_ _ |  |   __/   _ ` | \n'\
   '| __/ | | | (_| | | | - | |   | |_   |   | |  (_|  | \n'\
   '\___  |_| \__,_ | |_|   |_| _ | _ |  |_  |  \ __ ,_|\n'
# Print awesome banner and welcome message
print(banner)
print('Welcome in to hyundai, Can i intrest you in a Elantra?')

# Using title methods, print the number vehicles in alphabetical order, with the year and available colors.
name0='hyundai santa fe Plug-In Hybrid,year 2021 in the color silver'
print(name0.title())
name1='hyundai santa fe HEV, year 2018 in the color red'
print(name1.title())
name2= 'hyundai tucson, year 2020 in the color white'
print(name2.title())
name3='hyundai tucson Hybrid, year 2022 in the color blue'
print(name3.title())
name4='hyundai palisade, year 2020 in the color yellow'
print(name4.title())
# Create a variable that calculates a monthly payment (no interest) for 5yr/60months for the first vehicle
m=60
price=26450
print(26450 / 60)
# and print that in a nice, kind message. Don't be rude/pushy to the customer :)
print('Your monthly payment for the Hyundai Tucson would be')
print(26450 / 60)
# Do the same thing, but give them 4yr and 6yr options for the same vehicle
fourty_eight_month= 48
fourty_eight_price=26450
print(26450/48)
seventy_two_month=72
sevent_two_price=26450
print(26450/72)
print(' I also included the four and the six year option for payment plans as well')

# Lastly, give them a 5yr option for each of the other vehicles, just to see if they are interested
ms=60
print('I also have calculated the prices of the remainder of the vehicles in case any of these intrested you as well. the first one is the tucson hybrid')
print(29750/60)
print('The next one I calculated for you is the Santa Fe Hev')
print(34300/60)
print('Next we have the Palisade')
print(34950/ms)
print('Lastly we have the Nexo')
print(59435/60)
#3 extra features
input("Mr. Armstead have you thought about any vehicle you may want to purchase today?")
print('thats amazing i can give you a list of what your monthly payments would be.')
Four_years=(34300/48)
Five_years=(34300/60)
Six_years=(34300/72)
finance_months= ['For 4 years your monthly payment would be $715','For 5 years you would be looking at $571','Lastly for 6 years you would be looking at $476']
print(finance_months)