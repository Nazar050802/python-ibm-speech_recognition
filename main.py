from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

import speech_recognition as sr

# Get API and URL from this link https://www.ibm.com/cloud/watson-speech-to-text
apikey = 'YOUR API KEY'
url = 'YOUR URL'

authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator=authenticator)
stt.set_service_url(url)

MICROPHONE_INDEX = 1


# Recognize data with IBM service
def recognize_audio_with_IBM(audio_file):
    speech_recognition_results = stt.recognize(audio=audio_file.get_wav_data(), content_type='audio/wav').get_result()

    # Convert (json into str) and than convert (str into dict)
    json_to_dict = json.loads(json.dumps(speech_recognition_results))

    # Return data from dict
    return json_to_dict.get('results')[0].get('alternatives')[0].get('transcript')

  
# Main function
def main():
    # Get audio from micriphone
    r = sr.Recognizer()
    with sr.Microphone(device_index=MICROPHONE_INDEX) as source:

        print("Say something!")
        audio = r.listen(source)
    
    print(recognize_audio_with_IBM(audio))

    
main()
