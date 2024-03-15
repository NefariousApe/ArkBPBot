
import discord
import os
from dotenv import load_dotenv
from BPCalc import placeOrder, lookupBP

load_dotenv()

#! SWITCH TO PUBLISHED_TOKEN FOR MAIN BRANCH
TOKEN = os.getenv("PUBLISHED_TOKEN")
# f = open("BotToken.txt")
# token = f.read()


bot = discord.Bot()


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")


@bot.slash_command(name="blueprints", description="Returns the costs of a blueprint")
async def lookupBp(ctx, blueprint):

    bps = lookupBP(blueprint.lower())
    if bps == "Error":
        response = f'''
        There was an error processing your request.\nCheck that your input was matches a bp\nInput: {blueprint}
'''
        await ctx.respond(response)
    else:
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
    cost, parsedOrder, error = placeOrder(order.lower())
    if error == "Error":
        response = f'''
        There was an error processing your request.\nCheck that your input was matches a bp\nInput: {order}
    '''
        await ctx.respond(response)
    else:
        breakdown = ""
        for material, amount in cost.items():
            if amount > 0:
                breakdown = breakdown + f"## {material}: {amount}\n"
        await ctx.respond(f'''
        # Your Order (with tax): {parsedOrder}
        {breakdown}
    '''
        )

bot.run(TOKEN)
