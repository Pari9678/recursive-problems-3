def hanoi(n):
    if n == 0:
        return 0
    return 2 * hanoi(n - 1) + 1

input("hanoi (n) counts the minimum moves to shift n desks from peg. press enter")
print(" hanoi(1) =", hanoi(1))
print(" hanoi(2) =", hanoi(2))

n = int(input("Enter a number: "))
guess = input("What is hanoi(" + str(n) + ")? ")
input(" hanoi(n) = 2 * hanoi(n - 1) + 1 move stack twice plus the big disk once. press enter ")
print(" hanoi(" + str(n) + ") =", hanoi(n), " your guess:", guess)