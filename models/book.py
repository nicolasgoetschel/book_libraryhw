class Book():

    def __init__(self, title, pages, genre, read = False, id = None):
        self.title = title
        self.pages = pages
        self.genre = genre
        self.read = read
        self.id = id

    def mark_read(self):
        self.read = True