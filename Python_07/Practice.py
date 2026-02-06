# import random

# # shuffle : changes in the original list, work only with the list type & it does return nothing.
# deck = ["A♠", "2♠", "3♠", "4♠"]
# result = random.shuffle(deck)
# print(deck)
# print(result)
# print('\n')


# # choice : deal with the list, tuple and string (iterabel, indexed) , it return a random value from the iterable (list...).
# deck = ["A♠", "2♠", "3♠", "4♠"]
# result = random.choice(deck)
# print(deck)
# print(result)
# print('\n')


# # randint: acept two args as int's only (from and to) and it return a random number btween does two int's and they are also included.
# result = random.randint(1, 2)
# print(result)
# print("\n")

# # enum : for easy understanding and naming.
# from enum import IntEnum


# class Colors(IntEnum):
#     read = 1
#     blue = 2

# print(type(Colors.blue))
# print(Colors.blue.name)
# choice = int(input("Which color you wnat ?\n\t1) read   2) blue\n"))


# match choice:
#     case Colors.read | Colors.blue:
#         print("Bouth")
#     case _:
#         print("Else")


from datetime import datetime
import time as tim

# today from datetime: 2026-02-06 08:24:54.289618
time = datetime.today()
print(time.date())


time = datetime.now()

print(time)
print(time.year)
print(time.month)
print(time.day)

start = tim.time()
end = tim.time()

print(tim.asctime())
print(end - start)