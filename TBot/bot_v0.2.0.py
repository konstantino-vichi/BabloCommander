import os
from openai import OpenAI

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

print(_)


def get_completion_from_messages(messages, 
                                 model="gpt-3.5-turbo-1106", 
                                 temperature=0, 
                                 max_tokens=500):
    response = client.chat.completions.create(model=model,
    messages=messages,
    temperature=temperature, 
    max_tokens=max_tokens)
    return response.choices[0].message.content

delimiter = "####"
system_message = f"""
You will be provided with a list of spending entries. \
Each spending entry will be delimited with \
{delimiter} characters.
Categorize each entry into primary and secondary categories, \
and extract additional details like amount, currency, and user notes. 
Provide your output in JSON format with keys: \
category, subcategory, amount, currency, and notes.

Primary categories: Food, Housing, Transportation, Entertainment, Utilities, Others.

Food secondary categories:
Meal, Grocery, Beverage, Snack

Housing secondary categories:
Rent, Mortgage, Utilities, Maintenance

Transportation secondary categories:
Public Transport, Fuel, Vehicle Maintenance, Bike

Entertainment secondary categories:
Movies, Concerts, Sports, Travel

Utilities secondary categories:
Electricity, Water, Internet, Mobile

Others secondary categories:
Clothing, Health, Education, Miscellaneous

"""

# Example user message
user_message = f"""\
124 - lunch at the office\
{delimiter}85 - coffee at Starbucks\
{delimiter}150 - groceries at Seven Eleven\
{delimiter}10338 - rent for kvartira #1\
{delimiter}1994 - utilities for kvartira #2\
{delimiter}3200 - new bike purchase\
"""

messages = [
    {'role':'system', 'content': system_message},
    {'role':'user', 'content': f"{delimiter}{user_message}{delimiter}"},
]

response = get_completion_from_messages(messages)
print(response)