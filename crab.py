# CRAB BOT
# DEVELOPED BY Siren#9889 FOR UP CIRCUIT, 2020
# REFER TO README BEFORE PROCEEDING

import discord
from discord.ext import commands, tasks
from itertools import cycle
import csv

# ----------------------------------------------------- #
# COMMAND_PREFIX CHANGES THE PREFIX OF THE BOT TO THE DESIRED CHARACTER. 
# e.g. if value is ".", bot will respond to ".help"
# ----------------------------------------------------- #

crab = commands.Bot(command_prefix=".")
status = cycle(["Status 1", "Status 2"])
stat = discord.Game(name=".help for info")
database = {}
t=10

# READS BUDDY PROFILES FROM CSV. REFER TO README FOR DETAILS

with open('./Buddy_Profiles/buddyprofiles.csv', 'r') as fl:
        reader = csv.reader(fl)
        for row in reader:
            row.append(True)
            row.append(0)
            row.append("")
            database[row[0]] = row
        # print("Done.")

# ----------------------------------------------------- #
# THIS FOLLOWING BLOCK OF CODE PRINTS TO YOUR TERMINAL. DO NOT INTERACT WITH THE BOT ON DISCORD UNTIL YOU SEE THE READY ON YOUR TERMINAL.
# ----------------------------------------------------- #

active_dict = []
crab.remove_command('help')
@crab.event
async def on_ready():
    print("Crab Ready.") 
    await crab.change_presence(status=discord.Status.do_not_disturb, activity=stat)

# ----------------------------------------------------- #
# THIS FOLLOWING BLOCK OF CODE IS THE MEAT OF THE CODE. ANY CHANGES MADE TO message.channel.send FUNCTIONS WILL CHANGE THE BOT'S RESPONSE.
# ----------------------------------------------------- #

@crab.event
async def on_message(message):
    if message.author.bot == False:
        if message.content.startswith("DIBS "):
            codename = message.content.split(" ", 1)[1]
            if codename == active_dict[0]:
                if database[codename][2]:
                    await message.channel.send(embed = discord.Embed(description = f"{message.author.mention} called **DIBS** on {codename}!", color = discord.Color.blue()))
                    database[codename][2] = False
                    database[codename][4] = message.author.display_name
                else:
                    await message.channel.send(embed = discord.Embed(description =f"{message.author.mention} - {codename} not available for dibbing!", color = discord.Color.blue()))
            else:
                await message.channel.send(embed = discord.Embed(description = f"Check buddy nickname spelling, {message.author.mention}.", color = discord.Color.blue()))
        if message.content.startswith("STEAL "):
            try:
                parameters = message.content.split(" ", 2)         # parameters = ['STEAL', 'AMOUNT', 'CODENAME']
                if parameters[2] == active_dict[0] and database[active_dict[0]][2] == False:
                    codename = active_dict[0]
                    if database[parameters[2]][3] < int(parameters[1]) and database[codename][4] != message.author.display_name and int(parameters[1]) % 20 == 0 and int(parameters[1]) <= 3000:
                        database[parameters[2]][3] = int(parameters[1])
                        await message.channel.send(embed = discord.Embed(description =f"{codename} stolen from {database[codename][4]} by {message.author.mention} for {database[parameters[2]][3]}", color = discord.Color.blue()))
                        database[parameters[2]][4] = message.author.display_name
                    else:
                        await message.channel.send(embed = discord.Embed(description =f"Hey {message.author.mention}! You might be trying to steal from yourself, or check your bid. Bids must be divisible by 20, capped at 3000.", color = discord.Color.blue()))
                else:
                    await message.channel.send(embed = discord.Embed(description =f"Hey {message.author.mention}! Check buddy nickname spelling, or buddy may not be up for stealing.", color = discord.Color.blue()) ) 
            except(IndexError):
                await message.channel.send(embed = discord.Embed(description =f"Hey {message.author.mention}! Check format, or buddy may not be up for stealing.", color = discord.Color.blue()))
    await crab.process_commands(message)



@crab.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid keyword.")
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(embed = discord.Embed(description ="You do not have permission to use this command."))

# ----------------------------------------------------- #
# RESPONSE/PING CHECKER
# ----------------------------------------------------- #
@crab.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(crab.latency * 1000)}ms")

# ----------------------------------------------------- #
# RESETS THE VALUE OF THE BUDDY IN CASE OF ERRORS. REQUIRES ELEVATED PERMISSIONS IN THE CHANNEL.
# ----------------------------------------------------- #

@crab.command()
@commands.has_permissions(administrator=True)
async def reset(ctx):
    database[active_dict[0]][2] = True
    database[active_dict[0]][3] = 0
    await ctx.send(embed = discord.Embed(description = f"Values reset for {active_dict[0]}!", color = discord.Colour.blue()))
    database[active_dict[0]][4] = ""

# ----------------------------------------------------- #
# TIME ANNOUNCER. THIS HAS TO BE MANUAL, AND RESPONSE CAN BE MODIFIED BELOW
# ----------------------------------------------------- #

@crab.command()
@commands.has_permissions(administrator=True)
async def announce(ctx):
    await ctx.channel.purge(limit=1)
    await ctx.send(embed = discord.Embed(title = f"**30 seconds left for {active_dict[0]}**!", color = discord.Colour.blue()))

# ----------------------------------------------------- #
# BEGINS BIDDING FOR BUDDY. REQUIRES ELEVATED PERMISSIONS.
# ----------------------------------------------------- #

