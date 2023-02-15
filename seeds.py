import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author_1 = Author("Stephen", "King")
book_repository.save(author_1)
author_2 = Author("Franz", "Kafka")
author_repository.save(author_2)

author_repository.select_all()

book_1 = Book("The Shining", 100, author_1, "Gothic Novel", True, author_1)
book_repository.save(book_1)

book_2 = Book("The Stoker", 101, author_2, "Fiction", False, author_2)
book_repository.save(book_2)


pdb.set_trace()