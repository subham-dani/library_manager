# Library Manager

A small Python 3.12+ demonstration of abstract classes, inheritance, polymorphism, encapsulation, and exception handling for a campus library. Run it with `python3 main.py`.

## Reflection

### Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?
`LibraryItem` is abstract because it provides shared item behavior but does not define one universal late-fee rate. If `DVD` does not implement `late_fee()`, it remains abstract too, so attempting to create a `DVD` instance raises a `TypeError`.

### What happens when you read item.__available from outside the class, and why do we use is_available() instead?
Reading `item.__available` raises an `AttributeError` because Python name-mangles this private attribute. We use `is_available()` to check its value through a clear public interface without exposing the internal state.

### What is the difference between LibraryItem.total_items and self.title?
`LibraryItem.total_items` is a class attribute shared by every item and counts the items created. `self.title` is an instance attribute, so each item has its own title.
