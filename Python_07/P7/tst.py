def hi(dic: dict, card):
    if card in dic.keys():
        dic[card] += [card]
    else:
        dic[card] = [card]

dic: dict = {"creature": []}

hi(dic, "creature")
hi(dic, "creature")
hi(dic, "creature")
hi(dic, "creature")
hi(dic, "spell")
hi(dic, "spell")
hi(dic, "spell")
hi(dic, "spell")

print(dic)