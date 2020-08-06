 from flask import Flask , request
from twilio.twiml.messaging_response import MessagingResponse
import requests
from googletrans import Translator
app = Flask(__name__)

xx = {'irish':'ga','italian':'it','arabic':'ar','japanese':'ja','kannada':'kn',
    'korean':'ko','bengali':'bn','Latin':'la','portuguese':'pt','russian':'ru','french':'fr',
    'spanish':'es','swedish':'sv','greek':'el','telugu':'te','gujarati':'gu','hindi':'hi','tamil':'ta'}

fin=list()
lan=list()

@app.route("/")
def helo():
    return "Hello Anuraag"

@app.route("/Projext",methods = ["GET","POST"])
def Projext_reply():
    msg = request.form.get('Body')
    s1 = str(msg)
    s2 = s1.lower()
    print(s2)
    if s2=="stop translation":
        fin.clear()
        lan.clear()
        ad="Thank You!!"
        resp3 = MessagingResponse()
        resp3.message(ad)
        return str(resp3)
    elif len(fin)==0:
        fin.append(1)
        dfd = "Hello! can you tell me to which language i have to translate !!"
        respo = MessagingResponse()
        respo.message(dfd)
        return str(respo)
    elif len(fin)!=0 and len(lan)==0:
        lan.append(s2)
        resp1 = MessagingResponse()
        resp1.message("Continue sending the text to translate\nIf you want to Stop , send me the message STOP TRANSLATION")
        return str(resp1)
    elif len(fin)!=0 and len(lan)!=0:
        trans = Translator()
        t = trans.translate(s2,src="en",dest=xx[lan[0]])
        sf = str(t.text)
        resp2 = MessagingResponse()
        resp2.message(sf)
        return str(resp2)

if __name__=="__main__":
    app.run(debug=True)