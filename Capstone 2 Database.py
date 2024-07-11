#*****Capstone 2 Database.py*****
# Keanan Hinchliffe 02/07/2024
"""
A program which creates a table called 'book' in a database called 
'ebookstore'. 

The program allows the user to add new books to the 'book' table, update
entries, delete entries, and search the database for individual books. 

"""

# Imports 

import sqlite3


# Function Definitions

def check_yes_no(answer):
    """
    check_yes_no(answer)

    Checks if the inputted string is either a yes or a no and asks for an
    input until it is then returns the result.

    Arguments:
        answer (str) : a string

    Returns: 
        str: either "yes" or "no"        
    """
    while answer.lower() !='yes' and answer.lower() != 'no':
        answer = input ('\nPlease only put in \'yes\' or \'no\':\n')
    return answer.lower()


def positive_integer(item, update): 
    """
    check_integer tries to change an input to an int, if it can't it will
    ask for input until it can. If this is to be used in the update part 
    of the code an empty string is allowed for item.

    Arguments: 
            item : str
                A string which should be an integer.
            update : int
                Either 0 or 1 to determine whether an empty string should
                be allowed. If update == 0, item == "" is not allowed,
                but if update == 1, item can be "".

    Returns:    item : int or str
                   
    """
    if update == 0:
        while type(item) != int:
            try:
                item = int(item)

                if item < 0:
                    item = input("\nPlease input a positive number.\n")

            except:  
                item = input("\nThat is not an integer , please input again.\n")
        return item

    else:
        while type(item) != int and item != "":
            try:
                item = int(item)

                if item < 0:
                    item = input("\nPlease input a positive number.\n")

            except:  
                item = input("\nThat is not an integer , please input again.\n")
        return item


def correct_string(info, update):
    """
    correct_string(info)

    Checks with the user if the information they have inputted is correct.
    If the information was not correct it will ask the user to input
    the information correctly until the input is what the user desired.
    If update == 1 and info == "" then the user will not be prompted 
    to confirm if the input is correct.  

    Arguments:
        info : str
            A user inputted string.
        update : int
            Either 1 or 0. A value of 1 should be used during the update
            section of the code in order to allow an input of info = ""
            to skip the check. If update == 0 then the function runs with
            the check.         
        
    Returns:
        info : str
            A user inputted string which the user is confident
            is correct.  
    """

    while True:

        if update == 1 and info == "" : 
            return info
        
        else: 
            answer = check_yes_no(input(f"\nYou inputted \'{info}\'."
                                        + " Is this correct?\n"))
        
            if answer == 'yes':
                return info
            
            else:
                info = input('\nPlease re-enter the correct information.\n')


def search_by_id(id):
    """
    search_by_id searches the 'book' table for a record with a certain ID.
    
    Arguments:  
            id : int 
                The ID number of the book to be searched for


    Returns:    
            id_record : list / NoneType
                The record of the book with the ID provided or 
                None if there is no record with the ID 
    """

    cursor.execute('''
                                SELECT * FROM book WHERE id = (?) ''', 
                                (id,))
    db.commit()

    id_record = cursor.fetchone()
    return id_record 


def search_by_author_title(author, title):
    """
    search_by_author_title searches the 'book' table for a record
    with the title and author name equal to the Arguments.
    
    Arguments:  
            author : str 
                The name of the author of the book being searched for.
            title : str
                The title of the book being searched for.


    Returns:    
            id_record : list / NoneType
                The record of the book with the Arguments provided or 
                None if there is no record with these Arguments. 
    """

    cursor.execute('''
                            SELECT * FROM book WHERE title = (?) 
                            AND author = (?)''', 
                            (title, author))
    db.commit() 

    author_title_record = cursor.fetchone()
    return author_title_record


def display_book(id, title, author, qty):
    """
    display_book displays the information of a book's record to the user.
    
    Arguments: 
            id : int
                The book's ID.
            title : str
                The title of the book.
            author : str
                The book's author.
            qty : int
                The quantity of books. 
    
    Returns: 
    """

    print(f"""
________________________________________________________________________
              
              ID        :       {id} 
             Title      :       {title}
             Author     :       {author}
            Quantity    :       {qty}
________________________________________________________________________
\n""")
    return 


