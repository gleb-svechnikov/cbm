import itertools
#Starmap
#x = itertools.starmap(pow, [(2,2), (3,3), (5,5), (7,7), (11,11), (13,13), (17,17)])
#print (list(x))
#-------------------------------------------------------------------#
#Завтрак:
#чай, кофе, какао, сок
#каша, яичница, тост с вареньем
#яблоко, груша
#
# drink  = ["чай", "кофе", "какао", "сок"]
# food    = ["каша", "яичница", "тост"]
# fruit  = ["яблоко", "груша"]
#
# breakfast = list(
#     itertools.product(drink, food, fruit)
# )
#
# print(breakfast, len(breakfast))

#Комбинации с перестановками
#Сколько 'слов' можно четрыхзначных составить из слова ШКОЛА
#-------------------------------------------------------------------#
# word = 'ШКОЛА'
# number_of_signs = 4 #number of signs
# x = itertools.combinations_with_replacement(word, number_of_signs)
# result = list(x)
# print (result, len(result))

#-------------------------------------------------------------------#
#Комбинации без повторяющихся элементов
#Сколькими способами можно рассадить 2 учеников по 8 партам что бы они не сидели рядом?

# y = itertools.combinations('ABCDEFGH', 2)
# print(list(y))
