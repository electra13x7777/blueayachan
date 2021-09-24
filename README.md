╭━━╮╭╮╱╱╱╱╱╱╭━━━╮╱╱╱╱╱╱╱╱╱╭╮
┃╭╮┃┃┃╱╱╱╱╱╱┃╭━╮┃╱╱╱╱╱╱╱╱╱┃┃
┃╰╯╰┫┃╭╮╭┳━━┫┃╱┃┣╮╱╭┳━━┳━━┫╰━┳━━┳━╮╱╭━━┳╮╱╭╮
┃╭━╮┃┃┃┃┃┃┃━┫╰━╯┃┃╱┃┃╭╮┃╭━┫╭╮┃╭╮┃╭╮╮┃╭╮┃┃╱┃┃
┃╰━╯┃╰┫╰╯┃┃━┫╭━╮┃╰━╯┃╭╮┃╰━┫┃┃┃╭╮┃┃┃┣┫╰╯┃╰━╯┃
╰━━━┻━┻━━┻━━┻╯╱╰┻━╮╭┻╯╰┻━━┻╯╰┻╯╰┻╯╰┻┫╭━┻━╮╭╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯╱╰━━╯
## My third (and most functional) twitch IRC bot

### What is this?
blueayachan is a twitch IRC Bot with a more "iterative" (lazy) approach to it's design to maximize enjoyment for the user.

### Features!
* High speed "SFW" image scraping from Danbooru (Now with 100% more sauce!)
* Tons of gacha commands
* Lots of good memes
* User's can choose to omit commands they don't want to have in their channel (will eventually allow for this to be done in IRC)
* User level ability to add and remove their own channels to and from the bot with a single command (you don't have to ask me to add you!)

### "Good" Commands (there are more commands than just these but they probably suck)
#### Image Scraping
* !ayapic -  Queries safebooru and returns a link to a picture of Aya Shameimaru
* !maripic - Queries safebooru and returns a link to a picture of Marisa Kirisame
* !touhoupic - Queries safebooru and returns a link to a picture of a character from the Touhou™ series
* !tsukipic - Queries safebooru and returns a link to a picture of a character from tsukihime/melty blood. Can search for specific characters using the keywords for different tags. Find kewords with `!tsukipic -keys`
* !amepic - Queries safebooru and returns a link to a picture of Amelia Watson
* !etrianpic - Queries safebooru and returns a link to a picture from Etrian Odyssey
* !maypic - Queries safebooru and returns a link to a picture of May from Guilty Gear
* !dizzypic - Queries safebooru and returns a link to a picture of Dizzy from Guilty Gear
* !jampic - Queries safebooru and returns a link to a picture of Jam from Guilty Gear
* !idolpic - gets you an idol. i really don't know much about that stuff... 
* !mothmanpic - never scrapes images since there are like 2 mothman pics lol...
* !datapic - DataFace
* !fftpic - Queries safebooru and returns a link to a picture of art from the hit game Final Fantasy Tactics
#### Gachas
* !etrian - Returns an etrian class with witty flavor text
* !melty - Gives you a new main in Melty Blood: Actress Again Current Code
* !lumina - Gives you a new main in Melty Blood: Type Lumina
* !melee - Gives you a new main in SSB Melee
* !soku - Gives you a new main in Touhou 12.3 Hisoutensoku
* !hornedanimegacha - Returns a random horned anime of rarity 0 - 5 Stars
* !demongacha - Returns a random demon (currently only smt nocturne demons) of rarity 1 - 5 Stars
#### Music
* !etrianost - Sends a link to a random song from Etrian Odyssey and sends the title to the song
#### Misc/Quote
* !cfb - Generates a random text string using 'c', 'f', and 'b'
* !pasta - Returns a random copypasta (Has a 90 second timeout after each use on a "per-channel" basis)
* !dreamboumtweet - Returns a random tweet made by THE [@dreamboum](https://twitter.com/Dreamboum) on twitter
#### Join/Leave
* !joinch - Adds a user's channel to channels.txt and joins bot to channel if they are not in the file.
* !leavech - Removes user's channel from channels.txt.
#### Information
* !commandlist - Lists commands
* !infodump - Dumps info

### Special Thanks
It's pretty obvious, but this project was heavily inspired by bots that came before it.
* Botwoon by Dessyreqt
* FUNtoon by Taw_
* ZeppyZ by Kuribon
* Frigbot by Flameberger

These bots have all entertained me immensely over the years and I am very thankful to their creator's hard work to make such simple programs create such engaging user experiences.

### Contribution
Now that this has a repo I suppose I should actually clean up the codebase a bit and create some style guidelines. I will eventually get around to doing this as well as a detailed explanation of the file parsing formats and such. If you would like to help with the bot feel free to reach out and I'll start getting something together.

### Forking
As this is Free Software, feel free to fork this repository and use the code to write your own bot. (Obviously you will have to do heavy modification since you can't use the credentials I use for my own bot)

### Contact Me!

* [Twitch](https://www.twitch.tv/electra_RTA)
  
* [Twitter](https://twitter.com/electra_rta)
