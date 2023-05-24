import telebot
from book import *
from reminder import *
from files import *
import variables as v
BOT_TOKEN="5911996942:AAE9rRbyK_Y9NuvG1zBkq6xVmBznsMfsLFI"
bot = telebot.TeleBot(BOT_TOKEN)

### Commands List


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "\n /show_books -> Show all books \n /show_reminders -> List all reminders")

@bot.message_handler(commands=['show_books'])
def send_welcome(message):
    bot.reply_to(message, show_books() if show_books() else "Nothing to read")

@bot.message_handler(commands=['help'])
def help(message):
    help=get_help()
    bot.reply_to(message,"On the Right you have the function and on the left is the different commands which can be used for that function\n"+help)
    

@bot.message_handler(commands=['show_reminders'])
def send_welcome(message):
    bot.reply_to(message, show_reminder() if show_reminder() else "Nothing to reminder")


@bot.message_handler(func=lambda msg: True)
def confirm_order(message):
    id=message.chat.id
    text=message.text
    text=str(text).lower()
    if text.startswith("help"):
        help=get_help()
        bot.reply_to(message,"On the Right you have the function and on the left is the different commands which can be used for that function\n"+help)
    
    if text.startswith(v.show_books):
        books=show_books(id)
        bot.reply_to(message,"Here is the list of books:-\n"+books)
    
    
    elif text.startswith(v.show_reminders):
        reminder=show_reminder(id)
        bot.reply_to(message,"List of reminders:- \n"+ reminder)

    elif text.startswith(v.finish_book):
        book_id=text.split(" ")[-1]
        book_name=finish_book(book_id,id)
        bot.reply_to(message,"Marked {book} as read".format(book=book_name))


    elif text.startswith(v.mark_reminder):
        rem_id=text.split(" ")[-1]
        rem=finish_reminder(rem_id,id)
        bot.reply_to(message,rem+"marked as finished")
    
    elif text.startswith(v.remove_book):
        book_id=text.split(" ")[-1]
        book_name=remove_book(book_id,id)
        bot.reply_to(message,"Removed {book} from your list".format(book=book_name))

    elif text.startswith(v.remove_reminder):
        rem_id=text.split(" ")[-1]
        rem=remove_reminder(rem_id,id)
        bot.reply_to(message,"Reminder removed :-"+rem)
    
    elif text.startswith(v.add_book):
        book_name=text.split("book")[-1]
        add_book(book_name,id)
        bot.reply_to(message,"Book added to your list {book}. \n\nNow you have {count} books in your list.".format(book=book_name[1:],count=count_books(id)))
    
    elif text.startswith(v.add_reminder):
        reminder=text.split("reminder")[-1]
        add_reminder(reminder,id)
        bot.reply_to(message,"Added reminder for {reminder}. Now there are {count} reminders in your list.".format(reminder=reminder,count=count_reminders(id)))
    
    elif text.startswith(v.add_list):
        name=text.split("list")[-1]
        create_list(name[1:],id)
        bot.reply_to(message,"Created new list with title"+name)
    
    elif text.startswith(v.remove_list):
        list_id=text.split(" ")[-1]
        name=remove_list(list_id,id)
        bot.reply_to(message,"Removed list"+name)

    elif text.startswith(v.show_list):
        string=show_list(id)
        bot.reply_to(message,"List is"+string)
    
    elif text.startswith(v.add_user_list):
        list_name=text.split(" ")[1]
        all_list=get_list(id)
        if list_name not in all_list:
            bot.reply_to(message,"List doesn't exists. Create list first")
        else:
            add_element(list_name,text.split(list_name)[-1],id)
        bot.reply_to(message,"added movie"+text.split(list_name)[-1])
    elif text.startswith(v.show_user_list):
        list_name=text.split(" ")[1]
        all_list=get_list(id)
        if list_name not in all_list:
            bot.reply_to(message,"List doesn't exists. Create list first")
        else:
            string=show_element(list_name,id)
            bot.reply_to(message,string)
bot.infinity_polling()
