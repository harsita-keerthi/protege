import reflex as rx
from rxconfig import config
from .components.navbar import *
from server.transcribe import *
import io

class State(rx.State):
    # Example of how you might process the file bytes before passing
    def handle_upload(self, files):
        if files:
            # The uploaded files come in as a list, handle the first one
            uploaded_file = files[0]
            # Extract the file name and content
            file_name = uploaded_file["name"]
            file_content = uploaded_file["content"]  # Content will be in bytes
            
            # You can now process the content, e.g., transcribe or save the file
            self.process_audio(file_content, file_name)
    
    def process_audio(self, file_content, file_name):
        # Assume process is a function that handles the audio content
        # file_content is in bytes, so you may need to use an audio processing library
        # For example, saving it to a temporary file and processing it:
        
        # Example: save file to a temp directory, use pydub or wave to process the audio
        audio_file = io.BytesIO(file_content)  # Convert bytes into a file-like object
        
        # Pass the audio to some transcription function
        # For example: transcribe(audio_file)
        process(audio_file, file_name)  # Call your processing/transcribing function

def teach() -> rx.Component:
    return rx.fragment(
        navbar_user(),  # navbar
        rx.color_mode.button(position="bottom-left"),
        rx.vstack(
            rx.heading("become a protégé.", size="9", align="center"),
            rx.upload(
                rx.text("Drag and drop files here or click to select files"),
                rx.icon(tag="upload"),
                accept={"audio/*": [".mp3", ".wav", ".m4a"]},
                border="1px dotted rgb(107,99,246)",
                padding="5em",
                id="audio_upload",  # assign an ID to reference later
            ),
            rx.button(
                "Submit", 
                on_click=process()
            ),

            # styling
            spacing="5",
            justify="center",
            align_items="center",
            display="flex",
            flex_direction="column",
            min_height="85vh",
            padding_bottom="220px",
            padding_top="240px",
        ),
    )
