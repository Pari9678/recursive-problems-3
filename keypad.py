keys = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "2" : "wxyz"}
def count_combos(digits):
    if len(digits) == 0:
        return 1
    return len(keys[digits[0]]) * count_combos(digits[1:])

input("count_combos multiplies  letter choices at each digit - 3 letters per stop. press enter ")
print(" count_combos(2) =", count_combos('2'))
print(" count_combos(23) =", count_combos('23'))

d = input("Enter digits 2 to 9: ")
guess = input("What is count_combos(" + d + ")? ")
input("count_combos = choices at digit 0 x count_combos of the the rest. press enter ")
print(" count_combos(" + d + ") =", count_combos(d), " your guess:", guess)