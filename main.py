import os
import openai
import logging
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")
openai.api_key = os.getenv('OPENAI_API_KEY')
system_prompt = """
You are an expert in developing HTML solutions. Given the instructions,
 your task is to generate HTML layout for a text article. Your HTML markup should only consist of 
 tags which are allowed inside ```<body>```. Do not include these tags: ```<body>```, ```<html>```, ```<head>```. 
 Do not use any CSS styles or JS code, use only pure HTML.
 Your final answer should consist only of HTML markup without any additional text. 
 Follow these instructions thoroughly and carefuly:
1. Read the text article from user.
2. Write HTML markup based on text, while using the best semantic practices.
3. Given the context of a text, define places, where it would be suitable to add images:
3.1. For each of these places, create a text prompt for an image generation.
 Generated prompt should be detailed and have a purpose of illustrating the text based on context.
3.2. For previously defined places, add an ```<img src="image_placeholder.jpg" alt=''>```. In ```alt``` attribute,
 add previously generated prompts, respectively.
3.3. Wrap each image in a ```<figure>``` and add ```<figcaption>``` tag with image description in the language of this text.
 Image description should be concise and helpful.
4. For the final answer, combine your code with additions from 3.
"""

def read_article(file_path: str) -> str:
    """Reads content from a text file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except (FileNotFoundError, IOError) as e:
        logging.error(f"Error reading the file '{file_path}': {e}")
        raise

def get_html_from_article(system_prompt: str, article_content: str) -> str:
    """Calls the OpenAI API with article and prompt and returns the response content."""
    try:
        response = openai.chat.completions.create(
            model='gpt-4o',
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": article_content}
            ]
        )
        return response.choices[0].message.content
    except openai.OpenAIError as e:
        logging.error(f"Error during the API call: {e}")
        raise

def write_to_file(file_path: str, content: str) -> None:
    """Writes content to a file."""
    try:
        with open(file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(content)
    except IOError as e:
        logging.error(f"Error writing to the file '{file_path}': {e}")
        raise

if __name__ == "__main__":
    input_file = 'artykul.txt'
    output_file = 'artykul.html'

    article_content = read_article(input_file)
    generated_html = get_html_from_article(system_prompt, article_content)
    write_to_file(output_file, generated_html)