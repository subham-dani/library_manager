# main.py
from models import Book, DVD, Magazine, Member


book = Book("Python 101", 1, "A. Rao")
magazine = Magazine("Science Today", 2, 42)
dvd = DVD("Learning Python", 3, 120)
# An additional item lets the demo exercise Alice's three-item borrow limit.
extra_book = Book("Clean Code", 4, "Robert C. Martin")

alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)

# Borrowing, duplicate attempts, and friendly handling of invalid actions.
try:
    alice.borrow(book)
    print("Alice borrowed:", book.describe())
except ValueError as e:
    print("Could not borrow:", e)

try:
    alice.borrow(book)
except ValueError as e:
    print("Could not borrow:", e)

try:
    bob.borrow(book)
except ValueError as e:
    print("Could not borrow:", e)

# Fill Alice's allowance, then try to borrow a fourth item.
for item in (magazine, dvd):
    try:
        alice.borrow(item)
        print("Alice borrowed:", item.describe())
    except ValueError as e:
        print("Could not borrow:", e)

try:
    alice.borrow(extra_book)
except ValueError as e:
    print("Could not borrow:", e)

# Returning an item that belongs to another member is rejected.
try:
    bob.return_item(book)
except ValueError as e:
    print("Could not return:", e)

print("Alice's borrowed titles:", alice.borrowed_titles())

# Return a borrowed item and calculate its fee polymorphically.
try:
    fee = alice.return_item(book, days_late=3)
    print(f"Alice returned {book.title}; late fee: Rs {fee}")
except ValueError as e:
    print("Could not return:", e)
print("Book available after return:", book.is_available())

# Each item supplies its own late-fee rate; no type checks are needed here.
print("Late fees for 3 days:")
for item in (book, magazine, dvd):
    print(item.describe(), "-> Rs", item.late_fee(3))

# Private attributes are not accessed directly; use the public method instead.
try:
    print(book.__available)
except AttributeError:
    print("Direct access to book.__available raises AttributeError (it is private).")
print("Book availability via is_available():", book.is_available())

print("Total items created:", LibraryItem.total_items)
