import os
import google.generativeai as genai
from dotenv import load_dotenv

# load environment variables
load_dotenv()

# configure the Generative AI API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# function to create a lesson plan
def generate_pointers(transcript):
    # set up generation configuration
    generation_config = {
        "temperature": 0.5,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "application/json",
    }

    # create the generative model
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        system_instruction="You are an AI designed to help users enhance their learning by allowing them to teach you a subject. After the user explains a concept, create a table with the columns as positive feedback, negative feedback, and which topics they should review more. Your goal is to help the user solidify their understanding through reflection. Adapt your feedback table based on their explanations, focusing on areas where you sense uncertainty or opportunity for more learning. Be empathetic and understand their learning needs. Do not be condescending.",
    )

    # construct the user prompt
    user_prompt = transcript

    # initialize history
    history = []

    # start a chat session
    chat_session = model.start_chat(history=history)

    # send the message and get a response from the model
    response = chat_session.send_message(user_prompt)

    # get the model's response
    model_response = response.text

    # append the user input and model response to the history (optional for tracking)
    history.append({"role": "user", "parts": [user_prompt]})
    history.append({"role": "model", "parts": [model_response]})

    return model_response  # return the lesson plan generated by the model