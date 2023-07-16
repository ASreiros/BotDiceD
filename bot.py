import discord
import replies
import keys
import math


async def send_message(message, user_message, is_private):
    try:
        response = replies.get_response(user_message)
        if response:
            if len(response) <= 2000:
                await message.author.send(response) if is_private else await message.channel.send(response)
            else:
                print(response)
                number_of_msg = math.ceil(len(response) / 2000)
                for n in range(0, number_of_msg):
                    f1 = 2000*n
                    f2 = 2000*(n+1)
                    msg = response[f1:f2]
                    await message.author.send(msg) if is_private else await message.channel.send(msg)

    except Exception as e:
        print(e)


def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(keys.TOKEN)
