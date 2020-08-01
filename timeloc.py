from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
from bs4 import BeautifulSoup


def time(update,context):
	city_name=update.message.text[6:]
	r=requests.get("https://google.com/search?q="+city_name+"Time")
	response=r.content
	#print(response)
	soup=BeautifulSoup(response,"html.parser")
	rows=soup.find_all('div',{'class':'BNeawe iBp4i AP7Wnd'})
	for row in rows:
    		try:
    			if row.find('div').text is None:
    				update.message.reply_text(" ")
    			else:
    				update.message.reply_text(row.find('div').text)
    		except:
        		update.message.reply_text("Thank you!")
        	# except:
        	# 	update.message.reply_text("Something went wrong")


updater = Updater('1251053034:AAGMDVLqSk2VW6blNtqhG98hSt4mmnH9A1I', use_context=True)
updater.dispatcher.add_handler(MessageHandler(Filters.text,time))
updater.start_polling()
updater.idle()