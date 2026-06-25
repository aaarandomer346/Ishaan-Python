import tkinter as tk
import json
import os

root = tk.Tk()
root.title("Mom's Book Finder")
root.geometry("250x60")

DATA_FILE_PATH = os.path.expanduser("~/data.jsonl")

########################################################################################################
# Enter Books Top level ################################################################################
########################################################################################################

def show_add_entry_top_level():
    tags=[]
    def add_tag_to_book():
        tag = entry2.get() # gets the input of entry box 2
        if tag:
            tags.append(tag) # adds tag to list
            entry2.delete(0, tk.END) # clears entry box

    def add_data():
        name = entry1.get() # gets the input of entry box 1
        if name:
            book_data = { # json data to be added
                "name": name,
                "tags": tags
            }
            with open(DATA_FILE_PATH, "a") as file:
                file.write(json.dumps(book_data) + "\n") # adds data to josnl file without overriding previous content / allows for multiple entries
            entry1.delete(0, tk.END) # clears entry box
            tags.clear() # clears tags list


    top = tk.Toplevel(root)
    top.title("Add Book Entry")

    tk.Label(top, text="Book Name").grid(row=0, column=0) # Label for book name
    tk.Label(top, text="Tags").grid(row=1, column=0) # Label for tags

    button = tk.Button(top, text="Add Tag", command=add_tag_to_book)
    button.grid(row=1, column=2, columnspan=1) # button to add tag to list

    button = tk.Button(top, text="Add Data", command=add_data)
    button.grid(row=2, column=0, columnspan=2) # button to add data to jsonl file

    entry1 = tk.Entry(top) # adds entry box
    entry2 = tk.Entry(top) # adds entry box

    entry1.grid(row=0, column=1) # places entry box1
    entry2.grid(row=1, column=1) # places entry box2

    top.mainloop()

########################################################################################################
# Find Books Top level #################################################################################
########################################################################################################

def show_find_book_based_on_tags():
    tags=[]

    def findbookfromtags():
        with open(DATA_FILE_PATH, "r") as file:
            book_data = []
            for line in file:
                book_data.append(json.loads(line))

        found_books = []
        tag_match_count = 0
        for book in book_data:
            tag_match_count = 0
            for tag in tags:
                if tag in book["tags"]:
                    tag_match_count += 1
            if tag_match_count >= len(tags):
                found_books.append(book)

        current_row = 4
        for book in found_books:
            tk.Label(top, text=f"- {book['name']}").grid(row=current_row, column=0, sticky=tk.W) # displays found books in label form
            current_row += 1


    def add_tag_to_book():
        tag = tagentry.get() # gets the input of entry box 2
        if tag:
            tags.append(tag) # adds tag to list
            tagentry.delete(0, tk.END) # clears entry box
    
    top = tk.Toplevel(root)
    top.title("Find Book Based on Tags")

    tk.Label(top, text="Tags").grid(row=1, column=0) # Label for tags

    tagentry = tk.Entry(top)
    tagentry.grid(row=1, column=1) # places entry box2

    button = tk.Button(top, text="Add Tag", command=add_tag_to_book)
    button.grid(row=1, column=2, columnspan=1)

    tk.Button(top, text="Find Book(s)", command=findbookfromtags).grid(row=2, column=0, columnspan=2)

    tk.Label(top, text="Found Book(s):").grid(row=3, column=0) # Label for found books

    tk.Button(top, text="Close", command=top.destroy).grid(row=0, column=0, columnspan=3) # button to close top level window

########################################################################################################
# Main Root Window #####################################################################################
########################################################################################################

tk.Button(root, text="Add Book Entry", command=show_add_entry_top_level).pack()
tk.Button(root, text="Find Book", command=show_find_book_based_on_tags).pack()

root.mainloop()