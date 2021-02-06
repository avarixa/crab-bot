import discord
from discord.ext import commands, tasks
from itertools import cycle
import time, asyncio

crab = commands.Bot(command_prefix=".")
status = cycle(["Status 1", "Status 2"])
stat = discord.Activity(name="xd", type = discord.ActivityType.custom, details = "ayy")
active_dict = []
# Dictionary = "Codename" : [nickname, img url, available for dibbing, steal amount, buddy]
database = {"Buddy1" : ["Buddy1", "C:\\Users\\XC\\Pictures\\ajbf2r4bw7s31.png", True, 0, ""], "Buddy2" : ["Buddy1", "C:\\Users\\XC\\Pictures\\ajbf2r4bw7s31.png", True, 0, ""]
}
t=10

@crab.event
async def on_ready():
    print("Crab Ready.") 
    await crab.change_presence(status=discord.Status.do_not_disturb, activity=stat)

@crab.event
async def on_message(message):
    if message.author.bot == False:
        if message.content.startswith("DIBS "):
        #dibscheck 
            if message.content.split(" ", 1)[1] == active_dict[0]:
                if database[active_dict[0]][1]:
                    await message.channel.send(f"{message.author.mention} *CALLED DIBS ON* {active_dict[0]}")
                else:
                    await message.channel.send(f"{message.author.mention} - {active_dict[0]} not available for dibbing!")
            else:
                await message.channel.send(f"{message.author.mention} INVALID NAME! CHECK YOUR SPELLING")
        # if message.content.startswith("STEAL ") <STEAL amount codename>   
        #     if not(database[active_dict[0]][1]):
        #         if len(message.content.split(" ", 1)) == 2: 
        #             if message.content.split(" ", 1)[1] == active_dict[0]:
                    
    await crab.process_commands(message)

@crab.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid keyword.")
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have permission to use this command.")

@crab.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(crab.latency * 1000)}ms")

@crab.command()
@commands.has_permissions(administrator=True)
async def begin(ctx, *, buddy): #buddy = "Buddy1", "Buddy2"
    active_dict = database[buddy] #active_dict = ["Buddy1", "C:\\Users\\XC\\Pictures\\ajbf2r4bw7s31.png", True, 0, ""]
    await ctx.send(f"{buddy} now up for bidding!")

# @crab.event
# async def on_command_error(ctx, error):

def isxc(ctx):
    return ctx.author.id == 184985315159703552

@crab.command()
@commands.check(isxc)
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"{amount} messages deleted!")

# @tasks.loop(seconds=10)
# async def change_status():
#     await crab.change_presence(activity=discord.Game(next(status)))

@begin.error
async def clear_error(ctx, error):
    await ctx.send("Double-check params.")

@crab.command()
async def send(ctx):
    # await ctx.channel.purge(limit=1)
    embed = discord.Embed(title = "Buddy Codename", description = "", color = discord.Colour.blue())

    file = discord.File(database[active_dict[0]][0], filename="image.png")

    # embed.set_footer(text = "this is footer desuwa")
    embed.set_image(url="attachment://image.png")
    # embed.set_thumbnail(url="attachment://image.png")
    embed.set_author(name = "Buddy Profile:")
    # embed.add_field(name = "HS Stereotype 1", value = "Emo goth", inline = True)
    # embed.add_field(name = "HS Stereotype 2", value = "Art Hoe", inline = True)
    # embed.add_field(name = "HS Stereotype 3", value = "Burnout", inline = True)
    # embed.add_field(name = "Bakit ka dapat i-bid?", value = "akjsdfhbaskdjfhbasdfjkhbasdfjhb", inline = False)
    # embed.add_field(name = "Bakit ka nagjoin sa U.P. Circuit?", value = "para more friends in lyf", inline = False)
    # embed.add_field(name = "Hobbies and Interests", value = "acads, programming, gumala", inline = False)
    # embed.add_field(name = "Free Schedule", value = "all day everyday", inline = False)
    # embed.add_field(name = "Message for Future Buddy", value = "WOOOOOOOOOOOOOO", inline= False)
    await ctx.send(file=file,embed = embed)

@crab.command()
async def time(ctx): 
    await ctx.send(f"Bidding for {active_dict[0]} Opened!")
    while t:
        time.sleep(1)

    await end(ctx)

@crab.command()
async def end(ctx):
    await ctx.send(embed = discord.Embed(description = f"Bidding for {active_dict[0]} Closed!"))

@crab.command()
async def whatsmyid(ctx):
    await ctx.send(embed = discord.Embed(description = f"Your ID is {ctx.author.id}, {ctx.author.display_name}", color= discord.Color.blue()))

@crab.command()
async def demo(ctx):
    await ctx.send(embed = discord.Embed(title = "This is a title." ,description = "This is the description", color= discord.Color.blue()))



# @crab.command()
# @commands.check(isxc)
# async def extend(ctx):

crab.run("ODA1Nzk2MzIxNjU0MzQxNjky.YBgGTg.R7iO-A6xkkTHiyCg_blH4ShkrI4")