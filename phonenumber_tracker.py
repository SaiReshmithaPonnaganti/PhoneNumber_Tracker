import phonenumbers
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse("+12566342354")
phone_number2 = phonenumbers.parse("+1 415-555-2671")
phone_number3 = phonenumbers.parse("+918907542354")
phone_number4 = phonenumbers.parse("+44 161 555 1234")
phone_number5 = phonenumbers.parse("+61 3 5550 5678")

print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phone_number1,"en"))
print(geocoder.description_for_number(phone_number2,"en"))
print(geocoder.description_for_number(phone_number3,"en"))
print(geocoder.description_for_number(phone_number4,"en"))
print(geocoder.description_for_number(phone_number5,"en"))

