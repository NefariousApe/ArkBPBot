
import discord
import os
from dotenv import load_dotenv
from BPCalc import placeOrder, lookupBP

load_dotenv()

#! SWITCH TO PUBLISHED_TOKEN FOR MAIN BRANCH
TOKEN = os.getenv("DEVELOPMENT_TOKEN")
# f = open("BotToken.txt")
# token = f.read()


bot = discord.Bot()


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.slash_command(name="blueprints", description="Say hello to the bot")
async def lookupBp(ctx, blueprint):

    bps = lookupBP(blueprint.lower())
    response = ""
    for bp in bps:
        response = response + f'''
        # {bp["Rarity"]} {bp["Name"]}\n
'''
        for k, v in bp.items():
            if v != None and (k != "Rarity" and k != "Name"):
                response = response + f'''
                ## {k}: {v}\n
'''

    await ctx.respond(response)


@bot.slash_command(name="order", description="Place an order for bps")
async def order(ctx, order):
    cost, parsedOrder = placeOrder(order.lower())
    breakdown = ""
    for material, amount in cost.items():
        if amount > 0:
            breakdown = breakdown + f"## {material}: {amount}\n"
    await ctx.respond(f'''
    # Your Order (with tax): {parsedOrder}
    {breakdown}
''')

bot.run(TOKEN)
