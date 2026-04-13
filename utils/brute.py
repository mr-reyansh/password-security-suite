import hashlib
import itertools
import string

def brute_force_crack(target_hash, max_length=4):

    chars = string.ascii_lowercase + string.digits

    for length in range(1, max_length + 1):

        for attempt in itertools.product(chars, repeat=length):

            guess = ''.join(attempt)

            hashed = hashlib.sha256(guess.encode()).hexdigest()

            if hashed == target_hash:
                return f"💥 Password cracked: {guess}"

    return "❌ Password not cracked"