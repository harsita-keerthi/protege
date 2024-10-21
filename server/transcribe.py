from deepgram import DeepgramClient, PrerecordedOptions
import os
import json
from .critique import *

# Example of a custom class
class CustomResponse:
    def __init__(self, data):
        self.data = data

    def to_dict(self):
        return self.data  # Convert the object to a dictionary
    
    curr_feedback=""

DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
AUDIO_FILE = "sample.m4a"

def process():
    deepgram = DeepgramClient(DEEPGRAM_API_KEY)
    with open(AUDIO_FILE, 'rb') as buffer_data:
        payload = {'buffer': buffer_data}

        options = PrerecordedOptions(
            smart_format=True, model="base", language="en-US"
        )

        # Make the API call
        response = deepgram.listen.prerecorded.v('1').transcribe_file(payload, options)

        # Function to handle serialization of non-serializable types
        def custom_serializer(obj):
            if hasattr(obj, 'to_dict'):
                return obj.to_dict()  # Call to_dict method if it exists
            raise TypeError(f'Object of type {type(obj)} is not JSON serializable')

        # Convert response to JSON string
        json_string = json.dumps(response, default=custom_serializer)

        # Convert JSON string back to a Python dictionary
        response_dict = json.loads(json_string)

        # Now you can access the values using keys
        transcript = response_dict["results"]["channels"][0]["alternatives"][0]["transcript"]

        # Print the transcript
        CustomResponse.curr_feedback = generate_pointers(transcript)

def get_feedback():
    return CustomResponse.curr_feedback