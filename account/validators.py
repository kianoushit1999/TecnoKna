from django.core.validators import RegexValidator
import re

def phone_validator():
    phone_re = RegexValidator(regex=r'^\+?1?\d{10,15}$',
                              message="Your phone number should be like this format +9999...")
    return phone_re

def pass_validator(password:str):
    if(re.search(r'^\w+$', password) is not None):
        return True
    else:
        return False