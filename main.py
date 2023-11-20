import asyncio
import json
import requests
from pyrogram import Client,filters
api_id = 28077568
api_hash = "e84821a2cb299ceba1b8334947ca8b11"
bot_token = "6784652347:AAGQn0uHky5ZdGxLpdkbQy5vYtu8F4qVFRs"





app = Client(
    "my_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)
@app.on_message(filters.private)
def check(_,message):
    address = message.text
    response = requests.get(f'http://api.ipstack.com/{address}?access_key=92fdff29674615f83ed3c343cb239853')
    data = response.json()
    ip = data["ip"]
    country = data['country_name']
    city = data['city']
    zip = data['zip']
    country_code = data['country_code']
    flag_emoji = data["location"]["country_flag_emoji"]
    message.reply(f"address: {address}\n ip: {ip}\ncountry: {country} {flag_emoji}\n {country_code}\n city: {city}\n zip: {zip}" )


app.run()