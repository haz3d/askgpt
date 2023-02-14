import discord
import openai
from discord.ext import commands
from openai.api_key import API_KEY

client = commands.Bot(command_prefix='/')

# Authenticate with OpenAI API
openai.api_key = API_KEY

@client.event
async def on_ready():
    print(f'{client.user} is ready!')

@client.command()
async def askgpt(ctx, *, input):
    # Use the OpenAI API to generate a response
    response = await generate_response(input)

    # Send the response back to the user
    await ctx.send(response)

async def generate_response(input):
    # Use the OpenAI API to generate a response
    prompt = f"Q: {input}\nA:"
    completions = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop="\n"
    )
    response = completions.choices[0].text.strip()

    return response

client.run('YOUR_DISCORD_BOT_TOKEN')
