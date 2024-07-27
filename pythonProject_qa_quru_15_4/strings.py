# СТРОКИ

s = "hell'o, w'o'rld"

s = 'hel"lo, wor"ld'

s = "hello,\" world"

s = 'hello,\' world'

s = """hello,"'"''"'" world"""

print("---------")

# ПЕРЕНОС СТРОК

s = '''he
llo,
'' wo
rld'''

print(s)
print("---------")

s = 'hello, \nworld!'

print(s)
print("---------")

s = """hello,
 wordl"""

print(s)
print("---------")

s = "hello, " \
    "world!"

print(s)
print("---------")

#СЫРЫЕ СТРОКИ

s = 'hello, \\nworld'

print(s)
print("---------")


s = r'hello, \nworld'

print(s)
print("---------")

# ИНДЕКСЫ И СЛАЙС

email = "user@damain.com"

#Индексация всегда начинается с 0
print(email[0])
print(email[1])
print(email[2])
print(email[3])
print(email[-3])
print(email[-2])
print(email[-1])
print("---------")

print(email[0:5]) # Выбор диапазона
print("---------")

print(email[:5]) # Можно не указывать 0, а просто поставить :, тогда он сам будет счатить с нуля, потому что по умолчанию и так будет нулём
print("---------")

print(email[0:15:2])# Третье число означает шаг, с котоым мы идём по строке и берём символы
print(email[0:15:1])
print("---------")

print(email[::-1]) #Мы развернули задом на переём, если брать весь диапазон, то можно не указывать 0 и конечное число
print("---------")

# ОПЕРИРУЕМ

