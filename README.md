# **CRAB BOT**
### MADE BY XC ENRIQUEZ 2020

You are only expected to open the `Buddy_Profiles` folder and the `crab.py` file. The rest of the folders are dependencies to make the release portable. If an error occurs, consider running
```
pip install discord
```
on your terminal. Once this is done, delete all of the folders except `Buddy_Profiles`.

### How To Use:

#### Step Zero - Inviting the Bot
If this bot is not yet in the server you wish to use it on, personally contact me for an invite link.

#### Step One - The Discord Bot Token
You will need a Discord bot token. Personally contact me (Siren#9889) for the bot's token and paste it on the last line of `crab.py`.

If the token is ABC123, the last line of `crab.py` **must** be
```
crab.run("ABC123")
```

#### Step Two - Preparing the files
Place all buddy profiles in image format inside the `Buddy_Profiles` folder. 


Make a `.csv` file containing the **Buddy Nickname** on the **first column** and the **Buddy Profile Filename** on the **second column**. Note that the nicknames on the first column will be used to invoke the bidding. 


**FILENAMES ARE CASE-SENSITIVE** including the file extension, so make sure the filename is **exact**.


The following screencap assumes that the files `Buddy 1.PNG` and `Buddy2.png` both exist.
The bidding for these two can be invoked with
```
.begin Buddy 1
```
and
```
.begin Buddy2
```
respectively, assuming default settings.

!["csv screencap"](https://i.imgur.com/82BwLZV.png)

The filenames do not need to be exactly the same as the buddy nickname - `Buddy 2 != Buddy2`

### You're done!
More bullets will follow, but they are all optional.

#### "What does this do?"
Function descriptions are commented inside the `crab.py` file.

#### Changing the bot responses
Changing what is inside the .send() functions will change the bot responses. Refer to the `crab.py` for more details.

#### Unfinished Functions and Calls
There are unfinished functions and calls in the file. Feel free to finish them. Documentation can be found in https://discordpy.readthedocs.io/en/latest/api.html