def search_book():
    """
    search_book() asks the user to choose whether to search for a book by 
    its ID or by its title and author name. If the user chooses to search 
    for the book ID the search_by_id function will be used to find the book. 
    If the user chooses to search for the title and author name the 
    search_by_author_title function will be used to find the book. 
    If a book is found the display_book function is used to display the 
    books information to the user and the record will be returned. 
    If no book is found the user will be told this and search_book() will 
    return None. 

    Paramaters:

    Returns:    
        book_record : Li or NoneType
            The record of the searched for book if a book is found
            or None if a book is not found.
                
    """

    find_method = input("\nPlease choose how you would like to search"+
                              """ for the book:
1. By ID code
2. By tile and author name
\n""")
        
    while find_method != "1" and find_method != "2":
        find_method = input("\nPlease only input \'1\' to find by ID code" +
                            " or \'2\' to find by title and author name.\n")
             

    if find_method == "1":
        search_id = input("\nPlease enter the ID of the book you" +
                          " wish to update:\n")
        search_id = positive_integer(search_id, 0)
        book_record = search_by_id(search_id)

        if book_record == None: 
            print(f"\nWe do not have a book with the ID {search_id} " +
                    "in our database.")
            
        else:
            print("\nCurrently the book has the following information:")
            display_book(book_record[0], book_record[1],
                        book_record[2], book_record[3])
           

    else:   
        search_title = input("\nWhat is the title of the book?\n")
        search_title = correct_string(search_title, 0)

        search_author = input("\nWhat is the name of the author?\n")
        search_author = correct_string(search_author, 0)

        book_record = search_by_author_title(search_author, search_title)
            
        if book_record == None:
            print(f"\nWe do not have \'{search_title}\' by {search_author}"
                  + " in our database.")
            
        else:
            print("\nCurrently the book has the following information:")
            display_book(book_record[0], book_record[1],
                        book_record[2], book_record[3])
            
    return book_record
 

# Start of program.

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
book3001 = [3001, 'A Tale of Two Cities', 'Charles Dickens', 30 ]
book3002 =  [3002, 'Harry Potter and the Philosepher\'s Stone', 
                'J. K. Rowling', 40]
book3003 = [3003, 'The Lion, The Witch and the Wardrobe', 
                'C. S. Lewis', 25]
book3004 = [3004, 'The Lord of the Rings', 'J. R. R. Tolkien', 37]
book3005 = [3005, 'Alice in Wonderland', 'Lewis Carroll', 12]


# Placing the books into a list so they can be easily added to the database.
pop_library = [book3001, book3002, book3003, book3004, book3005]



# Inserting the books into the 'book' table.
cursor.executemany('''INSERT INTO book(id, title, author, qty)
                   VALUES (?,?,?,?)''', pop_library)
db.commit()


print ("""\n\nWelcome to the ebookstore database!
Here you will be able to enter new books to the database, update book 
information, delete books from the database, and search for books. """)


