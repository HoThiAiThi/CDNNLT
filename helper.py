# def n_max_number(n, k=2):
#     n.sort()
#     list_n_max_number = n[-k:]
#     return list_n_max_number

# def n_min_number(n, k=2):
#     n.sort()
#     list_n_min_number = n[:k]
#     return list_n_min_number

from config.constant import *
print(person1["name"])
print(person1["age"])
print(person1["country"])

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

# Tạo một đối tượng Rectangle với chiều dài 5 và chiều rộng 3
my_rectangle = Rectangle(5, 3)

# Sử dụng phương thức để tính diện tích và chu vi
area = my_rectangle.calculate_area()
perimeter = my_rectangle.calculate_perimeter()

print("Diện tích của hình chữ nhật là:", area)
print("Chu vi của hình chữ nhật là:", perimeter)



import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)

class Deck:
    def __init__(self):
        suits = ['Heart', 'Diamond', 'Club', 'Spade']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        if not self.is_empty():
            return self.cards.pop()
        else:
            return None

    def is_empty(self):
        return len(self.cards) == 0

# Tạo một bộ bài
deck = Deck()

# Trước khi xáo bài
print("Bộ bài ban đầu:")
for card in deck.cards:
    print(card)

# Xáo bài
deck.shuffle()
print("\nBộ bài sau khi xáo:")
for card in deck.cards:
    print(card)

# Loại ra một lá bài khỏi bộ bài
drawn_card = deck.draw_card()
if drawn_card:
    print("\nLá bài đã loại ra:", drawn_card)
else:
    print("\nKhông còn lá bài trong bộ bài.")

# Kiểm tra xem bộ bài còn trống hay không
if deck.is_empty():
    print("Bộ bài đã rỗng.")
else:
    print("Bộ bài còn chứa các lá bài.")