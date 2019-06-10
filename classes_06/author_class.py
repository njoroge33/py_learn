# Define a class Author
# Ask for author's name, email id , and book name
# Then print out the name of author, email id, and book name
# for more info on this quiz, go to this url: http://www.programmr.com/author-class-0


class Author:
	def __init__(self, author_first_name, author_second_name, book_name):
		self.author_name = author_first_name + ' ' + author_second_name
		self.email_id = author_first_name + author_second_name + '@' + 'gmail.com'
		self.book_name = book_name


author_1 = Author("chimamanda", "ngozi", "purple hibiscus")

print(author_1.author_name)
print(author_1.email_id)
print(author_1.book_name)