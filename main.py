# 1-m
class Kitob:
    def __init__(self, a, b):
        self.name = a
        self.mualif = b


k1 = Kitob("O‘tkan kunlar", "Abdulla Qodiriy")
print(k1.name)
print(k1.mualif)


k2 = Kitob("Mehrobdan chayon", "Abdulla Qodiriy")
print(k1.name)
print(k1.mualif)


# 2-m
class Talaba:
    def __init__(self, i, b):
        self.name = i
        self.age = b


t1 = Talaba("Ali", 20)
print(t1.name)
print(t1.age)


t2 = Talaba("Vali", 22)
print(t1.name)
print(t1.age)


# 3-m
class Telefon:
    def __init__(self, m, n):
        self.telefon = m
        self.narx = n


t1 = Telefon("iPhone 13", 1200)
print(t1.telefon)
print(t1.narx)


t2 = Telefon("Samsung S21", 900)
print(t2.telefon)
print(t2.narx)


# 4-m
class Shahar:
    def __init__(self, a, b):
        self.name = a
        self.people = b


t1 = Shahar("Toshkent", 3000000)
print(t1.name)
print(t1.people)


t2 = Shahar( "Samarqand", 600000)
print(t1.name)
print(t1.people)

#
# 5-m
class Mashina:
    def __init__(self, m, r):
        self.marka = m
        self.rang = r

t1 = Mashina("Cobalt", "oq")
print(t1.marka)
print(t1.rang)


t2 = Mashina("Malibu", "qora")
print(t2.marka)
print(t2.rang)

t3 = Mashina("Nexia", "kulrang")
print(t3.marka)
print(t3.rang)

