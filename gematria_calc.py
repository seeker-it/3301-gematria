import time

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes_until(limit):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    first_prime = True
    for num in range(2, limit + 1):
        if is_prime(num):
            if first_prime:
                print(num, end="")
                first_prime = False
            else:
                print(" ", num, end="", flush=True)
            if num == 1033:
                time.sleep(3)
            time.sleep(0.03)

mappings = {
    "F": 2, "U": 3, "TH": 5, "O": 7, "R": 11, "C": 13, "K": 13, "G": 17, "W": 19, "H": 23, 
    "N": 29, "I": 31, "J": 37, "EO": 41, "P": 43, "X": 47, "S": 53, "Z": 53, "T": 59, "B": 61,
    "E": 67, "M": 71, "L": 73, "NG": 79, "ING": 79, "OE": 83, "D": 89, "A": 97, "AE": 101, 
    "Y": 103, "IA": 107, "IO": 107, "EA": 109, " ": 0
}

def process_input(user_input):
    total_sum = 0
    i = 0
    warning_displayed = False
    while i < len(user_input):
        if i + 2 <= len(user_input) and user_input[i:i + 3].upper() in mappings:
            trigram = user_input[i:i + 3].upper()
            total_sum += mappings[trigram]
            i += 3
        elif i + 1 <= len(user_input) and user_input[i:i + 2].upper() in mappings:
            bigram = user_input[i:i + 2].upper()
            total_sum += mappings[bigram]
            i += 2
        elif user_input[i].upper() in mappings:
            letter = user_input[i].upper()
            total_sum += mappings[letter]
            i += 1
        else:
            if not warning_displayed:
                print(f"")
                print(f"Warning: You have inputted a character that isn't present in 3301's Gematria Primus ('{user_input[i]}')!")
                print(f"This character was substituted for U (Value = 3) instead.")
                warning_displayed = True
            total_sum += 3
            i += 1
    is_total_prime = is_prime(total_sum)
    return total_sum, is_total_prime

def main():
    while True:
        user_input = input("\nLP Input: (or type '1234' to quit): ").strip()
        if user_input.lower() == '1234':
            print("Like the instar tunneling to the surface. We must shed our own circumferences. Find the divinity within and emerge:")
            print_primes_until(3301)
            break
        total_sum, is_total_prime = process_input(user_input)
        print(f"\nTotal: {total_sum}")
        print(f"Prime Checker: {'Congrats! The result is a prime number!' if is_total_prime else 'The result is not a prime number!'}")
        print(f"---------------------------------------------------------------------------------------------------------------------")

if __name__ == "__main__":
    main()