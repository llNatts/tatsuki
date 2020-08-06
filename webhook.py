import requests #dependency
import json
import requests
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook, DiscordEmbed
import time

## Scrapy
reques_url = "https://animeshouse.net/"

req = requests.get(reques_url)
soup = BeautifulSoup(req.text, 'html.parser')


def titleItem():
	data = soup.find(class_="data")
	title = data.get_text()
	return title[0:-4]

title = titleItem()

def epItem():
	epi = soup.find(class_="epi").get_text()
	return epi

def imgItem():
	imgClass = soup.find(class_="item se episodes")
	img_url = imgClass.div.img['src']
	return img_url

def sinopseUrl():
	homeanime = soup.find(class_="poster")
	homeurl = homeanime.a['href']
	req2 = requests.get(homeurl)
	soup2 = BeautifulSoup(req2.text, 'html.parser')
	print(req2.status_code)

	info = soup2.find(id="info")
	sinopse = info.div.p.get_text()
	return sinopse


### webhook

webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/734857159853998172/JSj-SkgFkJcU0VY0wgYAYMtnHCHgay92CjiUr1SOwAzvpiaMQZteJgt43actbrvWRugI')

embed = DiscordEmbed(title=f'{title}', description=f'{epi}', color=242424)
embed.set_author(name=f'Animes House', url='', icon_url='https://animeshouse.net/wp-content/uploads/2020/07/favicon.png')
embed.set_footer(text=f'Animes House')
embed.set_thumbnail(url=imgUrl)
embed.set_timestamp()
embed.add_embed_field(name='Sinopse', value=sinopse)
webhook.add_embed(embed)



###Schedule


def executeSomething():
	req = requests.get(reques_url)
	soup = BeautifulSoup(req.text, 'html.parser')

	newdata = soup.find(class_="data")
	newtitle = newdata.get_text()[0:-4]

	if newtitle == title:
		print('Não temos nada de novo')
		time.sleep(60)
	else:
		response = webhook.execute()
while True:
    executeSomething()
