# Define the Book class
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Getter methods
    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_pages(self):
        return self.pages

    # Setter methods
    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_pages(self, pages):
        self.pages = pages

    # Class method to calculate reading time
    @classmethod
    def calculate_reading_time(cls, pages, reading_speed=250):
        words_per_page = 250  # Assuming an average of 250 words per page
        total_words = pages * words_per_page
        minutes = total_words / reading_speed
        return minutes


# Define the Ebook subclass inheriting from Book
class Ebook(Book):
    def __init__(self, title, author, pages, format):
        super().__init__(title, author, pages)
        self.format = format

    # Override __str__() method to display all attributes
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, Format: {self.format}"


# Example usage:
if __name__ == "__main__":
    # Create an instance of Book
    book1 = Book("Python Programming", "John Smith", 400)

    # Demonstrate getter and setter methods
    print("Before setting:")
    print(f"Title: {book1.get_title()}, Author: {book1.get_author()}, Pages: {book1.get_pages()}")

    book1.set_title("Learning Python")
    book1.set_author("Jane Doe")
    book1.set_pages(350)

    print("\nAfter setting:")
    print(f"Title: {book1.get_title()}, Author: {book1.get_author()}, Pages: {book1.get_pages()}")

    # Calculate reading time
    reading_time = Book.calculate_reading_time(book1.get_pages())
    print(f"\nEstimated reading time: {reading_time:.2f} minutes")

    # Create an instance of Ebook
    ebook1 = Ebook("Data Structures in Python", "Alice Johnson", 250, "PDF")
    print("\nEbook details:")
    print(ebook1)
