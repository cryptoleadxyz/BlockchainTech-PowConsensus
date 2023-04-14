# Author: CryptoLead at https://www.cryptolead.xyz
# Date: 2023-01-17
# Message: Hey there fellow coders! If you found my code helpful and want to show your support, consider buying me a coffee or two. Your donations help me keep improving the code and creating more awesome stuff for the community. Thanks for your support!
# Donation: cryptolead.eth or 0xa2c35DA418f52ed89Ba18d51DbA314EB1dc396d0

import hashlib
import time

# Control panel
difficulty = 4
print_switch = False


def proof_of_work(block_data, difficulty):
    target = "0" * difficulty
    if print_switch:
        print("target:", target)
    for i in range(100000000):
        test_nonce = str(i)
        hash_input_data = block_data + test_nonce
        hash_result = hashlib.sha256(hash_input_data.encode()).hexdigest()
        if print_switch:
            print(
                "||test nonce:",
                test_nonce,
                "||hash input data:",
                hash_input_data,
                "||hash value:",
                hash_result,
            )
        if hash_result[:difficulty] == target:
            return test_nonce
    return None


block_data = "Liza sends 5 BTC to Joe"
start_time = time.time()
nonce = proof_of_work(block_data, difficulty)
end_time = time.time()

print("Block:", block_data)
print("Matched nonce:", nonce)
print("Time taken:", end_time - start_time, "seconds")
