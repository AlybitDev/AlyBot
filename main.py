import discord
from openai import OpenAI
import asyncio

async def keep_alive():
    while True:
        await asyncio.sleep(60)

client_ai = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="your-openrouter-api-key"
)

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        asyncio.create_task(keep_alive())

    async def on_message(self, message):
        if message.author == client.user:
            return
        elif isinstance(message.channel, discord.DMChannel):
            completion = client_ai.chat.completions.create(
                extra_body={},
                model="ai-model",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": message.content
                            }
                        ]
                    }
                ]
            )

            await message.channel.send(completion.choices[0].message.content)

        elif client.user.mentioned_in(message):
            completion = client_ai.chat.completions.create(
                extra_body={},
                model="ai-model",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": message.content
                            }
                        ]
                    }
                ]
            )

            await message.channel.send(completion.choices[0].message.content)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run("discord-bot-token")
