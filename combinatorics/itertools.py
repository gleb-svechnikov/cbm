import itertools
a1 = [1,2,3]
a2 = [4,5,6]
a3 = [7,8,9]

result = list(itertools.product(a1,a2,a3))
print (result)
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
