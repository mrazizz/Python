import random

frequencies = [0, 0, 0, 0, 0, 0]

for i in range(1, 101):
    face = random.randint(1, 6)
    frequencies[face - 1] = frequencies[face - 1] + 1

print("Face\tFrequency")

for i in range(1, 7):
    print(f"{i}:\t{frequencies[i - 1]}")

print(f"Total:\t{sum(frequencies)}")