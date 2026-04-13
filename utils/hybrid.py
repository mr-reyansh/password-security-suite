import hashlib

def hybrid_crack(target_hash, wordlist_path):

    suffixes = ["123","1","!","@","2024"]

    with open(wordlist_path,"r") as f:
        words=[line.strip() for line in f]

    for word in words:

        for suffix in suffixes:

            guesses=[
                word+suffix,
                word.capitalize()+suffix,
                word.upper()+suffix
            ]

            for guess in guesses:

                hashed=hashlib.sha256(guess.encode()).hexdigest()

                if hashed==target_hash:
                    return f"💥 Cracked Password: {guess}"

    return "❌ Password not cracked"