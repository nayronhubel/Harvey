#Python libraries that we need to import for our bot
import random
import aiml
import re
from audio import Track
from flask import Flask, request
from pymessenger.bot import Bot

Track("https://cdn.fbsbx.com/v/t59.3654-21/28964772_1797027617028337_3373347643051737088_n.mp4/audioclip-1520694901000-2304.mp4?oh=ed3bd05101e5a9a9cd26ee137e02c49c&oe=5AA6F2ED")
app = Flask(__name__)
ACCESS_TOKEN = 'EAACohPsenJYBANFsNH2zBdRZAYFChz0jxn6ZCKIbvcErZBYHusrPViIS9GYHtaCgUF7Xhkeu1YhEeW37YmB5yHM10BAHZAkFzx2kM17efBCi2cOIWpoMzpZBorMaTCS60WrecvRN6ZBA4zgeFK1OJxaSAlgGxwesK0jPXNXU5rZAwZDZD'
VERIFY_TOKEN = 'teste1234'
bot = Bot(ACCESS_TOKEN)

kern = aiml.Kernel()
brainLoaded = False
forceReload = True
while not brainLoaded:
	if forceReload or (len(sys.argv) >= 2 and sys.argv[1] == "reload"):
		# Use the Kernel's bootstrap() method to initialize the Kernel. The
		# optional learnFiles argument is a file (or list of files) to load.
		# The optional commands argument is a command (or list of commands)
		# to run after the files are loaded.
		kern.bootstrap(learnFiles="std-startup.xml", commands="load aiml b")
		brainLoaded = True
		# Now that we've loaded the brain, save it to speed things up for
		# next time.
		kern.saveBrain("standard.brn")
	else:
		# Attempt to load the brain file.  If it fails, fall back on the Reload
		# method.
		try:
			# The optional branFile argument specifies a brain file to load.
			kern.bootstrap(brainFile = "standard.brn")
			brainLoaded = True
		except:
			forceReload = True

#We will receive messages that Facebook sends our bot at this endpoint 
@app.route("/", methods=['GET', 'POST'])


def receive_message():
	if request.method == 'GET':
		"""Before allowing people to message your bot, Facebook has implemented a verify token
		that confirms all requests that your bot receives came from Facebook.""" 
		token_sent = request.args.get("hub.verify_token")
		return verify_fb_token(token_sent)
    #if the request was not get, it must be POST and we can just proceed with sending a message back to user
	else:
        # get whatever message a user sent the bot
		output = request.get_json()
		for event in output['entry']:
			messaging = event['messaging']
			for message in messaging:
				if message.get('message'):
					#Facebook Messenger ID for user so we know where to send response back to
					recipient_id = message['sender']['id']
					if message['message'].get('text'):
						mensagem = message['message']['text']
						response_sent_text = get_message(remove_acentos(mensagem))
						send_message(recipient_id, response_sent_text)
						#if user sends us a GIF, photo,video, or any other non-text item
					if message['message'].get('attachments'):
						for attachment in message['message']['attachments']:
							if(attachment['type'] == "audio"):
								response_sent_nontext = get_message(Track(attachment["payload"]["url"]))
								send_message(recipient_id, response_sent_nontext)
							else:
								response_sent_nontext = get_attachments(attachment["payload"]["url"])
								send_message(recipient_id, response_sent_nontext)

	return "Message Processed"

def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'
	
def remove_acentos(mensagem):
	mensagem = re.sub(u'[àÀáÁâÂãÃ]', 'a', mensagem)
	mensagem = re.sub(u'[éÉêÊ]', 'e', mensagem)
	mensagem = re.sub(u'[íÍîÎ]', 'i', mensagem)
	mensagem = re.sub(u'[óÓôÔõÕ]', 'o', mensagem)
	mensagem = re.sub(u'[úÚûÛ]', 'u', mensagem)
	mensagem = re.sub(u'[çÇ]', 'c', mensagem)
	return mensagem

#chooses a random message to send to the user
def get_message(income):
	return kern.respond(income)

def get_attachments(income):
	return income

#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

if __name__ == "__main__":
    app.run()