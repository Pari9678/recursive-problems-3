def tower_of_hanoi(disks, source, helper, destination):
    if disks == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(disks - 1, source, destination, helper)
    print(f"Move disk {disks} from {source} to {destination}")
    tower_of_hanoi(disks - 1, helper, source, destination)
 
keypad = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

def generate_words(digits, current_word=""):
    if len(digits) == 0:
        print(current_word)
        return
    first_digit = digits[0]
    if first_digit not in keypad:
        generate_words(digits[1:], current_word)
        return
    for letter in keypad[first_digit]:
        generate_words(digits[1:], current_word + letter)

def trace_words(digits, current_word="", level=0):
    indent = "  " * level
    if len(digits) == 0:
        print(indent + "Completed: " + current_word)
        return
    first_digit = digits[0]
    print(indent + f"Digit: {first_digit}, Word: {current_word}")
    if first_digit not in keypad:
        trace_words(digits[1:], current_word, level + 1)
        return
    for letter in keypad[first_digit]:
        trace_words(digits[1:], current_word + letter, level + 1)

print("Tower of Hanoi")
tower_of_hanoi(3, "A", "B", "C")
print("\nKeypad words for 23")
generate_words("23")
print("\nRecursion tree for 23")
trace_words("23")