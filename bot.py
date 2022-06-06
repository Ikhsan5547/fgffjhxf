import telebot
import json

api = '5220149696:AAE1FlvfEh7P4nu-9nRD0NfGLTH2tl-MlXE'

bot = telebot.TeleBot(api)

@bot.message_handler(commands = ['start'])
def send_welcome(message):
    bot.reply_to(message,'Silakan pilih menu')
    bot.reply_to(message,'/Abjad')
    bot.reply_to(message, 'Terima Kasih')

@bot.message_handler(commands = ['Abjad'])
def send_welcome(message):
    bot.reply_to(message,'A')
    bot.reply_to(message,'B')
    bot.reply_to(message,'C')
    bot.reply_to(message,'D')
    bot.reply_to(message,'E')
    bot.reply_to(message,'F')
    bot.reply_to(message,'G')
    bot.reply_to(message,'I')
    bot.reply_to(message,'J')
    bot.reply_to(message,'K')
    bot.reply_to(message,'L')
    bot.reply_to(message,'M')
    bot.reply_to(message,'N')
    bot.reply_to(message,'O')
    bot.reply_to(message,'P')
    bot.reply_to(message,'Q')
    bot.reply_to(message,'R')
    bot.reply_to(message,'S')
    bot.reply_to(message,'T')
    bot.reply_to(message,'U')
    bot.reply_to(message,'V')
    bot.reply_to(message,'X')
    bot.reply_to(message,'Y')
    bot.reply_to(message,'Z')
    bot.reply_to(message,'www.xnxx.com')
print("Bot Berjalan")

bot.polling()