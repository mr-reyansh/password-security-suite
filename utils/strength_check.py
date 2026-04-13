import math
import string

def check_strength(password):

    charset=0

    if any(c.islower() for c in password):
        charset+=26

    if any(c.isupper() for c in password):
        charset+=26

    if any(c.isdigit() for c in password):
        charset+=10

    if any(c in string.punctuation for c in password):
        charset+=32

    entropy=len(password)*math.log2(charset) if charset else 0

    if entropy<28:
        return "Weak 😬"

    elif entropy<36:
        return "Medium 🔐"

    else:
        return "Strong 💪"