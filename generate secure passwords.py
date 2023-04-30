#python programe 3(generate secure passwords)
import string
import random

def generate_otp(length):
    if not isinstance(length, int) or length <= 0:
        raise ValueError("Length should be a positive integer")
        
    characters = string.digits + string.ascii_letters + string.punctuation
    otp = ''.join(random.choice(characters) for _ in range(length))
    return otp

if _name_ == "_main_":
    length = int(input("Enter length of OTP: "))
    otp = generate_otp(length)
    print("Your OTP is:", otp)