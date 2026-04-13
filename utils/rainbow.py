def rainbow_crack(target_hash,rainbow_file):

    with open(rainbow_file,"r") as f:

        for line in f:

            try:

                h,pw=line.strip().split(":")

                if h==target_hash:
                    return f"💥 Found in rainbow table: {pw}"

            except:
                continue

    return "❌ Not found in rainbow table"