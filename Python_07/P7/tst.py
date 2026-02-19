# lst = {"card_1": {"rating": 0, "scor": 2}, "card_2": {"rating": 0, "scor": 1}}
# board = []

# for card_id, value in lst.items():
#     board.append(value)

# for i, bor in enumerate(board):
#     bor["rating"] = i + 1

# print(board)


ls = [{"item": 1}, {"item": 2}]

for i in ls:
    i["item"] += 1

print(ls)