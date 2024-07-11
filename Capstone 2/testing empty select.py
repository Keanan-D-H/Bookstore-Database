
import sqlite3

# Class Definitions

class Book():
    """
    A class to represent a Book.

    Attributes
    __________
    id : str
        The given id of this book. 
    title : str
        The title of the book. 
    author : str
        The name of the book's author.
    quantity : int
        The number of this book which is in stock, given a default of 1.
    
    Methods
    _______
    change_quantity (difference, plus_minus)
        differnce : int
            How much the quantity is changing by.
        
    """
    
    def __init__(self, id, title, author, quantity = 1):

        self.id = id
        self.title = title
        self.author = author
        self.quantity = quantity 

    def change_quantity(self, difference): 
        self.quantity = self.quantity + difference
    

# Function Definitions

def check_yes_no(answer):
    """
    check_yes_no(answer)

    Checks if the inputted string is either a yes or a no and asks for an
    input until it is then returns the result.

    Arg:
        answer (str) : a string

    Returns: 
        str: either "yes" or "no"        
    """
    while answer.lower() !='yes' and answer.lower() != 'no':
        answer = input ('Please only put in \'yes\' or \'no\':\n')
    return answer.lower()


def positive_integer(item): 
    """
    check_integer tries to change an input to an int, if it can't it will
    ask for input until it can
    Parameters: item : str
    Returns the item as an int   
    """
    while type(item) != int:
        try:
            item = int(item)

            if item < 0:
                item = input("Please input a positive number.\n")

        except:  
            item = input("That is not an integer , please input again.\n")
    return item


def correct_string(info):
    """
    correct_string(info)

    Checks with the user if the information they have inputted is correct.
    If the information was not correct it will ask the user to input
    the information correctly until the input is what the user desired. 

    Arg:
        info (str): a user inputted string 

    Returns:
        info (str): a user inputted string which the user is confident
                    is correct.  
    """

    while True:
        answer = check_yes_no(input(f"\nYou inputted \'{info}\'."
                                     + " Is this correct?\n"))
        
        if answer == 'yes':
            return info
        
        else:
            info = input('Please re-enter the correct information.\n')



# Connect to a database called 'ebookstore' 
db = sqlite3.connect('ebookstore')
cursor = db.cursor()


# If a table called 'book' in 'ebookstore' exists then drop the table
cursor.execute('''
               DROP TABLE IF EXISTS book; 
               ''')
db.commit()


# Create a table called 'book' in 'ebookstore' 
cursor.execute('''
               CREATE TABLE book (id INTEGER PRIMARY KEY, title TEXT,
               author TEXT, qty INTEGER)
               ''')
db.commit()


# Creating books to populate the database. 
book3001 = Book(3001, 'A Tale of Two Cities', 'Charles Dickens', 30 )
book3002 = Book( 3002, 'Harry Potter and the Philosepher\'s Stone', 
                'J. K. Rowling', 40)
book3003 = Book(3003, 'The Lion, The Witch and the Wardrobe', 
                'C. S. Lewis', 25)
book3004 = Book(3004, 'The Lord of the Rings', 'J. R. R. Tolkien', 37)
book3005 = Book(3005, 'Alice in Wonderland', 'Lewis Carroll', 12)


# Placing the books into a list so they can be easily added to the database.
pop_library = [book3001, book3002, book3003, book3004, book3005]
library_info = []


# Adding each books (id, title, author, quantity) to the list library_info.
for i in pop_library:
    library_info.append((i.id, i.title, i.author, i.quantity))


# Inserting the books into the 'book' table.
cursor.executemany('''INSERT INTO book(id, title, author, qty)
                   VALUES (?,?,?,?)''', library_info)
db.commit()

cursor.execute(''' 
                SELECT * FROM book WHERE title = (?) AND author = (?)'''
               , ('John', 'JIM'))
db.commit()
jim = cursor.fetchone()
print(jim)

'''
new_title = correct_string(input("\nWhat is the title of the book?\n"))
new_author = correct_string(input("\nWhat is the name of the author?\n"))


        # Check if there is already a record in 'book' which has this title 
        # and author. 
cursor.execute(''''''
                SELECT * FROM book WHERE title = (?) 
                AND author = (?)'''''', 
                (new_title, new_author))
db.commit() 
find_title_author = cursor.fetchone()
print(find_title_author)

if find_title_author != []:
    print(f"{new_title} by {new_author} is already in our" + 
            "database. \nIf you wish to update this book please" +
            " choose the update option from the menu.\n")
    #continue
            
        # Defining find_id as 
find_id = [0]


while find_id !=[] :
    new_id = input('\nPlease enter the ID for ' +
                                f"{new_title} by {new_author}.\n")
    new_id =  positive_integer(new_id)


    cursor.execute(''''''
                    SELECT * FROM book WHERE id =(?) '''''', 
                    (new_id))
    db.commit()
    find_id = cursor.fetchone()
                
    if find_id != [] : 
        print (f"\'{new_id}\' is the ID for " +
                f"{find_id[1]} by {find_id[2].strip('\'')}")
               
            
    new_qty = positive_integer(input("How many copies of " + 
                    f"\'{new_title}\' by {new_author} are there?\n"))
                        

cursor.execute('''''' 
                INSERT INTO book(id, title, author, qty)
                VALUES (?,?,?,?)''''''
                ,(new_id, new_title, new_author, new_qty))
db.commit()'''