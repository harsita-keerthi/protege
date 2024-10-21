from deepgram import DeepgramClient, PrerecordedOptions
import os
import fastapi

DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
AUDIO_FILE = "sample.m4a"

def process():
    deepgram = DeepgramClient(DEEPGRAM_API_KEY)
    with open(AUDIO_FILE, 'rb') as buffer_data:
        payload = { 'buffer': buffer_data }

        options = PrerecordedOptions(
            smart_format=True, model="base", language="en-US"
        )

        response = deepgram.listen.prerecorded.v('1').transcribe_file(payload, options)
        # transcript = response.to_json()['results']['channels'][0]['transcript']
        # print(transcript)
        print(response.to_json(indent=4))