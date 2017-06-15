from watson_developer_cloud import TextToSpeechV1
username = '06b7c2a5-c27f-4917-b814-f4f068bd7719'
password = 'ys1L5MZDkXSY'

def text2speech(text, filename):
    watson_speech = TextToSpeechV1(username=username,password=password)
    with open(filename, 'wb') as file:
        file.write(watson_speech.synthesize(text=text, voice='en-US_AllisonVoice'))

#filename = '/Users/wzy/Documents/test.wav'
#text = 'Good afternoon'

#text2speech(text=text, filename=filename)