@crab.command()
@commands.has_permissions(administrator=True)
async def begin(ctx, *, buddy):
    for i in range(5):
        active_dict.append(database[buddy][i])
    embed = discord.Embed(title = f"{buddy} now up for **dibbing**!", description = "", color = discord.Colour.blue())
    file = discord.File("Buddy_Profiles/" + database[active_dict[0]][1], filename="image.PNG")
    embed.set_image(url="attachment://image.PNG")
    await ctx.send(file=file,embed = embed)
    

def isxc(ctx):
    return ctx.author.id == 184985315159703552

@crab.command()
@commands.check(isxc)
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"{amount} messages deleted!")

# ----------------------------------------------------- #
# HELP COMMAND. IF ANY ADDITIONS ARE MADE TO THE BOT, MAKE SURE TO REFLECT IT HERE.
# ----------------------------------------------------- #

@crab.command()
async def help(ctx):
    embed = discord.Embed(title = "Useful Commands for Apps", description = "", color = discord.Colour.blue())
    embed.add_field(name = "DIBS", value = "Dibs for a buddy!", inline = True)
    embed.add_field(name = "Format:", value = "DIBS <buddy codename>", inline = True)
    embed.add_field(name = "\u200B", value = "\u200B", inline = True)
    embed.add_field(name = "STEAL", value = "Steal a buddy for a price! Increments of 20 pesos", inline = True)
    embed.add_field(name = "Format:", value = "STEAL <amount> <buddy codename>", inline = True)
    embed.add_field(name = "\u200B", value = "\u200B", inline = True)
    await ctx.send(embed = embed)
    
# ----------------------------------------------------- #
# THIS FOLLOWING BLOCK OF CODE IS FOR SENDING A DETAILED EMBED AND IS UNFINISHED. 
# CONTACT ME Siren#9889 OR REFER TO DISCORD PYTHON DOCUMENTATION IF THERE IS A DESIRE TO CONTINUE THIS.
# ----------------------------------------------------- #

# @crab.command()
# async def send(ctx):
#     # await ctx.channel.purge(limit=1)
#     embed = discord.Embed(title = active_dict[0], description = "", color = discord.Colour.blue())

#     file = discord.File(database[active_dict[0]][1], filename="image.PNG")

#     # embed.set_footer(text = "this is footer desuwa")
#     embed.set_image(url="attachment://image.PNG")
#     # embed.set_thumbnail(url="attachment://image.png")
#     # embed.set_author(name = "Buddy Profile:")
#     # embed.add_field(name = "HS Stereotype 1", value = "Emo goth", inline = True)
#     # embed.add_field(name = "HS Stereotype 2", value = "Art Hoe", inline = True)
#     # embed.add_field(name = "HS Stereotype 3", value = "Burnout", inline = True)
#     # embed.add_field(name = "Bakit ka dapat i-bid?", value = "akjsdfhbaskdjfhbasdfjkhbasdfjhb", inline = False)
#     # embed.add_field(name = "Bakit ka nagjoin sa U.P. Circuit?", value = "para more friends in lyf", inline = False)
#     # embed.add_field(name = "Hobbies and Interests", value = "acads, programming, gumala", inline = False)
#     # embed.add_field(name = "Free Schedule", value = "all day everyday", inline = False)
#     # embed.add_field(name = "Message for Future Buddy", value = "WOOOOOOOOOOOOOO", inline= False)
#     await ctx.send(file=file,embed = embed)

# ----------------------------------------------------- #
# THIS FOLLOWING BLOCK OF CODE IS FOR SETTING A TIMER FOR THE BID AND IS UNFINISHED. 
# CONTACT ME Siren#9889 OR REFER TO DISCORD PYTHON DOCUMENTATION IF THERE IS A DESIRE TO CONTINUE THIS.
# ----------------------------------------------------- #

# @crab.command()
# async def time(ctx): 
#     await ctx.send(f"Bidding for {active_dict[0]} Opened!")
#     while t:
#         time.sleep(1)
#     await end(ctx)

# ----------------------------------------------------- #
# ENDS THE BIDDING. REQUIRES ELEVATED PERMISSIONS.
# ----------------------------------------------------- #

@crab.command()
@commands.has_permissions(administrator=True)
async def end(ctx):
    channel = crab.get_channel(808255725516095519)
    await ctx.send(embed = discord.Embed(description = f"Bidding for {active_dict[0]} closed!", color= discord.Color.blue()))
    if database[active_dict[0]][4] != "":
        await ctx.send(embed = discord.Embed(title = "Congratulations!", description = f"{active_dict[0]}'s buddy is **{database[active_dict[0]][4]}**!", color= discord.Color.blue()))
        await channel.send(embed = discord.Embed(description = f"{active_dict[0]}'s buddy is **{database[active_dict[0]][4]}**!", color= discord.Color.blue()))
    active_dict.clear()

@crab.command()
async def whatsmyid(ctx):
    await ctx.send(embed = discord.Embed(description = f"Your ID is {ctx.author.id}, {ctx.author.display_name}", color= discord.Color.blue()))

# ----------------------------------------------------- #
# OUTPUTS THE RESULTS ONTO A CSV FILE IN THE SAME DIRECTORY AS THE BOT. UNFINISHED.
# ----------------------------------------------------- #

@crab.command()
async def write(ctx):  
    with open('results.csv','w', newline='') as resultFile:
        fileWrite = csv.writer(resultFile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for value in database.values():
            fileWrite.writerow(value)

# ----------------------------------------------------- #
# PLACE TOKEN AS A PARAMETER OF .run() WITH QUOTATION MARKS
# ----------------------------------------------------- #

crab.run("PUT TOKEN HERE")