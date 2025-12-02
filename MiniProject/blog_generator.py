from google import genai
from google.genai import types
from dotenv import dotenv_values

config = dotenv_values("../.env")
client = genai.Client(api_key=config["API_KEY"])


def generate_blog(paragraph):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Write a paragraph about the following topic" + paragraph,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0)
        ),
    )

    reply = response.text
    return reply

keep_writing = True

while keep_writing:
    answer = input("Do you want to write a paragraph?, 'Y' for yes and anything else for no: ")
    if answer == "Y":
        paragraph = input("What is the paragraph you want to write?: ")
        print(generate_blog(paragraph))
    else :
        keep_writing = False