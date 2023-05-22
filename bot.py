import telebot
from book import *
from reminder import *
BOT_TOKEN="5911996942:AAE9rRbyK_Y9NuvG1zBkq6xVmBznsMfsLFI"
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "\n /show_books -> Show all books \n /show_reminders -> List all reminders")

@bot.message_handler(commands=['show_books'])
def send_welcome(message):
    bot.reply_to(message, show_books() if show_books() else "Nothing to read")

@bot.message_handler(commands=['show_reminders'])
def send_welcome(message):
    bot.reply_to(message, show_reminder() if show_reminder() else "Nothing to reminder")


import json
import numpy as np
@bot.message_handler(func=lambda msg: True)
def confirm_order(message):
    id=message.chat.id
    text=message.text
    text=str(text).lower()
    if text.startswith(("add book","new book")):
        book_name=text.split("book")[-1]
        add_book(book_name,id)
        bot.reply_to(message,"Book added to your list {book}. \n\nNow you have {count} books in your list.".format(book=book_name[1:],count=count_books(id)))
    
    
    elif text.startswith(("add reminder","set reminder","reminder","create reminder")):
        reminder=text.split("reminder")[-1]
        add_reminder(reminder,id)
        bot.reply_to(message,"Added reminder for {reminder}. Now there are {count} reminders in your list.".format(reminder=reminder,count=count_reminders(id)))
    
    
    elif text.startswith(("show books","show book","show all books","show all book","list books","list book","all books","all book")):
        books=show_books(id)
        bot.reply_to(message,books)
    
    
    elif text.startswith(("show reminders","show reminder","list reminders","list reminder","show all reminders","show all reminder","all reminder","all reminders")):
        reminder=show_reminder(id)
        bot.reply_to(message,reminder)

    elif text.startswith(("book finished","completed book","remove book","book remove","book completed")):
        book_id=text.split(" ")[-1]
        finish_book(book_id,id)
    
    elif text.startswith("reminder remove"):
        rem_id=text.split(" ")[-1]
        finish_book(rem_id,id)
           
bot.infinity_polling()
