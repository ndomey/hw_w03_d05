from models.book import Book

book1 = Book("1984", "George Orwell", "Political & Social Sci-fi", "To Winston Smith, a young man who works in the Ministry of Truth (Minitru for short), come two people who transform this life completely. One is Julia, whom he meets after she hands him a slip reading, 'I love you.' The other is O'Brien, who tells him, 'We shall meet in the place where there is no darkness.' The way in which Winston is betrayed by the one and, against his own desires and instincts, ultimately betrays the other, makes a story of mounting drama and suspense.")
book2 = Book("One Hundred Years of Solitude", "Gabriel García Márquez", "Magic realism", "The story of seven generations of the Buendía family and of Macondo and the town they built. Though little more than a settlement surrounded by mountains, Macondo has its wars and disasters, even its wonders and its miracles. A microcosm of Columbian life, its secrets lie hidden, encoded in a book, and only Aureliano Buendía can fathom its mysteries and reveal its shrouded destiny.")
book3 = Book("Little Prince", "Antoine de Saint-Exupéry", "Fabel, Fantasy", "After crash-landing in the Sahara Desert, a pilot encounters a little prince who is visiting Earth from his own planet. Their strange and moving meeting illuminates for the aviator many of life's universal truths, as he comes to learn what it means to be human from a child who is not.")
book4 = Book("The Alchemist", "Paulo Coelho", "Adventure, Fantasy", "Story of Santiago, an Andalusian shepherd boy who yearns to travel in search of a worldly treasure. His quest will lead him to riches far different—and far more satisfying—than he ever imagined. Santiago's journey teaches us about the essential wisdom of listening to our hearts, recognizing opportunity and learning to read the omens strewn along life's path, and, most importantly, following our dreams.")
book5 = Book("Master and Margarita", "Mikhail Bulgakov", "Novel", "The Master and Margarita became an overnight literary phenomenon when it was finally published it, signalling artistic freedom for Russians everywhere. Bulgakov's carnivalesque satire of Soviet life describes how the Devil, trailing fire and chaos in his wake, weaves himself out of the shadows and into Moscow one Spring afternoon. Brimming with magic and incident, it is full of imaginary, historical, terrifying and wonderful characters, from witches, poets and Biblical tyrants to the beautiful, courageous Margarita, who will do anything to save the imprisoned writer she loves.")
book6 = Book("Ocean at The End of Lane", "Neil Gaiman", "Fantasy Fiction", "A middle-aged man returns to his childhood home to attend a funeral. Although the house he lived in is long gone, he is drawn to the farm at the end of the road, where, when he was seven, he encountered a most remarkable girl, Lettie Hempstock, and her mother and grandmother. He hasn't thought of Lettie in decades, and yet as he sits by the pond (a pond that she'd claimed was an ocean) behind the ramshackle old farmhouse, the unremembered past comes flooding back. And it is a past too strange, too frightening, too dangerous to have happened to anyone, let alone a small boy.")

books = [book1, book2, book3, book4, book5, book6]

def add_new_book(book):

    books.append(book)


#remove book by index number
def remove_book(index):
    
    for book in books:
        if books.index(book) == int(index):
            books.pop(int(index))



#remove book by title
# def remove_book_by_title(book_title):
#     book_to_delete = None
#     for book in books:
#         if book.title == book_title:
#             book_to_delete = book
#             break
#     books.remove(book_to_delete)



    
    