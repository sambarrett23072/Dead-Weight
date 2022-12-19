import os
import discord
import responses
from dotenv import load_dotenv


# Send messages
async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN').strip('{').strip('}')
    intents = discord.Intents.all()
    intents.message_content = True
    client = discord.Client(intents=intents)

    #message runs when bot starts
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_voice_state_update(member, before, after):
        if before.channel and not after.channel:
            print(f'{member} has left the vc')
            await send_message(user_message="953272075555074142",is_private=False,message="test")

            
    # Remember to run your bot with your personal TOKEN
    client.run(TOKEN)