while True:

    menu = input ("""\n\nPlease choose an action from the following:
1. Enter book
2. Update book
3. Delete book
4. Search books
0. Exit
\n""")
    
    # SECTION to enter a new book to the database.
    if menu == "1":
         
        new_title = correct_string(input("\nWhat is the title of the book?\n")
                                   , 0)
        new_author = correct_string(input("\nWhat is the name of the author?\n")
                                    , 0)


        # Check if there is already a record in 'book' which has this title 
        # and author. 
        if search_by_author_title(new_author, new_title) != None:
                
                print(f"\n\'{new_title}\' by {new_author} is already in our" + 
                      " database. \nIf you wish to update this book please" +
                      " choose the update option from the menu.\n")
                continue
        
        new_id = input('\nPlease enter the ID for ' +
                        f"\'{new_title}\' by {new_author}.\n")
        new_id =  positive_integer(new_id, 0)            

        # If there is already a book with the provided ID then ask the  
        # user to provide a unique ID until they do.
        while search_by_id(new_id) != None:
        
            print (f"\n{new_id} is the ID for \'{search_by_id(new_id)[1]}\'" + 
                    f" by {search_by_id(new_id)[2]}.")
            
            new_id = positive_integer(input("\nPlease enter a unique ID.\n"), 0)
               
            
        new_qty = positive_integer(input("\nHow many copies of " + 
                    f"\'{new_title}\' by {new_author} are there?\n"), 0)
                        
        # Add the new record to the book table in ebookstore. 
        cursor.execute(''' 
                        INSERT INTO book(id, title, author, qty)
                        VALUES (?,?,?,?)'''
                       ,(new_id, new_title, new_author, new_qty))
        db.commit()


        # Inform the user of the information which has been added to
        # the database.
        print("\nThe following record has been added to the database:")
        display_book(new_id, new_title, new_author, new_qty)
    

    # SECTION to update or search for a book already in the database.
    elif menu == "2":

        print("\nWe will now search for the book you wish to update.")
        original_book_record = search_book()

        # If no book can be found then continue to menu.
        if original_book_record == None:
            continue

        # The following is for the users updating a book's record. 
        print("""\nYou will now be asked to update all of the above.
If you don't wish to update what is being asked, press the enter key.  """)
        
        # Ask for what the user wishes to update the title to, if they 
        # don't wish to update the title keep the new title as the original
        new_title = input("\nWhat is the title of the book?\n")
        new_title = correct_string(new_title, 1)

        if new_title == "":
            new_title = original_book_record[1]


        # Ask the user to update the authorn name, if they do not wish to 
        # update the author then keep it as the original.
        new_author = input("\nWhat is the name of the author?\n")
        new_author = correct_string(new_author, 1) 
        
        if new_author == "":
            new_author = original_book_record[2]


        update_book_record = search_by_author_title(new_author, new_title)

        # If the author and/or title has changed and there is already 
        # a different record with this information inform the user and 
        # return to the menu.
        if ((new_author != original_book_record[2]  or 
            new_title != original_book_record[1]) and
            update_book_record != None) :
            print(f"\n\'{new_title}\' by {new_author} is already in our" +
                  " database so we are unable to update to this.")
            continue
        
        # Ask the user for the new ID. If they do not wish to change the
        # ID then keep it as the old ID. If they change the ID check
        # if that ID is already used and ask for a unique ID until they
        # input one.
        new_id = input("\nWhat would you like to update the ID to?\n")
        new_id = positive_integer(new_id, 1)

        if new_id == "":
            new_id = original_book_record[0]

        else: 
            while (search_by_id(new_id) != None and 
                new_id != original_book_record[0]):

                print(f"\n{search_by_id(new_id)[0]} is the ID of \'" +
                    f"{search_by_id(new_id)[1]}\' by {search_by_id(new_id)[2]}.")
                
                new_id = input("\nPlease input a different ID number:\n")
                new_id = positive_integer(new_id, 1)
                
                if new_id == "": 
                    new_id = original_book_record[0]
                

        # Ask the user to update the book quantity. If they do not wish 
        # to change the quantity, keep the original quantity.         
        new_qty = input("\nWhat would you like to update the quantity to?\n")
        new_qty = positive_integer(new_qty, 1)
        
        if new_qty == "": 
            new_qty = original_book_record[3]

        # Update the record of the original book. 
        cursor.execute(''' 
                    UPDATE book SET id = ?, title = ?, author =?, qty = ?
                    WHERE id = ?''', (new_id, new_title, new_author, new_qty,
                                      original_book_record[0]))
        db.commit()

        print("\nThe book has now been updated with the following information:")
        display_book(new_id, new_title, new_author, new_qty)


    # SECTION to delete a book from the database.
    elif menu == "3":
        
        print("\nWe will now try and find the book you wish to delete.")
        original_book_record = search_book()

        if original_book_record == None:
            continue

        delete = input("\nAre you sure you want to delete this book?\n")
        delete = check_yes_no(delete)
        
        if delete == "no":
            print("\nThis book will not be deleted.")
            continue

        cursor.execute('''DELETE FROM book WHERE id = ?''',
                        (original_book_record[0],))
        db.commit()

        print("\nThe above book has now been deleted from the \'book\' table.")
    

    # SECTION to search for a book
    elif menu == "4":
        
        search_book()
        

    # Exit program
    elif menu == '0' : 
        exit()

    else : 
        print('\nPlease only input a \'1\', \'2\', \'3\', \'4\' or \'0\'.')



   