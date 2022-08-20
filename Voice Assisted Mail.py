#!/usr/bin/env python
# coding: utf-8

# In[1]:


import speech_recognition as sr
import yagmail
#import PyAudio
recognizer=sr.Recognizer()
with sr.Microphone() as source:
    print('Clearing background noise..')
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print("waiting for your message...")
    recordedaudio=recognizer.listen(source)
    print('Done recording..!')
try:
    print('Printing the message..')
    text=recognizer.recognize_google(recordedaudio,language='en-US')

    print('Your message:{}'.format(text))

except Exception as ex:
    print(ex)

#Automate mails:

reciever='xyz@gmail.com'
message=text
sender=yagmail.SMTP('abc@gmail.com')
sender.send(to=reciever,subject='This is an automated mail',contents=message)


# In[ ]:




