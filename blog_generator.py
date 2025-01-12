import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("No API key found. Make sure the environment variable 'OPENAI_API_KEY' is set correctly.")

import openai

openai.api_key = api_key


def generate_blog_post(prompt):
    """Generates a blog post based on the given prompt.

    Args:
        prompt: The prompt to guide the blog post generation.

    Returns:
        The generated blog post as a string.
    """
    response = openai.Completion.create(
        model="gpt-4o-mini",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7
    )

    blog_post = response.choices[0].text.strip()
    return blog_post


def main():
    print(r"""
Welcome to the Blog Post Generator!

     __  __      ____            _                 _ 
    |  \/  |_ __| __ )  __ _ ___| |__  _   _  __ _| |
    | |\/| | '__|  _ \ / _` / __| '_ \| | | |/ _` | |
    | |  | | |  | |_) | (_| \__ \ | | | |_| | (_| | |
    |_|  |_|_|  |____/ \__,_|___/_| |_|\__, |\__,_|_|
                                       |___/
    """)

    create_blog = input("Would you like to create a blog post? (y/n): ").strip().lower()

    if create_blog == 'y':
        topic = input("What topic do you need the blog post on? ").strip()
        title = input("What title do you want for the blog post? ").strip()
        add_emojis = input("Should I add emojis too? (y/n): ").strip().lower()

        prompt = f"Write a blog post titled '{title}' on the topic '{topic}'."

        if add_emojis == 'y':
            prompt += " Include emojis."

        blog_post = generate_blog_post(prompt)
        print("\nGenerated Blog Post:")
        print(blog_post)
    else:
        print("Okay, maybe next time!")


if __name__ == "__main__":
    main()
