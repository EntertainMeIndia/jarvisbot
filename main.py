import discord
from discord.ext import commands
import openai

openai.api_key = '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'

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.command()
async def chat(ctx, *, user_input):
    response = unleash_jarvis("User: " + user_input + "\nJarvis:")
    await ctx.send(f'Jarvis: {response}')


def unleash_jarvis(prompt):
    try:
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.6,
        )

        if len(response.choices) > 0:
            return response.choices[0].text.strip()
        else:
            return "I'm sorry, but I'm unable to generate a response at the moment. Feel free to try again later!"
    except openai.error.RateLimitError:
        return "I'm sorry, but it seems that I've been occupied with numerous requests. Please bear with me and try again later."


bot.run('MTA4NjE0OTg0ODM0MTk0MjI3Mg.Gz-d6J.QLPtN70Hr7hV8ITqTwRGyppoAicgDpjMHF0mrk')
