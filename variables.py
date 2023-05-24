#  On the Right you have the function and on the left is the different commands which can be used for that function

## Books
var_add_book=("add book",
          "new book",
          "insert book",
          "book")

var_finish_book=("book finished",
             "completed book",
             "book completed",
             "finished book",
             "mark book")

var_remove_book=("remove book",
             "book remove")

var_show_books=("show books",
            "show book",
            "show all books",
            "show all book",
            "list books",
            "list book",
            "all books",
            "all book")



## Reminders
var_add_reminder=("add reminder",
              "set reminder",
              "reminder",
              "create reminder",
              "set reminder",
              "new reminder")

var_mark_reminder=("reminder finished",
               "completed reminder",
               "reminder completed",
               "reminder done",
               "mark reminder")
var_remove_reminder=("reminder remove",
               "remove reminder",
               "delete reminder")

var_show_reminders=("show reminders",
                "show reminder",
                "list reminders",
                "list reminder",
                "show all reminders",
                "show all reminder",
                "all reminder","all reminders")



## Creating New
var_add_list=("create list",
          "new list",
          "add list")

var_remove_list=("remove list",
             "delete list")

var_show_list=("show list",
           "all lists")

## Custom List
var_add_user_list=("add ")
var_show_user_list=("show",
                "all")
import os
def get_excel_path(id):
    return os.path.join("..","files",str(id)+".xlsx")
