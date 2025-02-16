# 3301-gematria
A simple Python script that calculates the Gematria values based on Cicada 3301's Gematria Primus.

# Requirements
This script requires Python 3.6 or higher. No additional libraries need to be installed.

# How To Run
1. **Open a terminal**
- On *Windows*, press *Win + R*, then type *"cmd"* and hit *Enter*.
- On Mac/Linus, open the Terminal application.

2. Navigate to the script's directory, e.g. where you saved it.
- If the file *gematria_calc.py* is located on your desktop, type the following command:
```
cd %UserProfile%\Desktop
```

3. Run the script.
```
python gematria_calc.py
```

# Usage
1. Run the script (for a detailed guide on how to do this, check **How To Run** above).
2. You will be prompted to enter a string of text. The script will add up values of each letter corresponding to 3301's Gematria Primus table and tell you whether the end result is a prime number or not
3. If you enter a character that isn't a part of the Gematria Primus (most commonly V), a warning will be shown, and the character will be substituted with the default value for U (3).
4. To exit the program, type 1234. The style of Cicada OS has been implemented as a cute little reference.

# Examples
### Example 1: Prime Checker returns a prime number.
```
LP Input: Cicada

Total: 157
Prime Checker: Congrats! The result is a prime number!
```

### Example 2: Prime Checker doesn't return a prime number.
```
LP Input: Example

Total: 465
Prime Checker: The result is not a prime number!
```

### Example 3: Invalid character detected in user input.
```
LP Input: Ex@mple

Warning: You have inputted a character that isn't present in 3301's Gematria Primus ('@')!
This character was substituted for U (Value = 3) instead.

Total: 371
Prime Checker: The result is not a prime number!
```

# Explanation
- The code includes a *is_prime(n):* function which checks if a given number *n* is prime.
- *mappings* include a list of latin characters as seen from the [Gematria Primus](https://uncovering-cicada.fandom.com/wiki/Gematria_Primus?file=Testout.jpg)
- *process_input(user_input)* processes the user's input by summing the corresponding Gematria values for each character. This is called a **gematria sum**, I'm just not referring to it that way.

If a character isn't in the *mappings* section, namely V, it's replaced with the value for **U (3)** - That is because these two letters are interchanged in the solved pages, similarly to letters like **C and K (which both have the value 13)** or **NG/ING (value 79)**.

This doesn't only work for V, but for any special character you input that doesn't appear in *mappings*. Double-check your input before you click Enter!

# Short FAQ For Newbies

### What Is Cicada 3301, Liber Primus, etc?
Cicada 3301 is a mysterious group that became known for posting complex puzzles online, starting in 2012. These puzzles challenged participants with cryptography & steganography. The group's ultimate purpose remains unclear, but as mentioned in the beginning of each puzzle, they mentioned looking for "highly intelligent individuals".

You can read more about Cicada 3301 on [The Uncovering Cicada Fandom](https://uncovering-cicada.fandom.com/wiki/Uncovering_Cicada_Wiki), which also includes attempts at solving Liber Primus, Cicada's latest unresolved puzzle from 2014.

### What Is Gematria?
Gematria is a numerological practice of assigning numerical values to letters. It is traditionally used in Kabbalistic and other esoteric texts. In this specific case, Cicada 3301 made their own specific form of Gematria where each letter and certain bigrams and trigrams have a corresponding prime number value.

### Why Are Primes So Important & What Are They?
Prime numbers are numbers such that they are only divisible by 1 and themselves *(examples include 2, 3, 5, 7, 11, ...)*. Prime numbers play a significant role in cryptography, and even more so in the context of Cicada 3301. They are difficult to factorize, which makes them an essential element of secure encryption algorithms like [RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem)).

### Does It Mean Anything If My Input Is Prime Or Not?
The correctness of your input isn't dependant on it being prime. While some lines out of the already decrypted Liber Primus text do result in prime number results, there are lines which do not posess this property. Ultimately, solving the puzzle is not solely about finding prime numbers, but understanding what Cicada 3301 wants to teach us.
