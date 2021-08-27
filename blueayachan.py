'''
Project: BlueAyaChan - Twitch IRC Bot
File: blueayachan.py
Author: Alex Barney
'''
import async_timeout
import twitchio.dataclasses
from twitchio.ext import commands
#from twitchio.ext import
from pybooru import Danbooru, Moebooru
from googletrans import Translator
from datetime import datetime, timedelta
import random
import asyncio
import time
import os
#import re
#import os
'''
                                            GLOBALS
'''
#timer = time.sleep(60)
last_pasta_call = datetime.now()

ha_list = [
            "HornedAnime",
            "CornedAnime",
            "PiratedAnime",
            "HornyAnime",
            "HornedAnimeTangledUpInChristmasLights",
            "TrippyAnime",
            "ShivvedAnime",
            "ShakingAnime",
            "HornedAnimeWithPantiesOnHerHead",
            "HornedAnimeButShesAGarbageCan",
            "HornedAnimeWithCabbageOnHerHead",
            "HornedAnimeWithPantiesOnHerHeadLookingOutHerWindow",
            "HornedAnimeWithPeachOnHead",
            "HornedAnimeWithChuckOnHerHead",
            "HornedAnimeWithRunGoing",
            "HornedAnimeWithShieldOnHead",
            "HornedAnimeWithNoWeebsAllowed",
            "HornedAnimeWithAllProsthetics",
            "HornedAnimeWithMossOnHerHead",
            "HornedAnimeWithGadgetOnHerHead",
            "HomedAnime",
            "HornlessAnime",
            "HornedAnimeWearingAFedora",
            "HornedAnimeWithSocksOnHerHorns",
            "HornedMiniDonuts",
            "HornedAnimeWearingHerVariaSuit",
            "HornedSlayer",
            "HornlessSpin",
            "HornedVN",
            "HornedAnimeWithBurgyOnHerHead",
            "HornedAnimeWithAnimeDreamingOfWRSleepingBehindHerHorns",
            "HornedGrimChamp"
] #horned animes | TODO: parse from file
pasta_str = [
            'Hey TheClaude sorry to bother you. When you said "FFMQ sub2 is impossible" do you mean you speedrun the game, or are you a mod on speedrun.com and never see sub-2 runs submitted? Just curious =)',
            "Hey TheClaude sorry to bother you. When you said" + '"1.3 is finished"' + " do you mean you completed the game, or are you the creator of 1.3 and that's an old message? Just curious =)",
            "Hey claude. I see youre already up 3 minutes. What new gameshark code/" + '"route change"' + " are you using this time?",
            "Hey Clod, I hope you can see this message now that the chat has died down. I wanted to say congrats! I know you can do a little bitter but I always want to tip my hat off to you. Through thick and thin I will still be here to always support you. I know times are hard, but you always come back with a good attitude. I wish you the very best on your next runs, and hope you get an even better score. I will continue to be here and find new strats as always. Great job stiv. I am rooting for you always",
            "Hey Claude, I'm currently watching the stream with my 5 year old son, now I don't mind all the cursing but can you please stop the bad camera rotations? I don't want my son to learn how to suck at fft speed run",
            "I owe my life to Claude. I was in a coma for 6 months after a terrible car crash. One day my nurse turned on the T.V. to Claude's stream, so I got up and muted it.",
            "No, you can't. Using an instant win attacks is the only thing you can't do in a Speed Run. Just like Zanmato in FFX. Why, you may ask? Because we use skills, speed and strategy in a Speed Run, and an instant win attack isn't a strategy. We have discussed this matter, and our conclusion is that you can achieve a better result by using the Slots, but not a much better one.",
            "Maths skills are too op, but using wizards who have all skills due to a bug is not op? I'm always disappointed in speed runs that break the game unrealistically to achieve a useless goal. How about play the game as intended and learn to use legitimate strategies to progress through the game. I understand this is common in the speed run community. Props to the speed runner but I would like to see the community grow and really show talent.",
            "waffle42 isn't so great? Are you kidding me? When was the last time you saw a player with such an ability and movement with Diddy? waffle puts the game in another level, and we will be blessed if we ever see a player with his skill and passion for the game again. V0oid breaks records. fis breaks records. waffle42 breaks the rules. You can keep your statistics. I prefer the magic.",
            "You know they say all men are created equal, but you look Mill and you can see that statement is NOT TRUE! See, normally if you go one-on-one with another gamer you got a fifty/fifty chance of throwing the daily. But I'm a genetic freak, and I'm not normal! So you got a 25 percent at best at throwing! And then you add Midboss to the mix? You-the chances of throwing drasticy go down. See, the 3-Way at V0oidathon, you got a 33 and a third chance of throwing. But I! I got a 66 and two thirds chance",
            "Yeah, fuck off buddy we absolutely need more waffle races. Fuckin every time this kid steps on SRL someone's bopped. kids fuckin dirt nasty man. Does fuckin Reflected have thirteen 40s this season I dont fuckin think so bud. I'm fuckin tellin ya Waffle" + ' "golden flow" ' + "42 is pottin 39 in '17 fuckin callin it right now. Clap bombs, fuck moms, wheel, snipe, and fuckin celly boys fuck",
            "you've seen waffle play, but have you seen him drink? the man can down a gallon of bleach in the time it takes him to reset on lockjaw, and let's not even mention his off-stream world record for 69 fakes in a row... I don't care who has the most points, waffle is the true winner",
            "CLAUDE (AGRADECE AL AGUA EN AGUJA) ME HACE SENTIR MAL QUE NO HAYA TIEMPO. PORQUE LA GENTE MIRA MI TIEMPO Y PIENSAN QUE SOY TERCEROS EN EL MUNDO, Y TENGO QUE SALIR DE MI MANERA PARA DECIR" +' "NO, ES MÁS PEQUEÑO QUE USTED CREE QUE ES"' +". ¡¿SENSACIÓN?! TENGO QUE SALIR DE MI MANERA DE DECIRLE A TODOS LOS QUE MIRAN A MI TIEMPO," +' "OH, LO SIENTO, NO ME TENGO LO BUENO QUE USTED PIERDE"'+".",
            "t ｈｅｎ ｉ ｓｅｅ ｍｅｔａｌ ｓｌｉｍｅ， ｍｙ ｈａｎｄ ａｕｔｏｍａｔｉｃａｌｌｙ ｇｏ ｔｏ ｔｈｅ ｄｉｃｋ． ｉ ｓｔｒｏｋｅ ｔｈｅ ｄｉｃｋ ａｎｄ ｆｅｅｌ ｉ ｈａｖｅ ｓｅｘ ｗｉｔｈ ｔｈｅ ｄｑ３． ａｌｌ ｂｅｃｏｍｉｎｇ ｗｏｒｌｄ ｒｅｃｏｒｄ",
            "Greet every customer as they enter your store/channel. For example, lets say a potential customer named ‘Peaches’ enters the chat. Don’t just say “Hello Peaches” since that isn’t personable. Instead what you should say is “Hello Peaches, how is your big rig?” By asking about their personal life, they will feel like you actually care about it. This is a key aspect of streaming biger.",
            "CLAUDE (ANGRILY CHUGS WATER) IT MAKES ME FEEL BAD THAT YOUR TIME’S NOT UP. BECAUSE PEOPLE LOOK AT MY TIME, AND THEY THINK I’M THIRD BEST IN THE WORLD, AND I HAVE TO GO OUT OF MY WAY TO SAY “NO, I’M WORSE THAN YOU THINK I AM.” YOU KNOW HOW THAT MAKES ME FEEL?! I HAVE TO GO OUT OF MY WAY TO TELL EVERYBODY WHO LOOKS AT MY TIME, “OH SORRY, I’M NOT AS GOOD AS YOU THINK I AM.” CUZ THERE’S THIS RANDOM PERSON WHO WON’T POST HIS TIME",
            "just a reminder that the claude should not be winning he is an enemy of peace and justice, a force of evil in the universe. please raise your arms and transfer your spirit energy so that we may charge the spirit bomb to obliterate this plight on the universe.",
            "I just feel like because I'm good at all 3 games, people should kinda.... i dunno.... show some respect, i guess? But they don't. They don't care. And the #dkc IRC is just like... " + "Hey, what's up, let's talk about like pointless shit that has nothing to do with Donkey Kong, and let's ignore new people that come into the IRC, and who actual legitimate questions. And besides the community being a bunch of assholes.... like, it"+"'"+"s a good game... But. the community is awful... one of the worst.",
            "l i t t l e m o n e y",
            "THIS is why math skilling wizards is NOT the ultimate team...1.joined easy story battle in chapter 3... the one with Olan 2. A Theif charms one of my female math skill wizards... 3. her turn comes before any of my other chars turns4 ct5 flare on my entire party... 5. me=O_o",
            "Have you seen him dig before? he's got the perfect form, the most pristine technique, and the optimal build. You really can't do much better than LCC when it comes to striking the ground with a well crafted spade. A true connoisseur of the shovel.",
            "This is not speed run. it's like use cheating: you are use holes in textures, etc. you cross half game over the air. this? is not honestly, I think. IMHO - this is not rightly - to go like it. It is immitating of complete of the game. Sure - you make global and cosmical work. You are exxellent spec. But it is not speed run...And the end is sux. And one of you has problem - hi is looking for the asses. For Doggy-doggy ass too. how old him? 11? 12?But it was looking perfect. Not game - speed!",
            "One cannot simply just vote yes. To be a" + ' "Yeschad"' + ", one must contemplate the very essence of voting yes. You must live YES, breath YES, eat YES, even fuckin shit YES dude. If you only vote yes for odds FUCK YOU you don't deserve the title "+'"Yeschad"'+" you are just a lame nocuck poser moonlighting as the superior specimen that is the yeschad.",
            "Hello, my name is Luzbelheim and I've been doing speedruns for like 2 years approximately. The main reason I'm here is because I need your support, and in exchange for that, I will put my speedruns at your disposal. In other words, you will decide what game I have to play and try to do the World Record.",
            "sqpat lay on his deathbed, surrounded by his loyal stream viewers. He had memorized all 2,136 relevant kanji, traveled to every country on Earth, and created over 100 mobile phone games (at least 10 of them bug-free). His final words before he passed on from this mortal coil:"+' "Almost done with ZAVAS, guys"'+ ".",
            f"I'll start this with theclaude owes me nothing. He doesn't owe any of us anything. He's a professional gamer/twitch streamer. With that being said I got into watching speedrunning after watching the sub 4 run. Then 2016 happens and i begin to wonder if i started following theclaude too late.",
            f"Tell the truth, most of claude's PBs so far are fraudulent records that have been edited. By the way, his real PB of DKC1 is 8:09. He didn't want to say. Also he is trying to PB in Kick Master 100%,but mention of whether it is a fraudulent or not is undecided. How you receive this is up to you.",
            f"Hey, Klosty! What's up, man? It's the puke in your bed. I didn't know you were some kind of internet superstar hahahaha. Clean me up, man. Btw, did you ever hook up with Ashley? She was a big girl hahah. You are such a dog. It's so cool to see you again. You're literally on top of me. Just clean me up, man.",
            f"Claude (thanks for the water in the needle) makes me feel bad about not having time. People look at my time and think I'm a third party in the world, so I have to get out of my way to say " + '"No, it"'+ "'" + 's smaller than you think"' + " Hmm. sense? !! I have to leave my way and say to everyone watching at my time, " + '"I'+"'"+'m sorry, you haven'+"'"+'t lost anything."',
            f"sqpat17 I am nominating this stream for disappointment of the year. I've waited my entire life to watch you play Last Armageddon, because it's the only PC-88 game I've ever heard of thanks to a PCE version of one of the songs I heard on Youtube once and / or because Macaw played it. And what do you do? Spam EZ mode kill everything lightning move with your Cyclops and abuse the 2800 / 280 damage weapon (it scrolled too fast for me to see). Worst Zarbon Day ever.",
            f"these memes are going downhill fast. the first few were both spicy and original. like i legitamately laughed out loud. these new ones are getting weak. like I don't get it either, the guy seems downright unassuming, just playing the game. People are just apparently utterly obsessed with saying weird stuff about him. This guy....",
            f"Claude 925 (born July 21, 925) is a popular lets player[1][2] and occasional speedrunner[3][4][5]. Claude is an accomplished Super Mario RPG and Final Fantasy: Mystic Quest speed runner and is one of very few runners to reach a sub 2 hour time in Final Fantasy Mystic Quest. Controversy: According to speedrun.com [9][10] Claude does not have a sub 2 hour time in Final Fantasy Mystic Quest. This is due to observed irregularities in his splits and timing.",
            f'Some viewers have also accused the Claude of using glitches[citation needed] in certain speed runs. Because of the difficult nature of classifying glitches, this has been difficult to prove.',
            f"WOW you play CALCULATOR? That's like, SO COOL! I love her diverse set of tools, such as math skill in neutral, math skill in a blockstring, math skill on the enemy's wakeup, math skill as an anti-air, math skill as a backdash read, math skill trading favorably in every possibly situation, and when she does the mech hand assist in combos.",
            f"Please for the fuck of fuck no shitty venus shield strats. Save 7 seconds over the same potential insta deaths anyway. Save gold for 67 cures or learn to early fireburg before ice golem. Better investments.",
            f"This is the first time ever in my speedrunning career I accuse someone of cheating. I have and have had many world records in the Final Fantasy series. If I don't have a WR I have the 2nd or 3rd place most of the time. I love RPG speedrunning. I have never seen any top time in the FF series being done with cheats.",
            f"Such an amazing soundtrack. It's too bad you probably weren't able to enjoy it since you went so fast through all the levels. And skipped some.",
            f"If there’s a better game out there than Link to the Past, I've definitely played it. Nintendo has created, for me, the worst game of all time. It's nothing I want from a game and one of the most unrewarding experiences I've ever had.",
            f'yo Claude. I was watching the FFT TAS and had someone translate the broadsword-dagger swap part. This is what it says roughly "If this game is played quickly, to fight the enemy, the weapon will be bugged and turn into a different weapon. After the RNG adjustment, buffer then cancel. Fight with the fastest attacker then use this bug to obtain the broadsword"',
            f"If there’s a better speedrun out there than DKC3 Any% J, I haven’t played it. The Japanese TAS-er who found Bleak Skip has created, for me, the greatest speedrun of all time. It’s everything I want from a speedgame and one of the most rewarding experiences I’ve ever had.",
            f"The difference between irc and discord is that i like everyone on irc, isn't bogged down by a bunch of unwanted features, down't force memes on me, doesn't have avatars and pictures everywhere, has more customizable layout and colour, uses less memory and processing power, doesn't by default let everyone know what game i'm playing, has been around for ages, and isn't a gay piece of shit",
            f"Hey, Claude! What's up, man? It's your Megaman X2 Let's Play. I didn't know you were some kind of speedrunner hahahaha. Finish me, man. Btw, did you ever plan to play X3 next? Sure is worse than X2 hahah. You are such a fraud. It's so cool to see you again. You're literally wasting your time playing rando. Just finish me, man.",
            f"I mean, I get along with most people, but... I dunno... it's... not a good community. Been a few people told me that used to speedrun this game, that that's why they quit. That's understandable... but it's whatever. It's mainly a community of friends, more than like a community of people that care about the game. A bunch of elitists... and their little circlejerks.",
            f"A lot of us would love to see the DKC series on this site, and some of us refuse to use the current DKC leaderboards site, even though it really isn't bad; it just feels more inconvenient. I'd like to run this, as it's one of my favorite games, but I like to keep all of my speedruns in one place(my profile here), and submitting it to the lower-profile DKC site seems a bit counter-intuitive.",
            f"ｗｈｅｎ Ｉ ｓｅｅ ＦＦＴ， ｍｙ ｈａｎｄ ａｕｔｏｍａｔｉｃａｌｌｙ ｇｏ ｔｏ ｔｈｅ ｍｏｎｓｔｅｒ ｄｉｃｔ． ｉ ｒｅａｄ ｔｈｅ ｄｉｃｔ ａｎｄ ｆｅｅｌ ｉ ｈａｖｅ ｇａｌａｘｙ ｓｔｏｐ ｗｉｔｈ ｔｈｅ Ｏｌａｎ， ａｌｌ ｂｅｃｏｍｉｎｇ ＡＧＤＱ ｒｅｊｅｃｔ",
            f"If Tide 👧 😍 and LCC 🐒 both streaming RoF 😱 👋 and I can only watch one 😤 😬 Catch me at Tide's stream 😔 👻 🌹 with my 🔫 out 😏 💯 😎 🍆",
            f"Hi Claude! I've stopped by to tell you that Skyler, the prince formally known as your son, has been defeated! Using my niche detective skills, I have exposed him of his speedcrimes. Since our boy has not shown up for Donkey Court, he was banished from the DKCWiki for good! No need to thank me! I'll be awaiting your let's play of A Link to the Past as a token of your gratitude.",
            f"Hey, Claude. Can you explain the rivalry between you and SonVaan? I've asked him but he said"+ '"wtf idk"' + " as i recal",
            f"hryougi i'm new who play? I spent a day practicing the corner knife loop and I got it once so I think I'm ready to play some actual matches. If you are wondering I picked H-ryougi because I love the kara no kyoukai movies and I saw a japanese combo movie with half moon doing a bunch of cool combos(like the knife loop I mentioned earlier) so I picked this moon of ryougi so I can do cool combos as well. Hope we have fun matches.",
            f"WOW you play MAY? That's like, SO COOL! I love her diverse set of tools, such as totsugeki in neutral, totsugeki in a blockstring, totsugeki on the enemy's wakeup, totsugeki as an anti-air, totsugeki as a backdash read, totsugeki trading favorably in every possibly situation, and when she does the mech hand assist in combos.",
            f"WOW you play MECH? That's like, SO COOL! I love her diverse set of tools, such as bababa in neutral, bababain a blockstring, bababa on the enemy's wakeup, hammer as an anti-air, bababa as a backdash read, bababatrading favorably in every possibly situation, and when she does the rocket launcher BNB in combos",
            f"ｗｈｅｎ S M T P o r t u g a l p o s t s a b o u t T h e S i l v e r C a s e， ｍｙ ｈａｎｄ ａｕｔｏｍａｔｉｃａｌｌｙ ｇｏ ｔｏ ｔｈｅ r e t w e e t． ｉ ｒｅａｄ ｔｈｅ t w e e t ａｎｄ ｆｅｅｌ ｉ ｈａｖｅ a ç a í ｗｉｔｈ ｔｈｅ s a m b a， ａｌｌ ｂｅｃｏｍｉｎｇ m u i t o r e a l",
            f"LCC, there's something I've been meaning to talk to you about, and, it's kinda the elephant in the room here. I want you to take what I say to heart. I think you're getting too invested in, um, Portuguese SMT Twitter, and I feel like you need to hear it coming from me, to like, really have it have any impact on you. Sorry if this is awkward, and sorry I'm bringing this up in front of a lot of people, but like, you need help man. There, I said it.",
            f"Cha0s, there's something I've been meaning to talk to you about, and, it's kinda the elephant in the room here. I want you to take what I say to heart. I think you're getting too invested in, um, FF14 Triple Triad, and I feel like you need to hear it coming from me, to like, really have it have any impact on you. Sorry if this is awkward, and sorry I'm bringing this up in front of a lot of people, but like, you need help man. There, I said it.",
            f"BJW, there's something I've been meaning to talk to you about, and, it's kinda the elephant in the room here. I want you to take what I say to heart. I think you're getting too invested in, um, Korone, and I feel like you need to hear it coming from me, to like, really have it have any impact on you. Sorry if this is awkward, and sorry I'm bringing this up in front of a lot of people, but like, you need help man. There, I said it.",
            f"amy, there's something I've been meaning to talk to you about, and, it's kinda the elephant in the room here. I want you to take what I say to heart. I think you're getting too invested in, um, Ame, and I feel like you need to hear it coming from me, to like, really have it have any impact on you. Sorry if this is awkward, and sorry I'm bringing this up in front of a lot of people, but like, you need help man. There, I said it.",
            f"May, there's something I've been meaning to talk to you about, and, it's kinda the elephant in the room here. I want you to take what I say to heart. I think you're getting too invested in, um, 🐬 TOTSUGEKI 🐬 , and I feel like you need to hear it coming from me, to like, really have it have any impact on you. Sorry if this is awkward, and sorry I'm bringing this up in front of a lot of people, but like, you need help man. There, I said it.",
            f"Claude, there's something I've been meaning to talk to you about, and, it's kinda the elephant in the room here. I want you to take what I say to heart. I think you're getting too invested in, um, winning festival, and I feel like you need to hear it coming from me, to like, really have it have any impact on you. Sorry if this is awkward, and sorry I'm bringing this up in front of a lot of people, but like, you need help man. There, I said it.",
            f"Dreamboum, there's something I've been meaning to talk to you about, and, it's kinda the elephant in the room here. I want you to take what I say to heart. I think you're getting too invested in, um, Yasumi Matsuno, and I feel like you need to hear it coming from me, to like, really have it have any impact on you. Sorry if this is awkward, and sorry I'm bringing this up in front of a lot of people, but like, you need help man. There, I said it.",
            f"Iateyourpie, there's something I've been meaning to talk to you about, and, it's kinda the elephant in the room here. I want you to take what I say to heart. I think you're getting too invested in, um, Streaming Big, and I feel like you need to hear it coming from me, to like, really have it have any impact on you. Sorry if this is awkward, and sorry I'm bringing this up in front of a lot of people, but like, you need help man. There, I said it.",
            f"(streamer), there's something I've been meaning to talk to you about, and, it's kinda the elephant in the room here. I want you to take what I say to heart. I think you're getting too invested in, um, (stream title), and I feel like you need to hear it coming from me, to like, really have it have any impact on you. Sorry if this is awkward, and sorry I'm bringing this up in front of a lot of people, but like, you need help man. There, I said it.",
            f"Albrecht there's something I've been meaning to talk to you about, and, it's kinda the elephant in the room here. I want you to take what I say to heart. I think you're getting too invested in, um, bep, and I feel like you need to hear it coming from me, to like, really have it have any impact on you. Sorry if this is awkward, and sorry I'm bringing this up in front of a lot of people, but like, you need help man. There, I said it.",
            f"V0oid, there's something I've been meaning to talk to you about, and, it's kinda the elephant in the room here. I want you to take what I say to heart. I think you're getting too invested in, um, rambi hate, and I feel like you need to hear it coming from me, to like, really have it have any impact on you. Sorry if this is awkward, and sorry I'm bringing this up in front of a lot of people, but like, you need help man. There, I said it.",
            f"HyruleHero, there's something I've been meaning to talk to you about, and, it's kinda the elephant in the room here. I want you to take what I say to heart. I think you're getting too invested in, um, not speedrunning, and I feel like you need to hear it coming from me, to like, really have it have any impact on you. Sorry if this is awkward, and sorry I'm bringing this up in front of a lot of people, but like, you need help man. There, I said it.",
            f"BJW, dewe's somefing I've been meaning tuwu tawk tuwu yuwu about, and, it's kinda de ewephant in d-de woom hewe. invents nose I want y-yuw tuwu take what I say to heawt. I-I think you'we getting too invested in, um, Kowone, and I feew wike yuu need tuwu heaw it coming fwom me, tuwu wike, weawwy hawv it have any impact on you. Sowwy if dis is awkwawd, awnd sowwy I'm b-bwinging dis up in fwont of a wot of peopwe, but wike, yuwu need hewp man. ^_^ Dewe, I said it. OwO",
            f"Cyghfer, there's something I've been meaning to talk to you about, and, it's kinda the elephant in the room here. I want you to take what I say to heart. I think you're getting too invested in, um, The Legend of Zelda: A Link to the Past Speedrun, and I feel like you need to hear it coming from me, to like, really have it have any impact on you. Sorry if this is awkward, and sorry I'm bringing this up in front of a lot of people, but like, you need help man. There, I said it.",
            f"Ruckus applause fill the audience. The atmosphere rises to a fever pitch, as Manny Pardo says the line. Women weep and begin to give birth. The conception is instant.",
            f"even in 2021, hotline refuses to quit. no matter how many times we think this game will finally kick the bucket, it always finds a way to crawl it's way back from the brink of it's much needed demise. someone just HAS to pardo post this or richard deathless that, and necro this shit tier meme every year this game will never fucking die. pardochads, we kneel.",
            f'its raidenomics - I am not being critical bc its super easy to watch someone do an rts and say "you should do X, Y, Z"- but they raided you early and messed with your eco and you didnt turtle enough to stop it or punish them with counter raids - so they got ahead of you (not a knock - it happens)',
            f"Hey 2dos why don't you play DK64 anymore? I think it's pretty fkin rude how you're acting right now. Most people only follow for your DK64 and you're losing followers tonight acting like a child.",
            f"I'm saying it is straight up not possible. You could tone it down just a bit to make it possible while still being very hard. As is, gym leader 8 ace is level 75, and champion ace is 95. There is simply not enough exp in the game to keep up with that scaling. 100% fact, not just me complaining, promise.",
            f"You guys keep ridiculing me, but just wait until you reach the Elite 4 if you even can. That's when the level curve goes sky high. And I'll be there to say I told you so. The math is never wrong.",
            f"Electra_RTA, there's something I've been meaning to talk to you about, and, it's kinda the elephant in the room here. I want you to take what I say to heart. I think you're getting too invested in, um, pasta commands, and I feel like you need to hear it coming from me, to like, really have it have any impact on you. Sorry if this is awkward, and sorry I'm bringing this up in front of a lot of people, but like, you need help man. There, I said it.",
            f"Utsuho is by far the most atmospheric final boss to ever grace this series. Everything about the battle fits really well together: the music, the annoyingly bright radioactive bullets, the gigantic sun bullet danmaku, and the... whatever that is in the background, the nuclear symbol with the cat on it. To put it simply, it's intense.",
            f"mpghap, there's something I've been meaning to talk to you about, and, it's kinda the elephant in the room here. I want you to take what I say to heart. I think you're getting too invested in, um, doing challenge runs in Shin Megami Tensei III Nocturne, and I feel like you need to hear it coming from me, to like, really have it have any impact on you. Sorry if this is awkward, and sorry I'm bringing this up in front of a lot of people, but like, you need help man. There, I said it.",
            f"The romance is completely ruining FFT. Cause there have six girl love Ramza. I just want to say if the story wanna have romantic drama, only one girls in love with Ramza. Not fucking six girl, that is more like a drama for ecchi anime. (many girl love one guys). Also you guys should remember Ramza cheating the last fight in FFT world. His hp goes to 0. I feel like hell nooo!!!. But nope, Ramza is not dead his eye turn to yellow and win the fight... My friend laugh so hard at that scene. LOL.",
            f"Claude is a great gamer and speedrunner. Loved his commentary on the DKC trilogy relay race at AGDQ. Such a funny and knowledgable guy.",
            f"I think I'm about to give up on making speedfriends. No one talks to me or remembers me from previous chats/streams. It seems like the only way you get included is if you're an oldboy with a forum account on SDA or something. Fuck this...seriously. I'm over trying to make friends with these autists....what was I thinking? What a waste of my time.",
            f"Join hook girl on her journey to find her senpai, propelling her across the world and even to the far reaches of the galaxy. Buzzsaws, electric currents, and killer whales will attempt to thwart her mission, but like any other anime girl, she's as determined as she is cute. From the same team that brought you Super Hook Girl comes the anime coming-of-age story of the century; you don't want to miss it.",
            f"Another month, another cluster of Touhou fans that discover this forum and continue to clog it with drivel. I look forward to your overly sarcastic posts, meme picture responses, and creative vocabulary with more words like" +' "shitposter" and "butthurt." ' + "I applaud you at least for not responding with a picture slathered with humorous text. You'll stick around for a few more months, maybe, then you'll depart and find a new internet fad that wavers your attention and your lust for more derivative Japanese pop-culture that is the perfect mix of slightly underground, yet still accessible for the budding youth who dares to be different. Who knows, maybe you'll stick around to further white knight other Touhou fans in distressful situations that keep getting picked on for drab attempts at humor, pedantic inputs during their first few posts, or for resurrecting old threads to rant because 4chan won't listen. Godspeed you, fine patron of the internet. I hope you find what you're looking for.",
            f"This is not the run. If these words could possibly describe the amount of negativity in my body right at this very moment, your screen would shatter in shock. This whole run is a joke. There's been tons of fuck ups everywhere, the sole reason he's ahead right now is due to his abomination of a previous run. He's also a complete and utter choker in intense situations and fucks up every possible chance he gets. He doesn't like you guys, he doesn't enjoy streaming, the only reason he still streams is to get donations in order to pay for a roof over his sorry ass. He has no social life, all he does is stream all day and buy shitty materiel products with the money he earns from twitch. I can't believe he hasn't quit already. This is a complete and utter disgrace to speedrunning.",
            f"hey dude i'm fine, just wondering if life is worth it sometimes you know, with the darkness creeping in and everything feels pointless, but speedrunning does take the edge off when the darkest moments because when you gaze at the abyss, it gazes back at you. i think my grandma used to tell me that anyway but now she's dead so who knows",
            f"Hey Stiv, I hope you can see this message now that the chat has died down. I wanted to say congrats! I know you can do a little better but I always want to tip my hat off to you. Through thick and thin I will still be here to always support you. I know times are hard, but you always come back with a good attitude. I wish you the very best on your next runs, and hope you get an even better score. I will continue to be here and find new strats as always. Great job Stiv. I am rooting for you always! You should be proud.",
            f"An Agent race would be just as hype (and if not even more intense) than the Super Metroid race of AGDQ 2014",
            f"Unlike Rockman X 1-3, Spyro, and Sly Cooper, all of which have optimized World Records, this is clearly anything but, and you are basically begging someone to take that record from you. So, without further adieu, excuse me while I push you down the stairs, into the spiked, flaming pit at the end use this opportunity. Nothing personal, but I have a goal.",
            f"Ah, the antelope of death. It's because I cheated in Super Mario 64. This will need to be addressed soon.",
            f"I'm sorry, but that french guy was driving me insane. Impossible to understand such a heavy accent, his microphone towered over his face which wasn't even loud, and the things that I could hear made it sound like he didn't even know what he was talking about for most things, especially considering the other guys on the couch would cringe or tilt their heads like "+"'"'What? That"'"s not true?",
            f"Hey Claude why don't you play DKC2 anymore? I think it's pretty fkin rude how you're acting right now. Most people only follow for your DK64 and you're losing followers tonight acting like a child.",
            f"electra, there's something I've been meaning to talk to you about, and, it's kinda the elephant in the room here. I want you to take what I say to heart. I think you're getting too invested in, um, 4chan lingo, and I feel like you need to hear it coming from me, to like, really have it have any impact on you. Sorry if this is awkward, and sorry I'm bringing this up in front of a lot of people, but like, you need help man. There, I said it.",
            f"There are definitely some assholes in the community. So I just don't involve myself with them anymore. I mean, it is kinda of baseless, but... regardless if it's baseless or not, I can tell that people don't like me in the community, for like absolutely no reason, so... there's just idiots in the community. Alright, so that looks like something... oh dude, this... this is so cool, this'll be something once I get my Morph Ball. Yes, you are a friend dcr.",
            f"I'm here to kill Cha0s. That's my mission. Looks like Cha0s has been waiting for us. I only know one thing, I want to kill Cha0s. Need to. It's not a hope, or a dream. It's like a hunger, thirst. You sure Cha0s is here? This is the shrine of Cha0s. He's here, we just have to hunt him down. The darkness is so thick I can taste it. This is it, no doubt. Cha0s... We're here to kill Cha0s. I've become Cha0s!",
            f"So you're going by "+'"Louie 2"'+" now nerd? Haha whats up douche bag, it's Donald from Highschool. Remember me? Me and the guys used to give you a hard time in school. Sorry you were just an easy target lol. I can see not much has changed. Remember Daisy the duck you had a crush on? Yeah we're married now. I make over 200k a year and drive a kart badly. I guess some things never change huh loser? Nice catching up lol. Pathetic.."
            f"So today, for the first time, my little toddler finally counted to ten. Everyone was celebrating, saying how proud they are in my kid, and then Ben Shapiro kicks open the door."+' "Oh you think it'+"'"+'s impressive that they can count to ten? I can count to one million."'+" and then proceeded, in my living room for the next two weeks, to count to one million. He then said "+'"yep, another libtard destroyed" and then curbstomped my kid."',
            f'"'"Hello, my oshi is from NiSan_, but its embarrassing to send this SC there so I'll send it here. Yesterday I divorced my wife. I can almost forgive the cheating but the fact the 3 kids I raised for 20 years arent mine is unforgivable (1/2)",
            f"hey Claude, whats up! We met at AGDQ 2020. We chatted a bit and you said you would watch my fft runs haha. I wonder if you ever got around to it. I checked my youtube comments every week. i could DM you the youtube link if you lost it. i know you are speedrunning all the time and maybe busy so maybe you just forgot. also i made some cool emotes i think you can use in your channel. let me know man. take it easy. cheers!",
            f" Hey, uhh... None of you guys are funny. If you want to prevent cancer consider standing out in front of the shuttle that's running in front of the hotel on the hour. Thank you.",
            f"So you're going by "+'"Donkey" now nerd?'+" Haha whats up douche bag, it's Funky from Highschool. Remember me? Me and the guys used to give you a hard time in Kong College. Sorry you were just an easy target lol. I can see not much has changed. Remember Candy the kong you had a crush on? Yeah we're married now. I make over 200k bananas a year and drive a speedboat. I guess some things never change huh loser? Nice catching up lol. Pathetic..",
            f"Speedrunning an RPG. That's awesome. You guys should try it with the speed cranked up a bit. Then the science of the speedrun will be no different than a sidescroller. Someone should definitely speedrun games with speed up on. Whole other level.",
            f"Yeah, fuck off buddy we absolutely need more Claude streams. Fuckin every time this kid hits the go live button some kusos bopped kids fuckin dirt nasty man. Does fuckin LCC have this many kuso under his belt I dont think so I'm fuckin tellin ya Claude is pottin 100 kusos in '21 fuckin callin it right now.",
            f"electra, i didnt think id live to see the day when ayapic would be corrupted by claudes hentai game energy and be lewder than maripic",
            f" t ｈｅｎ ｉ ｓｅｅ ｋｏｒｏｎｅ， ｍｙ ｈａｎｄ ａｕｔｏｍａｔｉｃａｌｌｙ ｇｏ ｔｏ ｔｈｅ ｄｉｃｋ． ｉ ｓｔｒｏｋｅ ｔｈｅ ｄｉｃｋ ａｎｄ ｆｅｅｌ ｉ ｈａｖｅ ｓｅｘ ｗｉｔｈ ｔｈｅ ｋｏｒｏｎｅ． ａｌｌ ｂｅｃｏｍｉｎｇ ＳＥＸしましょう",
            f"Yes I am in love with Amelia Watson, now you may say to me "'"'"isn't she just a fictional character?"'"'" well that is were you wrong by virtue of being a vtuber she is a real person with a fictional overlay, I dont like Amelia watson the character I love Amelia Watsion the person. I love the way she laughs, how she gets angry, her love for her pets and her inventive stream ideas. I love that she always tries her best and has fun while doing it.",
            f"All of my previous and upcoming records in DKC are fraudulent. This is the unmistakable truth. I have chosen of my own free will to admit fraud and be permanently banned from the SRC, so I have no intention of further developing the story.",
            f"Okay sooooo I'm a HUGE fan of the game Melty Blood Type Lumina (I've never played it but the 30-second trailers make it look AMAZING!!) and I noticed that this game" '"Melty Blood Actress Again Current Code”'" got rollback on PC. I have a question. Can the devs count?? I know the "'"Lumina"'" is an unreleased game but shouldn't "'"UNICLR"'" get rollback firs? I want to get this "'"Current Code”'" game but I think the ,UNICLR, game should be the play rollback first. Thanks!"
    ] #copypastas | TODO: parse from file THIS IS URGENT
cs_names = [
        "White Knight From The Weeb Fright",
        "No Whore Shall Suffer Word Gore",
        "Fedora Over My Menorah",
        "BBC Ecstasy",
        "Bull With My Wife in the Wool",
        "Lucky Cucky",
        "Nice Guys Finish Last",
        "Take My WR, Take My Wife",
        "I'll Beat Puncay Someday",
        "Trihex Brings Home My Bacon",
        "Matriarchy Malarkey",
        "Feminist Specialist",
        "Immaculate Emasculate",  # we have opted to omit "Yessuh Massa Trihex"
        "White Guilt Built",
        "Anita es Bonita",
        "Quinn Will Win",
        "Gate Is Hate",
        "Her Name Is Caitlyn",
        "Hilary Shillary",
        "Redacted Holocaust 'Joke'", #"Six Million",  # we have also opted to omit "Hard On For Trayvon" as well as "Crown For Mike Brown"
        "Trigger Warning",
        "Mighty Number 9 Backer",  # we have ALSO opted to omit "Freddie Gray Shall Have His Day"
        "Gender Fluid Druid",
        "Bonafide White Genocide"
] # carl names | TODO: parse from file
eo_classes = \
    [
        #eo1
        'Alchemist https://static.wikia.nocookie.net/etrian/images/7/7b/EO1Alchemists.png',
        'Dark Hunter https://static.wikia.nocookie.net/etrian/images/2/21/EO1DarkHunter.png',
        'Landsknecht https://static.wikia.nocookie.net/etrian/images/7/75/EO1Landsknecht.png',
        'Survivalist https://static.wikia.nocookie.net/etrian/images/2/2d/EO1Survivalists.png',
        'Troubadour https://static.wikia.nocookie.net/etrian/images/d/d6/EO1Troubadour.png',
        'Medic https://static.wikia.nocookie.net/etrian/images/7/75/EO1Medics.png',
        'Ronin https://static.wikia.nocookie.net/etrian/images/a/a6/EO1Ronins.png',
        'Hexer https://static.wikia.nocookie.net/etrian/images/7/7d/EO1Hexers.png',
        'Protector https://static.wikia.nocookie.net/etrian/images/e/ef/EO1Protectors.png',
        #eo2
        'Gunner https://static.wikia.nocookie.net/etrian/images/5/56/EO2GunnersArt.png',
        'War Magus https://static.wikia.nocookie.net/etrian/images/d/db/War_magus.png',
        'Beast https://static.wikia.nocookie.net/etrian/images/1/17/Beast.png',
        #eo3
        'Princess https://static.wikia.nocookie.net/etrian/images/5/5d/Prince%28ss%29.png',
        'Gladiator https://static.wikia.nocookie.net/etrian/images/e/ee/Warriors.png',
        'Hoplite https://static.wikia.nocookie.net/etrian/images/6/60/Phalanxesb.png',
        'Buccaneer https://static.wikia.nocookie.net/etrian/images/0/04/Piratesh.png',
        'Ninja https://static.wikia.nocookie.net/etrian/images/7/75/Shinobis.png',
        'Monk https://static.wikia.nocookie.net/etrian/images/f/fb/Ztxpp.jpg',
        'Zodiac https://static.wikia.nocookie.net/etrian/images/7/7a/Zodiacs.png',
        'Wildling https://static.wikia.nocookie.net/etrian/images/7/74/Beastmasters.png',
        'Arbalist https://static.wikia.nocookie.net/etrian/images/3/36/Ballistas.png',
        'Farmer https://static.wikia.nocookie.net/etrian/images/e/e8/Farmers.png',
        'Shogun https://static.wikia.nocookie.net/etrian/images/9/96/Xooaiu.jpg',
        'Yggdroid https://static.wikia.nocookie.net/etrian/images/3/3b/Yggdroid.png',
        #eo4
        'Landsknecht (EO4) https://vignette1.wikia.nocookie.net/vsbattles/images/c/c3/Etrian_Landsknecht.png',
        'Nightseeker https://gamefaqs1.cbsistatic.com/faqs/15/76915-111.png',
        'Fortress https://savepoint.es/wp-content/uploads/2013/01/Etrian-Odyssey-IV-fortress.jpg',
        'Sniper https://2.bp.blogspot.com/-PL8elPUt1KA/Ut9qR466GxI/AAAAAAAAQgg/FR3g4O39vI0/s1600/Etrian-Odyssey-IV-18.jpg',
        'Medic (EO4) https://img1.ak.crunchyroll.com/i/spire3/867efdc4bac7777491caeb99c215a4af1332989836_full.jpg',
        'Runemaster https://cdn.eldojogamer.com/wp-content/uploads/2013/02/Etrian-Odyssey-IV-Runemaster.png',
        'Dancer https://oyster.ignimgs.com/wordpress/stg.ign.com/2012/12/dancer1.jpg',
        'Arcanist http://oyster.ignimgs.com/mediawiki/apis.ign.com/etrian-odyssey-iv-legends-of-the-titan/thumb/7/77/Arcanist-F1-610x667.jpg/228px-Arcanist-F1-610x667.jpg',
        'Bushi https://www.legendra.com/media/artworks/3ds/etrian_odyssey_iv___legends_of_the_titan/etrian_odyssey_iv___legends_of_the_titan_art_47.jpg',
        'Imperial https://www.akibagamers.it/wp-content/uploads/2018/04/etrian-odyssey-x-24.jpg',
        #eo5
        'Fencer https://static.wikia.nocookie.net/etrian/images/f/f1/Fencer_all.png',
        'Dragoon https://static.wikia.nocookie.net/etrian/images/a/a6/Dragoon_all.png',
        'Pugilist https://static.wikia.nocookie.net/etrian/images/e/e7/Cestus_all.png',
        'Harbinger https://static.wikia.nocookie.net/etrian/images/4/47/Reaper_All.png',
        'Warlock https://static.wikia.nocookie.net/etrian/images/a/a0/Warlock_all.png',
        'Necromancer https://static.wikia.nocookie.net/etrian/images/f/f8/Necro_All.png',
        'Rover https://static.wikia.nocookie.net/etrian/images/8/84/Hound_all.png',
        'Masurao https://static.wikia.nocookie.net/etrian/images/7/71/Masurao_All.png',
        'Shaman https://static.wikia.nocookie.net/etrian/images/4/4b/Shaman_all.png',
        'Botanist https://static.wikia.nocookie.net/etrian/images/5/54/Herbalist_All.png',
        #sqx
        'Hero https://static.wikia.nocookie.net/etrian/images/9/91/Hero-0.png',
        'Vampire https://static.wikia.nocookie.net/etrian/images/0/00/Vampire.jpg',
        #emd
        'Wanderer https://i0.wp.com/www.segalization.com/wp-content/uploads/2015/01/Etrian-MD_01-08-15.jpg',
        #sekaiju to fusigi no danjon 2
        'Kenkaku https://www.ducumon.com/wp-content/uploads/2019/07/etrianmysterydungeon2-compressed.jpg',
        #misc
        'Mediko!! https://static.wikia.nocookie.net/etrian/images/d/df/EO1ExplorersLog0.png',
    ]
melty_chars = \
    [
        "Aoko",
        "Tohno",
        "Hime",
        "Nanaya",
        "Kouma",
        "Miyako",
        "Ciel",
        "Sion (Eltnam)",
        "Riesbyfe",
        "Sion (Vampire)",
        "Warachia",
        "Roa",
        "Maids",
        "Akiha",
        "Arcueid",
        "Powered Ciel",
        "Warc",
        "V. Akiha",
        "Mech",
        "Seifuku",
        "Satsuki",
        "Len",
        "Ryougi",
        "White Len",
        "Nero",
        "Neco Chaos",
        "Koha-Mech",
        "Hisui",
        "Neco Arc",
        "Kohaku",
        "Neco-Mecho"
    ]
melee_chars = \
    [
        "Dr. Mario",
        "Mario",
        "Luigi",
        "Bowser",
        "Peach",
        "Yoshi",
        "Donkey Kong",
        "Captain Falcon",
        "Ganondorf",
        "Falco",
        "Fox",
        "Ness",
        "Ice Climbers",
        "Kirby",
        "Samus",
        "Zelda",
        "Sheik",
        "Link",
        "Young Link",
        "Pichu",
        "Pikachu",
        "Jigglypuff",
        "Mr. Game & Watch",
        "Marth",
        "Roy"
    ]
soku_chars = \
    [
        "Sanae",
        "Cirno",
        "Meiling",
        "Reimu",
        "Marisa",
        "Alice",
        "Patchy",
        "Utsuho",
        "Suwako",
        "Sakuya",
        "Remilia",
        "Youmu",
        "Yuyuko",
        "Yukari",
        "Reisen",
        "Suika",
        "Komachi",
        "Aya",
        "Iku",
        "Tenshi",
        "Giant Catfish",

    ]
melty_tags = \
    {
        "aoko":"aozaki_aoko ",
        "tohno":"tohno_shiki ",
        "hime":"archetype_earth",
        "nanaya":"nanaya_shiki",
        "kouma":"kishima_kouma",
        "miyako":"arima_miyako",
        "ciel":"ciel_(tsukihime)",
        "sion": "sion_eltnam_atlasia",
        "ries":"riesbyfe_stridberg",
        "wara":"wallachia",
        "roa":"michael_roa_valdamjong",
        "akiha":"tohno_akiha",
        "arc":"arcueid_brunestud",
        "warc":"warcueid",
        "mech":"mecha_hisui",
        "satsuki":"yumizuka_satsuki",
        "len":"len_(tsukihime) ",
        "ryougi":"ryougi_shiki",
        "wlen":"white_len_(tsukihime)",
        "nero":"nrvnqsr_chaos",
        "nac":"nekoarc_chaos",
        "hisui":"hisui_(tsukihime)",
        "neco":"nekoarc",
        "kohaku":"kohaku_(tsukihime)"
    }
backup_links = \
    [
        f'https://konachan.com/image/d647a7d3ed0197be796ea4894417b4e3/Konachan.com%20-%20273192%20autumn%20black_hair%20blush%20boat%20dress%20hat%20kneehighs%20landscape%20leaves%20red_eyes%20reflection%20scenic%20shameimaru_aya%20short_hair%20touhou%20water%20waterfall%20wings.jpg',
        f'https://danbooru.donmai.us/data/original/fa/bb/fabb65e4dbf6a6af37680fdb7cecfad9.jpg',
        f'https://konachan.com/image/0c9c4bdc5f8e5d671bda3bc58c3631f2/Konachan.com%20-%20201535%202girls%20clouds%20fan%20hat%20inubashiri_momiji%20izumi4195202%20japanese_clothes%20katana%20miko%20shameimaru_aya%20sky%20socks%20sword%20thighhighs%20touhou%20weapon%20wolfgirl.jpg',
        f'https://konachan.com/image/74372dc58d1e627ff66ff1e91e69cc40/Konachan.com%20-%20234089%20black_hair%20building%20dress%20kneehighs%20mifuru%20petals%20pointed_ears%20shameimaru_aya%20short_hair%20touhou.jpg',
        f'https://konachan.com/image/bfc2fc102119e19131bc864e88535a74/Konachan.com%20-%20208397%20chen%20cirno%20dahuang%20doll%20fairy%20food%20foxgirl%20group%20hat%20hourai%20maid%20mask%20miko%20myon%20nazrin%20rope%20rumia%20seiran%20skirt%20su-san%20touhou%20vampire%20wings%20wolfgirl.jpg',
        f'https://konachan.com/image/0c00a308521e5f61d09a99ede9d56397/Konachan.com%20-%20263550%20barefoot%20brown_hair%20fallen_heaven%20flowers%20grass%20hat%20red_eyes%20ribbons%20shameimaru_aya%20short_hair%20skirt%20touhou.jpg',
        f'https://konachan.com/image/0c00a308521e5f61d09a99ede9d56397/Konachan.com%20-%20263550%20barefoot%20brown_hair%20fallen_heaven%20flowers%20grass%20hat%20red_eyes%20ribbons%20shameimaru_aya%20short_hair%20skirt%20touhou.jpg',
        f'https://danbooru.donmai.us/data/original/3e/35/3e35157038858361547d135cf3c27b1a.png',
        f'https://danbooru.donmai.us/data/original/0b/b8/0bb848217217d6e60c7c1a07caaf6df3.jpg',
        f'https://konachan.com/image/6316f2b34e68e3d8aeb184e9605c0dde/Konachan.com%20-%20231622%20bow%20braids%20brown_eyes%20brown_hair%20dress%20drink%20food%20forest%20group%20hat%20horns%20long_hair%20miko%20night%20pink_hair%20skirt%20tie%20touhou%20tree%20twintails%20wings.png',
        f'https://konachan.com/image/9f71b66be8e29b70d963d3865cc6dbb5/Konachan.com%20-%20256833%20aliasing%20autumn%20black_hair%20cibo_%28killy%29%20gloves%20kneehighs%20leaves%20orange_eyes%20pointed_ears%20ribbons%20short_hair%20skirt%20touhou%20tree%20watermark%20wings.png',
        f'https://konachan.com/image/e1c3464a7e2aa1cf6204187d9fa7d891/Konachan.com%20-%20190421%20hat%20nyuu_%28manekin-eko%29%20orange%20shameimaru_aya%20short_hair%20skirt%20touhou%20translation_request%20wings.jpg',
        f'https://konachan.com/image/b465107c9ef33c03bb7218f740661d08/Konachan.com%20-%20185777%20black_hair%20fan%20feathers%20hat%20niwashi_%28yuyu%29%20panties%20red_eyes%20shameimaru_aya%20short_hair%20skirt%20sky%20thighhighs%20tie%20touhou%20underwear%20upskirt%20wings.jpg',
        f'https://konachan.net/jpeg/a1e5fc4511d0588ec49bf0ac0d8878c6/Konachan.com%20-%20241020%20animal_ears%20black_hair%20boots%20gloves%20inubashiri_momiji%20pointed_ears%20red_eyes%20shameimaru_aya%20short_hair%20skirt%20thighhighs%20tie%20touhou%20wings.jpg',
        f'https://konachan.net/jpeg/34755cc3490940b4c94c60e4f9199b16/Konachan.com%20-%20325247%20black_hair%20bow%20clouds%20fan%20feathers%20hat%20leaves%20orange_eyes%20shameimaru_aya%20shirt%20skirt%20sky%20thighhighs%20touhou%20wings%20yaye.jpg',
        f'https://konachan.net/image/591f4f2495adff6d98be1d3f9116c1ec/Konachan.com%20-%20319540%20animal%20autumn%20bird%20black_hair%20brown_eyes%20camera%20hat%20kneehighs%20leaves%20rin_falcon%20scarf%20shameimaru_aya%20skirt%20touhou%20tree%20wings.jpg',
        f'https://konachan.net/jpeg/76f1373139c640ce017dcee0827140e4/Konachan.com%20-%20299964%20animal%20bird%20brown_hair%20fan%20feathers%20hat%20nahaki%20red_eyes%20shameimaru_aya%20short_hair%20thighhighs%20touhou%20wings.jpg',
        f'https://konachan.net/image/6937b6147863573350b8fed6c8a2fc82/Konachan.com%20-%20295576%20animal%20black_hair%20blush%20bow%20drink%20fish%20food%20hat%20ken_%28coffee_michikusa%29%20sake%20shameimaru_aya%20short_hair%20skirt%20touhou%20water%20wings.jpg',
        f'https://konachan.net/jpeg/4dbd7ae35b56b4890afd0e57e7b214c2/Konachan.com%20-%20294029%20brown_eyes%20brown_hair%20clouds%20gray_hair%20long_hair%20phone%20red_eyes%20ribbons%20short_hair%20skirt%20sky%20tail%20tie%20touhou%20tree%20twintails%20waifu2x%20wolfgirl.jpg',
        f'https://konachan.net/jpeg/6f0c26fd69c392dc2a464b4771945408/Konachan.com%20-%20293985%20animal_ears%20brown_hair%20clouds%20gray_hair%20red_eyes%20shameimaru_aya%20short_hair%20siyajiyatouhou%20sky%20touhou%20tree%20water%20waterfall%20wings%20wolfgirl.jpg',
        f'https://konachan.net/jpeg/a46948c2beeef8449b573b7ce4fbfe1a/Konachan.com%20-%20290897%20animal%20apron%20autumn%20boots%20bow%20camera%20fang%20fire%20group%20hat%20leaves%20miko%20skirt%20sword%20syuri22%20touhou%20tree%20water%20weapon%20wink%20witch%20witch_hat%20wolfgirl.jpg',
        f'https://konachan.net/jpeg/848059ba8ecd9522b97fb9ad76265e56/Konachan.com%20-%20288650%20animal_ears%20autumn%20brown_hair%20camera%20long_hair%20paper%20red_eyes%20shade%20short_hair%20skirt%20stairs%20thkani%20tie%20touhou%20tree%20twintails%20white_hair%20wolfgirl.jpg',
        f'https://konachan.net/image/0a00365308c6118bcde032e3a02a5fa2/Konachan.com%20-%20263156%20black_hair%20brown_eyes%20cherry_blossoms%20cibo_%28killy%29%20clouds%20flowers%20katana%20long_hair%20petals%20shameimaru_aya%20skirt%20sky%20sword%20touhou%20weapon%20wings.jpg',
        f'https://konachan.net/jpeg/0788f5fda279463618a5d5ab3bbfaeee/Konachan.com%20-%20241031%20camera%20group%20hakurei_reimu%20kirisame_marisa%20leaves%20leon_7%20miko%20remilia_scarlet%20shameimaru_aya%20touhou%20vampire%20wings%20witch%20yakumo_yukari.jpg',
        f'https://konachan.net/image/9d0e955b121920a04133030f5b321215/Konachan.com%20-%20235613%20animal_ears%20black_hair%20blush%20brown_eyes%20drink%20fang%20food%20gray_hair%20green_eyes%20green_hair%20kimono%20morino_hon%20short_hair%20tokiko%20torii%20touhou%20wings.jpg',
        f'https://konachan.net/image/a0e40c5ff467b229b690bf348ecbd007/Konachan.com%20-%20192820%20blush%20camera%20clouds%20glasses%20hat%20pyonsuke0141%20scarf%20shameimaru_aya%20signed%20skirt%20sky%20thighhighs%20touhou%20wings%20zettai_ryouiki.jpg',
        f'https://konachan.net/image/47bea2c77896ce6c373097dc2c5741de/Konachan.com%20-%20135275%20excel_%28shena%29%20inubashiri_momiji%20red_eyes%20shameimaru_aya%20sky%20tail%20touhou%20water%20wings%20wolfgirl.jpg',
        f'https://pbs.twimg.com/media/E4rX8I2WQAQz1JP?format=jpg&name=large'
    ]
prev_url = ['dummy text']
takuya_quotes = \
    [
        "(I pray that this teacher remains employed...)",
        "Really? Violence is bad, man.",
        "It's all coming to me. There's no way that I could delete records of such a beautiful girl from my mental database.",
        "*sniff*... *sniff* *sniff*... ",
        "*gulp* *gulp* *gulp*... Fhwaa! This cup of water is what I've been living for!",
        "I'm going to eat you!",
        "(She must have farted or something)",
        "(Wow... now that's what I'd call a foxy mama.)",
        "I don't feel like studying at my desk. Oh well, let's just have some doggy style sex on top of it then.",
        "(Everyone has the right to live, no matter how r*tarded they may be.)",
        "(Oh God, I want to be that wrinkle.)",
        "(This never fails to make me happy.)",
        "(I want to be the wind.)",
        "(I want to be those documents.)",
        "........ What a sight.",
        "I-I wasn't trying to grab your boobs or anything!",
        "(Oh God, I want to be that desk.)",
        "Woods? Woods as in how much wood would a woodchuck chuck if a woodchuck could chuck wood?",
        "(Oh God, I have such a small vocabulary.)",
        "Hedonism is one of my trademarks.",
        "No way... it was educational in all sorts of ways.",
        "She suddenly burst into the room. We had no chance to hide.",
        "Y-Yeah, it's gotten pretty hot in here, huh!",
        "There's three people... then it must be a gangb... uh, never mind.",
        "(Oh God... I want to be that towel.)",
        "O Juliet, thine eyes strike me with the force of a million volts! ...How 'bout that?",
        "I want to be scolded.",
        "Former statements exit to be retracted.",
        "Aaagh! Please don't dig up old shit like that!"
    ]
demons_nocturne = \
    {
        #foul
        "Will O' Wisp":'https://static.wikia.nocookie.net/megamitensei/images/3/34/Will_o%27_wisp.png/revision/latest/scale-to-width-down/1000?cb=20120421225839',
        'Slime': 'https://static.wikia.nocookie.net/megamitensei/images/1/19/Slime_SMT1.png/revision/latest/scale-to-width-down/350?cb=20210123165750',
        'Mou-Ryo': 'https://static.wikia.nocookie.net/megamitensei/images/f/fc/Mou-Ryo_SMTIV.png/revision/latest/scale-to-width-down/350?cb=20170304180522',
        'Blob': 'https://static.wikia.nocookie.net/megamitensei/images/c/ca/Blobartwork.jpg/revision/latest/scale-to-width-down/350?cb=20190330032552',
        'Black Ooze': 'https://static.wikia.nocookie.net/megamitensei/images/6/68/184_Black_Ooze.jpg/revision/latest/scale-to-width-down/350?cb=20100514013933',
        'Phantom': 'https://static.wikia.nocookie.net/megamitensei/images/b/b8/174_Phantom.jpg/revision/latest/scale-to-width-down/292?cb=20100514013418',
        'Sakahagi': 'https://static.wikia.nocookie.net/megamitensei/images/3/3f/SMT3Sakahagi.png/revision/latest/scale-to-width-down/228?cb=20201118161744',
        'Shadow': 'https://static.wikia.nocookie.net/megamitensei/images/6/6c/Shadow2.jpg/revision/latest/scale-to-width-down/348?cb=20190330035201',
        #haunt
        'Preta': 'https://static.wikia.nocookie.net/megamitensei/images/3/37/Preta2.jpg/revision/latest/scale-to-width-down/350?cb=20090516184216',
        'Choronzon': 'https://static.wikia.nocookie.net/megamitensei/images/5/52/Choronzon.png/revision/latest/scale-to-width-down/350?cb=20120420045333',
        'Yaka': 'https://static.wikia.nocookie.net/megamitensei/images/3/3b/KWYakka.jpg/revision/latest/scale-to-width-down/350?cb=20110904051009',
        'Chatterskull': 'https://static.wikia.nocookie.net/megamitensei/images/c/c4/Spn_chr_mob_chatterskull.png/revision/latest/scale-to-width-down/1000?cb=20210610094802',
        'Pisaca': 'https://static.wikia.nocookie.net/megamitensei/images/7/71/Pisaca2.jpg/revision/latest/scale-to-width-down/287?cb=20101122173626',
        'Legion': 'https://static.wikia.nocookie.net/megamitensei/images/d/de/LegionSMT.jpg/revision/latest/scale-to-width-down/350?cb=20080709034919',
        'Rakshasa': 'https://static.wikia.nocookie.net/megamitensei/images/b/b3/Gurr.JPG/revision/latest/scale-to-width-down/350?cb=20190328190438',
        #raptor
        'Gurr': 'https://static.wikia.nocookie.net/megamitensei/images/b/b3/Gurr.JPG/revision/latest/scale-to-width-down/350?cb=20190328190438',
        #tyrant
        'Loki': 'https://static.wikia.nocookie.net/megamitensei/images/8/8c/LokiKW.jpg/revision/latest/scale-to-width-down/350?cb=20080612232628',
        'Abaddon': 'https://static.wikia.nocookie.net/megamitensei/images/a/a1/Abaddon2.jpg/revision/latest/scale-to-width-down/800?cb=20080708170232',
        'Surt': 'https://static.wikia.nocookie.net/megamitensei/images/d/df/Surt.JPG/revision/latest/scale-to-width-down/317?cb=20190328185801',
        'Aciel': 'https://static.wikia.nocookie.net/megamitensei/images/c/cc/Aciel.jpg/revision/latest/scale-to-width-down/291?cb=20190501013550',
        'Beelzebub (human)': 'https://static.wikia.nocookie.net/megamitensei/images/0/03/Baal_Zabul.JPG/revision/latest/scale-to-width-down/350?cb=20190328184406',
        'Mot': 'https://static.wikia.nocookie.net/megamitensei/images/e/eb/Mot.jpg/revision/latest/scale-to-width-down/309?cb=20190328171656',
        'Beelzebub (fly)': 'https://static.wikia.nocookie.net/megamitensei/images/7/7c/KazumaKaneko-Beelzebub.jpg/revision/latest/scale-to-width-down/350?cb=20090219082929',
        #vile
        'Arahabaki': 'https://static.wikia.nocookie.net/megamitensei/images/f/fb/ArahabakiKC.jpg/revision/latest/scale-to-width-down/301?cb=20080705222447',
        'Baphomet': 'https://static.wikia.nocookie.net/megamitensei/images/3/33/Baphomet.jpg/revision/latest/scale-to-width-down/350?cb=20080802231114',
        'Pazuzu': 'https://static.wikia.nocookie.net/megamitensei/images/e/ea/PazuzuSMT2.jpg/revision/latest/scale-to-width-down/337?cb=20080806165033',
        'Girimehkala': 'https://static.wikia.nocookie.net/megamitensei/images/4/4a/KazumaKaneko-Girimehkala.jpg/revision/latest/scale-to-width-down/335?cb=20090404041239',
        'Tao Tie': 'https://static.wikia.nocookie.net/megamitensei/images/f/f5/Tao_Tie_%282%29.jpg/revision/latest/scale-to-width-down/350?cb=20190330150732',
        'Samael': 'https://static.wikia.nocookie.net/megamitensei/images/5/59/Samael.jpg/revision/latest/scale-to-width-down/348?cb=20110611102937',
        'Mada': 'https://static.wikia.nocookie.net/megamitensei/images/3/38/Mada2.jpg/revision/latest/scale-to-width-down/322?cb=20151130235912',
        #wilder
        'Zhen': 'https://static.wikia.nocookie.net/megamitensei/images/4/43/Zhen.png/revision/latest/scale-to-width-down/1000?cb=20190401160319',
        'Bicorn': 'https://static.wikia.nocookie.net/megamitensei/images/4/48/KWBicorn.jpg/revision/latest/scale-to-width-down/350?cb=20110904050857',
        'Raiju': 'https://static.wikia.nocookie.net/megamitensei/images/5/5a/514_-_Raiju.jpg/revision/latest/scale-to-width-down/340?cb=20120514051105',
        'Nue': 'https://static.wikia.nocookie.net/megamitensei/images/b/be/Nue.jpg/revision/latest/scale-to-width-down/350?cb=20080617063258',
        'Mothman': 'https://static.wikia.nocookie.net/megamitensei/images/e/e0/Mothmanof.png/revision/latest/scale-to-width-down/350?cb=20190328182520',
        'Hrezvelgr': 'https://static.wikia.nocookie.net/megamitensei/images/2/29/Hresvelgr.JPG/revision/latest/scale-to-width-down/350?cb=20190328203244',
        #avatar
        'Makami': 'https://static.wikia.nocookie.net/megamitensei/images/7/71/Makami_-_Nocturne.jpg/revision/latest/scale-to-width-down/350?cb=20080920172200',
        'Cai-Zhi': 'https://static.wikia.nocookie.net/megamitensei/images/c/c1/KaichiDS.jpg/revision/latest/scale-to-width-down/350?cb=20190328190351',
        'Yatagarasu': 'https://static.wikia.nocookie.net/megamitensei/images/5/57/Yatagarasu3.JPG/revision/latest/scale-to-width-down/350?cb=20190330162439',
        'Barong': 'https://static.wikia.nocookie.net/megamitensei/images/1/14/Barong3.JPG/revision/latest/scale-to-width-down/350?cb=20190328174958',
        #avian
        'Garuda': 'https://static.wikia.nocookie.net/megamitensei/images/8/82/Garuda_%282%29.jpg/revision/latest/scale-to-width-down/325?cb=20190328225002',
        #deity
        'Horus': 'https://static.wikia.nocookie.net/megamitensei/images/2/2b/KazumaKaneko-Horus.jpg/revision/latest/scale-to-width-down/350?cb=20090315020228',
        'Atavaka': 'https://static.wikia.nocookie.net/megamitensei/images/2/2d/SMTIIAtavaka.png/revision/latest/scale-to-width-down/350?cb=20090513035957',
        'Amaterasu': 'https://static.wikia.nocookie.net/megamitensei/images/4/4f/Amaterasu_%28Devil_Summoner_Art%29.png/revision/latest/scale-to-width-down/350?cb=20210821003120',
        'Odin': 'https://static.wikia.nocookie.net/megamitensei/images/7/75/OdinKW.jpg/revision/latest/scale-to-width-down/322?cb=20080612231621',
        'Mithra': 'https://static.wikia.nocookie.net/megamitensei/images/a/a4/MithraSMT3.jpg/revision/latest/scale-to-width-down/262?cb=20151130235513',
        'Vishnu': 'https://static.wikia.nocookie.net/megamitensei/images/e/e8/Vishnu_%28Soul_Hackers_Art%29.png/revision/latest/scale-to-width-down/350?cb=20210703011829',
        #dragon
        'Gui Xian': 'https://static.wikia.nocookie.net/megamitensei/images/c/c8/Genbu232.JPG/revision/latest/scale-to-width-down/309?cb=20190328230315',
        'Long': 'https://static.wikia.nocookie.net/megamitensei/images/d/dc/Seiryu.JPG/revision/latest/scale-to-width-down/350?cb=20190328230357',
        #element
        'Erthys': 'https://static.wikia.nocookie.net/megamitensei/images/7/7b/EarthiesSMT2.jpg/revision/latest/scale-to-width-down/350?cb=20080806041550',
        'Aeros': 'https://static.wikia.nocookie.net/megamitensei/images/4/44/Aeros2.jpg/revision/latest/scale-to-width-down/350?cb=20080806033020',
        'Aquans': 'https://static.wikia.nocookie.net/megamitensei/images/6/64/Aquans2.jpg/revision/latest/scale-to-width-down/264?cb=20080806032351',
        'Flaemis': 'https://static.wikia.nocookie.net/megamitensei/images/2/2f/FlamiesSMT.jpg/revision/latest/scale-to-width-down/319?cb=20080802001254',
        #mitama
        'Ara Mitama': 'https://static.wikia.nocookie.net/megamitensei/images/f/f7/Ara_Mitama_%28Devil_Summoner_Art%29.png/revision/latest/scale-to-width-down/345?cb=20210821003118',
        'Nigi Mitama': 'https://static.wikia.nocookie.net/megamitensei/images/0/0e/NigiMitamaP4.png/revision/latest/scale-to-width-down/350?cb=20190402144926',
        'Kusi Mitama': 'https://static.wikia.nocookie.net/megamitensei/images/6/68/KusiMitamaP4.png/revision/latest/scale-to-width-down/350?cb=20190402144809',
        'Saki Mitama': 'https://static.wikia.nocookie.net/megamitensei/images/d/dd/SakiMitamaP4.png/revision/latest/scale-to-width-down/350?cb=20190402144703',
        #entity
        'Albion': 'https://static.wikia.nocookie.net/megamitensei/images/c/c1/AlbionandCo.jpg/revision/latest/scale-to-width-down/350?cb=20090405043841',
        #fury
        'Dionysus': 'https://static.wikia.nocookie.net/megamitensei/images/a/a2/Dionysius.jpg/revision/latest/scale-to-width-down/279?cb=20190328152501',
        'Wu Kong': 'https://static.wikia.nocookie.net/megamitensei/images/3/3d/SeitenteiseiSMT.jpg/revision/latest/scale-to-width-down/350?cb=20080706003024',
        'Beiji-Weng': 'https://static.wikia.nocookie.net/megamitensei/images/3/3a/Hokutoseikun-1-.jpg/revision/latest/scale-to-width-down/350?cb=20130825110711',
        'Shiva': 'https://static.wikia.nocookie.net/megamitensei/images/4/45/Shiva2.JPG/revision/latest/scale-to-width-down/350?cb=20151130225129',
        #genma
        'Kurama': 'https://static.wikia.nocookie.net/megamitensei/images/2/20/Kurama2.jpg/revision/latest/scale-to-width-down/350?cb=20080708185322',
        'Hanuman': 'https://static.wikia.nocookie.net/megamitensei/images/f/fd/HanumanSMT.jpg/revision/latest/scale-to-width-down/255?cb=20080802034006',
        'Cu Chulainn': 'https://static.wikia.nocookie.net/megamitensei/images/1/1c/CuChulainn2.jpg/revision/latest/scale-to-width-down/350?cb=20080708183926',
        #holy
        'Shiisaa': 'https://static.wikia.nocookie.net/megamitensei/images/a/a1/ShiisaaDS.jpg/revision/latest/scale-to-width-down/350?cb=20190331161840',
        'Unicorn': 'https://static.wikia.nocookie.net/megamitensei/images/5/53/UnicornSMT.jpg/revision/latest/scale-to-width-down/350?cb=20080801225707',
        'Senri': 'https://static.wikia.nocookie.net/megamitensei/images/6/63/Senri_-_Nocturne.jpg/revision/latest/scale-to-width-down/350?cb=20080920172616',
        'Feng Huang': 'https://static.wikia.nocookie.net/megamitensei/images/a/af/Suzaku.jpg/revision/latest/scale-to-width-down/350?cb=20190328230049',
        'Baihu': 'https://static.wikia.nocookie.net/megamitensei/images/4/40/ByakkoSMT2.jpg/revision/latest/scale-to-width-down/350?cb=20080808014542',
        'Chimera': 'https://static.wikia.nocookie.net/megamitensei/images/9/9b/Chimera2.JPG/revision/latest/scale-to-width-down/350?cb=20190328211529',
        #kishin
        'Minakata': 'https://static.wikia.nocookie.net/megamitensei/images/0/06/Minakata.jpg/revision/latest/scale-to-width-down/316?cb=20080728203159',
        'Zouchouten': 'https://static.wikia.nocookie.net/megamitensei/images/8/87/Zouchou.png/revision/latest/scale-to-width-down/346?cb=20080728210910',
        'Koumokuten': 'https://static.wikia.nocookie.net/megamitensei/images/9/95/18_-_Komokuten.jpg/revision/latest/scale-to-width-down/350?cb=20120325011542',
        'Okuninushi': 'https://static.wikia.nocookie.net/megamitensei/images/0/05/Okuninushi2.jpg/revision/latest/scale-to-width-down/205?cb=20190501013035',
        'Mikazuchi': 'https://static.wikia.nocookie.net/megamitensei/images/1/1c/TakemikazuchiSMT.jpg/revision/latest/scale-to-width-down/309?cb=20080706004955',
        'Jikokuten': 'https://static.wikia.nocookie.net/megamitensei/images/c/c0/P3Jikokuten.jpg/revision/latest/scale-to-width-down/313?cb=20090903054909',
        'Futomimi': 'https://static.wikia.nocookie.net/megamitensei/images/1/16/SMT3Futomimi.png/revision/latest/scale-to-width-down/191?cb=20201118132550',
        'Bishamonten': 'https://static.wikia.nocookie.net/megamitensei/images/2/23/Bishamonten.png/revision/latest/scale-to-width-down/350?cb=20090516182036',
        'Thor': 'https://static.wikia.nocookie.net/megamitensei/images/2/23/Thor.jpg/revision/latest/scale-to-width-down/350?cb=20080613190606',
        #lady
        'Kikuri-Hime': '',
        'Kushinada': '',
        'Parvati': '',
        'Kali': '',
        'Skadi': '',
        #megami
        'Uzume': '',
        'Sarasvati': '',
        'Sati': '',
        'Lakshmi': '',
        'Scathach': '',
        #seraph
        'Uriel': '',
        'Raphael': '',
        'Gabriel': '',
        'Michael': '',
        'Metatron': '',
        #wargod
        'Valkyrie': '',
        'Ganesha': '',
        #beast
        'Inugami': '',
        'Nekomata': '',
        'Babd Catha': '',
        'Orthrus': '',
        'Sparna': '',
        'Cerberus': '',
        #brute
        'Shikigami': '',
        'Momunofu': '',
        'Oni': '',
        'Shiki-Ouji': '',
        'Kin-Ki': '',
        'Sui-Ki': '',
        'Fuu-Ki': '',
        'Ongyo-Ki': '',
        #divine
        'Angel': '',
        'Archangel': '',
        'Principality': '',
        'Power': '',
        'Virtue': '',
        'Dominion': '',
        'Throne': '',
        #fairy
        'Pixie': '',
        'Jack Frost': '',
        'High Pixie': '',
        'Pyro Jack': '',
        'Kelpie': '',
        'Troll': '',
        'Setanta': '',
        'Oberon': '',
        'Titania': '',
        #fallen
        'Forneus': '',
        'Eligor': '',
        'Berith': '',
        'Ose': '',
        'Decarabia': '',
        'Flauros': '',
        #femme
        'Datsue-Ba': '',
        'Taraka': '',
        'Shikiome': '',
        'Yaksini': '',
        'Dakini': '',
        'Clotho': '',
        'Lachesis': '',
        'Atropos': '',
        'Rangda': '',
        #jirae
        'Kodama': '',
        'Hua Po': '',
        'Sudama': '',
        'Sarutahiko': '',
        'Titan': '',
        'Gogmagog': '',
        #night
        'Lilim': '',
        'Fomor': '',
        'Incubus': '',
        'Succubus': '',
        'Kaiwan': '',
        'Loa': '',
        'Queen Mab': '',
        'Black Frost': '',
        'Nyx': '',
        'Lilith': '',
        #snake
        'Nozuchi': '',
        'Naga': '',
        'Mizuchi': '',
        'Raja Naga': '',
        'Quetzalcoatl': '',
        'Yurlungur': '',
        #yoma
        'Apsaras': '',
        'Isora': '',
        'Koppa': '',
        'Dis': '',
        'Karasu': '',
        'Onkot': '',
        'Jinn': '',
        'Purski': '',
        'Efreet': '',
        #fiend
        'Matador': '',
        'Daisoujou': '',
        'Hell Biker': '',
        'White Rider': '',
        'Red Rider': '',
        'Black Rider': '',
        'Pale Rider': '',
        'The Harlot': '',
        'Trumpeter': '',
        'Dante From The Devil May Cry Series': '',
    }
superuser = \
    [
        f'electra_rta'
    ]
plebfilter = \
    [
        'mpghappiness',
        'symm_',
        'NASAMarathon',
        'v0oid'
    ]
silenced = \
    [
        "TIUYMI"
    ]
pasta_dict = {} # Empty dictionary used for pasta cooldown
'''
                                           CLASS DEF
'''

class BlueAyaChan(commands.Bot):
    def __init__(self):
        # allocate channels list with IRC channels from plaintext
        channels = []
        print('allocating channels to bot')
        with open('channels.txt', 'r') as fin:
            for l in fin:
                channels.append(l)
        for i in channels:
            print("connected to #" + str(i).strip('\n'))
        #auth token allocation
        tokens = []
        with open("hooks", 'r') as fin:
            for l in fin:
                tokens.append(l)
        # call superconstructor
        super().__init__(irc_token=tokens[0], client_id=tokens[1], nick='BlueAyaChan', prefix='!', initial_channels=channels)

    #print deployment message
    async def event_ready(self):
        print(f'{self.nick} is ready to launch')
    #log chats
    async def event_message(self, message):
        curtime = datetime.now()
        print(f'[' + str(curtime.strftime("%H:%M:%S")) + '] #' + str(message.channel) + " <" + message.author.name +">: " + message.content)
        #if(message.author.name not in silenced):
        await self.handle_commands(message)
        #else:
        #    return

    ''' new_msg = ''
            i = 0
            while(i < len(raw_msg)):
                new_msg += raw_msg[i]
                if(i % 80 == 0):
                    new_msg += '\n'
        '''
    '''################- C O M M A N D S -################'''
    '''
    @commands.command(name='test')
    async def my_command(self, ctx):
        await ctx.send(f'Hello {ctx.author.name}!')
    '''

    '''
    Command: !cfb - parses cfb.txt into lists used to create a name to send to the chat.
    '''
    @commands.command(name='cfb')
    async def cfb_string_gen(self, ctx):
        # populate lists for !cfb
        c_list = []
        f_list = []
        b_list = []
        #TODO: add '-v' for verbose cfb
        cfb_txt = open('20k.txt', 'r')
        cfb_str = cfb_txt.readlines()
        cfb_txt.close()
        for i in cfb_str:
            if (i[0] == 'c'):
                c_list.append(i)
            if (i[0] == 'f'):
                f_list.append(i)
            if (i[0] == 'b'):
                b_list.append(i)
        #print(str(len(c_list)) + ' ' + str(len(f_list)) + ' ' + str(len(b_list)))
        await ctx.send(f'' + c_list[random.randint(0,len(c_list))] + ' ' + f_list[random.randint(0,len(f_list))] + ' ' + b_list[random.randint(0,len(b_list))])

    '''
    Command: !grim 
    TODO: fix this shit
    '''
    #@commands.command(name='grim_do_not_run')
    async def grim(self, ctx):
        grim_txt = open('grim2.txt', 'r')
        grim_str = grim_txt.readlines()
        grim_txt.close()
        #print(grim_str[0:13])
        await ctx.send(f'      ' + str(grim_str[0:5]))
        #await ctx.send(f'' + str(grim_str[13:-1]))

    '''
    Command: !lunch - dumb meme
    '''
    @commands.command(name='lunch')
    async def lunch(self, ctx):
        await ctx.send(f'{ctx.author.name} is logging this chatroom! TheForkies')

    '''
    Command: !carl - generates a random Carl Sagan name
    '''
    @commands.command(name='carl')
    async def carl(self, ctx):
        global cs_names
        await ctx.send(f'Carl "' + cs_names[random.randint(0, len(cs_names)-1)] + '" Sagan')


    '''
    Command: !pasta - posts a random copypasta
    '''
    async def pasta(self, ctx):
        '''def dt_to_float(dt):
            timestamp = time.mktime(dt.timetuple()) + dt.microsecond / 1e6
            return float(timestamp)'''
        global pasta_dict
        global pasta_str
        time_now = datetime.now()
        if(str(ctx.channel) not in pasta_dict.keys()):
            try:
                await ctx.send(f'' + str(pasta_str[random.randint(0,len(pasta_str) - 1)]))
            except:
                commands.CommandError
                await ctx.send(f'' + str(pasta_str[random.randint(0, len(pasta_str) - 1)]))
            pasta_dict[str(ctx.channel)] = datetime.now()
        elif(str(ctx.channel) in pasta_dict.keys()):
            print(time_now.time())
            #minutes_diff = (float(time_now.timestamp()) - float(pasta_dict[str(ctx.channel)].timestamp())) / 60.0
            #print(minutes_diff)
            diff = (time_now.minute*60 + time_now.second) - (pasta_dict[str(ctx.channel)].minute*60 + pasta_dict[str(ctx.channel)].second)
            print(diff)
            if(diff >= 90 or diff <= -1):
                try:
                    await ctx.send(f'' + str(pasta_str[random.randint(0, len(pasta_str) - 1)]))
                except:
                    commands.CommandError
                    await ctx.send(f'' + str(pasta_str[random.randint(0, len(pasta_str) - 1)]))
                pasta_dict[str(ctx.channel)] = None
                pasta_dict[str(ctx.channel)] = datetime.now()
        else:
            try:
                await ctx.send(f'' + str(pasta_str[random.randint(0, len(pasta_str) - 1)]))
            except:
                commands.CommandError
                await ctx.send(f'' + str(pasta_str[random.randint(0, len(pasta_str) - 1)]))
            return

        #await asyncio.wait_for(timeout=60, fut=60)
        #self.remove_check(pasta())

    @commands.command(name='pasta')
    async def runpasta(self, ctx):
        await asyncio.gather(self.pasta(ctx))
        #task = self.remove_check(pasta(ctx))

    '''
    # async with async_timeout.timeout(60):
    async def x(self,ctx):
        with async_timeout.timeout(60):
           await pasta(ctx)
'''
    #await async_timeout(60) #non clocking sleep for 1 minute

    '''
    Command: !pointsbetting
    '''
    #@commands.command(name='alert')
    async def alert(self, ctx):
        memetext = ['BOGGED GrimChamp REMEMBER TO VOTE NO SINCE THE STREAMER PLANS TO THROW THIS PREDICTION!!! GrimChamp BOGGED', 'REMEMBER TO VOTE YES SINCE THE STREAMER HOT ON HIS GAMING TONIGHT!!! WR BABY LETS HECKIN GO!!! TheLegendaryRonald TheDaily']
        await ctx.send(f'ALERT ALERT!!!! THE PREDICTION TIMER HAS STARTED!!! GET THOSE PREDICTIONS IN!!! ' + str(memetext[random.randint(0,len(memetext))]))
    '''
    
    '''
    @commands.command(name='advertise_server_to_increase_brand_recognition')
    async def advertise(self, ctx):
        await ctx.send(f'!discord DataFace')

    '''
    
    '''
    #@commands.command(name='savecfb')
    async def save_cfb(self, ctx):

       #if()
       await None

    '''
    Command: !mari - takes in a IRCstream and adds Marisa's flourishes to it
    '''
    @commands.command(name='mari')
    async def mari_text(self, ctx):
        irc_string = ctx.content[6:] #ignores command str len
        #for i in irc_string:
        flourishes = [" ze! ", " wa yo. ", " daro. "]
        rand = random.randint(1, 5)
        try:
            if(rand % 3 == 0):
                irc_string = irc_string.replace( ". ", flourishes[0], 1)
                rand = random.randint(1, 5)
            elif(rand % 3 == 1):
                irc_string = irc_string.replace(". ", flourishes[2], 1)
                rand = random.randint(1, 5)
            elif(rand % 3 == 2):
                irc_string = irc_string.replace(". ", flourishes[1], 1)
                rand = random.randint(1, 5)
        except:
            IOError()
        try:
            irc_string = irc_string.replace( ", ", " da ze, ")
        except:
            IOError()
        try:
            irc_string = irc_string.replace("! ", " da! ")
        except:
            IOError()
        try:
            irc_string = irc_string.replace("? ", " ne da ze? ")
        except:
            IOError()
        if(rand%2 == 0):
            irc_string = "yare yare, " + irc_string
        elif(rand%2 == 1):
            irc_string += " yare yare..."
        await ctx.send(f'' + irc_string)
        '''
               def find_sub(in_str, start, end):
                    return re.sub(
                        r'(?<={}).*?(?={})'.format(re.escape(start), re.escape(end)),
                        lambda m: m.group().strip().replace('.', ' ze!'),
                        in_str)
                '''

#-------------------------------------------------------------------------------------------------------------#
############################################### PICTURE SCRAPING ##############################################
#-------------------------------------------------------------------------------------------------------------#

    '''
    Command: !ayapic - Queries safebooru and returns a link to a picture of
                       Aya Shameimaru
    '''
    @commands.command(name='ayapic')
    async def aya_picture_sfw(self, ctx):
        #global prev_url
        #print(ctx.channel)
        global plebfilter
        #print(noayapic[0])
        if(str(ctx.channel).strip() in plebfilter):
            await ctx.send(f"too hot for #{ctx.channel}")
            return

        global backup_links
        '''try:
            loc_purl = prev_url.pop()
        except:
            IndexError
            loc_purl=''
        client = Danbooru(site_name='safebooru')
        ''''''
        '
        randr = random.randint(1,6)
        if(randr==1):
            init_page = random.randint(1,50)
        elif(randr==2):
            init_page = random.randint(51,100)
        elif(randr==3):
            init_page = random.randint(101,150)
        elif(randr==4):
            init_page = random.randint(151,200)
        else:
            init_page = random.randint(201, 250)
        '''
        client = Danbooru(site_name='safebooru')
        #client = Moebooru(site_name='konachan')
        init_page = random.randint(2, 250)
        rand = random.randint(1,21)
        def get_img_url():
            try:
                ayapiclist = client.post_list(limit=1, page=init_page, tags=["shameimaru_aya"], rand=True, rating='safe')
                print('Image queried from ' + client.site_name)
            except:
                commands.CommandError
                print('Image query from ' + client.site_name + ' failed. Sending local pulled image link.')
                url = str(backup_links[random.randint(0, len(backup_links) - 1)])
                return url

            #    ayapiclist = client.post_list(limit=1, page=init_page+1, tags="shameimaru_aya", rand=True, rating='safe')
            print(ayapiclist)
            #really fucking gross code to partition metadata down to a single url
            url_str = str(ayapiclist).partition("'file_url':")[2]
            urls = url_str.split(',')
            print(urls)
            url = urls[0].strip(" ").strip("'")
            return url
        url = get_img_url()
        await ctx.send(f'' + url)

    '''
        Function: danbooru_picture_sfw
        Parameters: 
            self - object pointer
            tag - can be either string or list of tags
        Optional Parameters:
            limit_p - booru page limit when scraping
            init_p - initial page to start on when scraping (defaults to 2 to prevent nsfw)
        Description: Base to make image scraping really easy to do
    '''
    def danbooru_picture_sfw(self, tag, limit_p=250, init_p=2):
        client = Danbooru(site_name='safebooru')
        init_page = random.randint(init_p, limit_p) # Starts at page 2 since sometimes porn slips through the cracks on 1
        #rand = random.randint(1, 21) # Frankly, I have no idea why this is here but I'll keep it just incase
        def get_img_url():
            try:
                piclist = client.post_list(limit=1, page=init_page, tags=tag, rand=True, rating='safe')
                print('Image queried from ' + client.site_name)
            except:
                commands.CommandError
                print('Image query from ' + client.site_name + ' failed.')
            print(piclist)
            # really fucking gross code to partition metadata down to a single url
            # its just a few string operations and is still fast enough so whatever
            url_str = str(piclist).partition("'file_url':")[2]
            urls = url_str.split(',')
            print(urls)
            url = urls[0].strip(" ").strip("'")
            return url
        return get_img_url()

    '''
        maripic for clod
     '''

    @commands.command(name='maripic')
    async def mari_picture_sfw(self, ctx):
        mari_channels = ["claude", "darko_rta","electra_rta", "thelcc"]
        if (str(ctx.channel).strip().lower() not in mari_channels):
            await ctx.send(f"too hot for #{ctx.channel}")
            return
        url = self.danbooru_picture_sfw('kirisame_marisa')
        await ctx.send(f'' + url)

    '''
        tsukipic for clod
    '''
    @commands.command(name='tsukipic')
    async def tsukihime_picture_sfw(self, ctx):
        global melty_tags
        tags = ["tsukihime", "melty_blood"]
        little_art = ["roa", "mech", "neco", "nac", "wara", "hime", "nero", "nanaya", "warc", "miyako"]
        chat = str(ctx.content)
        msg = chat[10:].strip()
        if(msg.lower() in melty_tags.keys()):
            tags.append(melty_tags[msg.lower()])
        elif(msg.lower() == "-keywords" or msg.lower() == "-keys"):
            keys = []
            for i in melty_tags.keys():
                keys.append(i)
            await ctx.send(f'{str(keys).strip("[").strip("]")}')
        elif(msg.lower() == "-tags"):
            tags = []
            for i in melty_tags.values():
                tags.append(i)
            await ctx.send(f'{str(tags).strip("[").strip("]")}, nakadashi ;)')
        elif(msg.lower() == "hisui drip"):
            url = 'https://i.imgur.com/9oCJoKQ.png'
            await ctx.send(f'' + url)
            return
        if(msg.lower() in little_art):
            url = self.danbooru_picture_sfw(tags, limit_p=20, init_p=1)
        else:
            url = self.danbooru_picture_sfw(tags)
        await ctx.send(f'' + url)

    '''
        amepic for amy
    '''
    @commands.command(name='amepic')
    async def ame_picture_sfw(self, ctx):
        tags = "watson_amelia"
        if (str(ctx.channel).strip() != "amyrosalina"): # and ctx.author.name != "amyrosalina" or ctx.author.name == "electra_rta"):
            await ctx.send(f"too hot for #{ctx.channel}")
            return
        #elif(str(ctx.channel).strip() != "amyrosalina" and ctx.author.name == "amyrosalina" or ctx.author.name == "electra_rta"):
        #    url = self.danbooru_picture_sfw(tags)
        #    await ctx.send(f'PRIVMSG jtv :/w amyrosalina ' + url)
        #    return
        url = self.danbooru_picture_sfw(tags)
        await ctx.send(f'' + url)

    '''
        etrianpic for me and rosael
    '''
    @commands.command(name='etrianpic')
    async def etrian_picture_sfw(self, ctx):
        tags = ["sekaiju_no_meikyuu"]
        url = self.danbooru_picture_sfw(tags, init_p=1, limit_p=7)
        await ctx.send(f'' + url)

    '''
        mothmanpic
    '''
    @commands.command(name='mothmanpic')
    async def mothman_pic_sfw(self, ctx):
        tags = ['mothman_(megami_tensei)']
        url = self.danbooru_picture_sfw(tags)
        await ctx.send(f'' + url)

# -------------------------------------------------------------------------------------------------------------#
##############################################   GACHA COMMANDS   ##############################################
# -------------------------------------------------------------------------------------------------------------#

    '''
    Command: !hornedanimegacha
    TODO: write to file to collect usage data for use later
    '''
    @commands.command(name='hornedanimegacha')
    async def hornedanimes(self, ctx):
        global ha_list
        try:
            ha_rand = random.randint(0,len(ha_list)-1)
            g_rand = random.randint(0, 101)
            print(str(ha_rand) +'|'+str(g_rand))
        except:
            IndexError
            print(str(ha_rand) +'|'+str(g_rand))
        stars = 0
        if(g_rand >= 1 and g_rand <= 45):
            stars=1
        elif(g_rand > 45 and g_rand <= 70):
            stars=2
        elif (g_rand > 70 and g_rand <= 85):
            stars = 3
        elif (g_rand > 85 and g_rand <= 96):
            stars = 4
        elif (g_rand > 97 and g_rand <= 100):
            stars = 5
        shiny = random.randint(0,8193)
        if(shiny == 8192):
            await ctx.send(f'{ctx.author.name} rolled a ' + str(stars) + '☆ ' + 'Shiny' + str(ha_list[ha_rand]) + '!!!!!!!!!!!!!!!')
            return
        await ctx.send(f'{ctx.author.name} rolled a ' + str(stars) + '☆ ' + str(ha_list[ha_rand]))

    '''
    
    '''
    @commands.command(name='hagweights')
    async def hagw(self, ctx):
        await ctx.send(f' | 1☆~45% | 2☆~25% | 3☆~15% | 4☆~10% | 5☆<5% |')

    '''
        Etrian
    '''
    @commands.command(name='etrian')
    async def etrian(self, ctx):
        rand = random.randint(0,len(eo_classes)-1)
        metric = \
            [
                'most based',
                'worst',
                'best',
                'most boring',
                'most fun',
                'worst programmed',
                'most weeb',
                'most breakable',
                'most underused',
                'most loliposting',
                'stupidest',
                'most subclassable',
                'least subclassable',
                'most useless',
                'most average',
                'best bunny in',
                'least bunny in',
                'fastest',
                'slowest',
                'least intelligent (with people)',
                'most playtested'
            ]
        met_rand = random.randint(0, len(metric)-1)
        await ctx.send(f'The {metric[met_rand]} Etrian is {eo_classes[rand]}')

    '''
        Melty
    '''
    @commands.command(name='melty')
    async def melty(self, ctx):
        global melty_chars
        moons = ["Crecent", "Half", "Full"]
        rand = random.randint(0, len(melty_chars) - 1)
        moon_rand = random.randint(0, len(moons) - 1)
        await ctx.send(f'{ctx.author.name} your new main in melty is {moons[moon_rand]} Moon {melty_chars[rand]}!')

    '''
        Melee
    '''
    @commands.command(name='melee')
    async def melee(self, ctx):
        if (str(ctx.channel).strip() != "liquidsquidd" and str(ctx.channel).strip() != "mpghappiness" and str(ctx.channel).strip() != "electra_rta" and str(ctx.channel).strip() != "darko_rta"):
            await ctx.send(f"too hot for #{ctx.channel}")
            return
        global melee_chars
        rand = random.randint(0, len(melee_chars) - 1)
        await ctx.send(f'{ctx.author.name} your new main in melee is {melee_chars[rand]}!')

    """
        Soku
    """
    @commands.command(name ='soku')
    async def soku(self, ctx):
        global soku_chars
        rand = random.randint(0, len(soku_chars) - 1)
        await ctx.send(f'{ctx.author.name} your new main in Touhou 12.3 Hisoutensoku is {soku_chars[rand]}!')

    """
        Demon
    """
    @commands.command(name='demongacha')
    async def demongacha(self, ctx):
        global demons_nocturne
        demon_names = list(demons_nocturne.keys())
        rand = random.randint(0, len(demon_names) - 1)
        #if(ctx.message[6:].lower() == 'gacha'):
        g_rand = random.randint(0, 101)
        stars = 1
        if (g_rand >= 1 and g_rand <= 45):
            stars = 1
        elif (g_rand > 45 and g_rand <= 70):
            stars = 2
        elif (g_rand > 70 and g_rand <= 85):
            stars = 3
        elif (g_rand > 85 and g_rand <= 96):
            stars = 4
        elif (g_rand > 97 and g_rand <= 100):
            stars = 5
        await ctx.send(f'{ctx.author.name} summoned a {stars}☆ {demon_names[rand]}! {demons_nocturne[demon_names[rand]]}')

    # -------------------------------------------------------------------------------------------------------------#
    ##############################################   QUOTE COMMANDS   ##############################################
    # -------------------------------------------------------------------------------------------------------------#

    '''
        takuyaquote
    '''
    @commands.command(name='takuyaquote')
    async def takuyaquote(self, ctx):
        global takuya_quotes
        rand = random.randint(0, len(takuya_quotes) - 1)
        await ctx.send(f'【Takuya】{takuya_quotes[rand]}')

    '''
        dreamboumtweet
    '''
    @commands.command(name='dreamboumtweet')
    async def dreamboum_tweet(self, ctx):
        rand = random.randint(0, 1618 - 1)
        with open('pt.txt', 'r', encoding='utf8') as fin:
            x = 1
            for l in fin:
                if(x == rand):
                    await ctx.send(f'{l[0:-13]}')
                    return
                else:
                    x+=1

    # -------------------------------------------------------------------------------------------------------------#
    ##############################################   MISC COMMANDS   ##############################################
    # -------------------------------------------------------------------------------------------------------------#
    '''
    '''
    #@commands.command(name='shittytl')
    async def shittytl(self, ctx):
        tran = Translator()
        text = ctx.content[9:]
        t = tran.translate(text=str(text), src='en', dest='es')
        t = tran.translate(text=str(text), src='es', dest='en')
        t = tran.translate(text=str(text), src='en', dest='es')
        #t2 = tran.translate([text=str(t), dest='en')
        #t3 = tran.translate(text=str(t2), dest='es')
        print(str(t))

    '''
        pyramid
    '''
    '''
    @commands.command(name='pyramid')
    async def pyramid(self, ctx):
        if(ctx.author.name in silenced):
            return
        
        if(msg == '-h'):
            await ctx.send(f'The !pyramid command creates customizable pyramids. '
                           f'Syntax: "!pyramid <EMOTE1> <EMOTE2> <EMOTE3> <ARG>". '
                           f'Text following the command is stripped into argv and '
                           f'supports up to 3 emotes. Deafult settings create pyramids '
                           f'sequentially based on the input. <ARG>: "-s/-sX": creates '
                           f'a single or multiple "stacked" (hence -s) pyramid(s) with 3 different emotes. '
                           f'For more "art" see "!castle <EMOTE>"')
            return
        async def pyramid_5_msgs(msg):
            await ctx.send(f'' + msg)
            await ctx.send(f'' + msg + ' ' + msg)
            await ctx.send(f'' + msg + ' ' + msg + ' ' + msg)
            await ctx.send(f'' + msg + ' ' + msg)
            await ctx.send(f'' + msg)
        msg_list = chat[9:].split(' ')
        print(msg_list)
        async def pyramid_5_msgs_stack(msg_list):
            await ctx.send(f'' + msg_list[0])
            await ctx.send(f'' + msg_list[0] + ' ' + msg_list[1])
            await ctx.send(f'' + msg_list[0] + ' ' + msg_list[1] + ' ' + msg_list[2])
            await ctx.send(f'' + msg_list[0] + ' ' + msg_list[1])
            await ctx.send(f'' + msg_list[0])
        if (len(msg_list) > 3):
            if(msg_list[3] == '-s'):
                await pyramid_5_msgs_stack(msg_list)
            elif(msg_list[3] == '-s2'):
                msg_list2 = msg_list
                msg_list2.remove(msg_list2[3])
                temp = msg_list2.pop(0)
                msg_list2.append(temp)
                await pyramid_5_msgs_stack(msg_list)
                await pyramid_5_msgs_stack(msg_list2)
            elif (msg_list[3] == '-s3'):
                #print(f'msg: {msg_list}')
                msg_list2 = msg_list
                #print(f'msg2: {msg_list2}')
                msg_list2.remove(msg_list2[3])
                #print(f'msg2: {msg_list2}')
                temp = msg_list2.pop(0)
                msg_list2.append(temp)
                #print(f'msg2: {msg_list2}')
                msg_list3 = msg_list2
                #print(f'msg3: {msg_list3}')
                temp = msg_list2.pop(0)
                #print(f'msg3: {msg_list3}')
                msg_list3.append(temp)
                #print(f'msg3: {msg_list3}')
                await pyramid_5_msgs_stack(msg_list)
                await pyramid_5_msgs_stack(msg_list2)
                await pyramid_5_msgs_stack(msg_list3)
            elif(len(msg_list) > 3 and msg_list[3] != '-s' and msg_list[3] != '-s3'):
                await ctx.send(f"I'm a bot lazily written in python bro, you're gonna blow my stack if ya' don't cool it")
        elif(len(msg_list) > 1):
            for i in msg_list:
                await pyramid_5_msgs(i)
            return
        else:
            await pyramid_5_msgs(msg)

    '''

    '''
        pyramid5x
    '''
    '''
    @commands.command(name='castle')
    async def castle(self, ctx):
        if (ctx.author.name in silenced):
            return
        chat = str(ctx.content)
        msg = chat[8:].strip()
        await ctx.send(f'' + msg)
        await ctx.send(f'' + msg + ' ' + msg)
        await ctx.send(f'' + msg + ' ' + msg + ' ' + msg)
        await ctx.send(f'' + msg + ' ' + msg)
        await ctx.send(f'' + msg)
        await ctx.send(f'' + msg)
        await ctx.send(f'' + msg + ' ' + msg)
        await ctx.send(f'' + msg + ' ' + msg + ' ' + msg)
        await ctx.send(f'' + msg + ' ' + msg + ' ' + msg + ' ' + msg)
        await ctx.send(f'' + msg + ' ' + msg + ' ' + msg + ' ' + msg + ' ' + msg)
        await ctx.send(f'' + msg + ' ' + msg + ' ' + msg + ' ' + msg)
        await ctx.send(f'' + msg + ' ' + msg + ' ' + msg)
        await ctx.send(f'' + msg + ' ' + msg)
        await ctx.send(f'' + msg)
        await ctx.send(f'' + msg)
        await ctx.send(f'' + msg + ' ' + msg)
        await ctx.send(f'' + msg + ' ' + msg + ' ' + msg)
        await ctx.send(f'' + msg + ' ' + msg)
        await ctx.send(f'' + msg)
'''

    @commands.command(name='reggie')
    async def reggie(self, ctx):
        await ctx.send(f'https://i.imgur.com/ZsAZXS9h.jpg')

    @commands.command(name='tridance')
    async def tridance(self, ctx):
        await ctx.send(f'https://i.imgur.com/3HGV7Hy')

    @commands.command(name='434')
    async def four_three_four(self, ctx):
        await ctx.send(f'https://twitter.com/LiquidSquid_/status/1215446601810042880?s=20')

    '''
    
    '''
    #@commands.command(name='furpost')
    async def furry_yiffer_response_generator(self, ctx):
        text=\
        [
            'hmmm pog'
        ]
        return

    #@commands.command(name="uptime")
    async def uptime(self, ctx):
        time_now = datetime.now()
        time_started = self.get_channel(ctx.channel).started_at()
        time_live_sec = (time_now.hour*3600 + time_now.minute*60 + time_now.second) - (time_started.hour*3600 + time_started.minute*60 + time_started.second)
        hrs = 0
        mins = 0
        secs = 0
        while(time_live_sec > 0):
            if(time_live_sec >= 3600):
                hrs+=1
                time_live_sec -= 3600
            elif(time_live_sec < 3600 and time_live_sec >= 60):
                mins+=1
                time_live_sec -= 60
            elif(time_live_sec < 60):
                secs = time_live_sec
                time_live_sec = 0
        await ctx.send(f"{ctx.channel} has been live for {hrs} Hours {mins} Minutes and {secs} Seconds") #whisper coroutine

    # -------------------------------------------------------------------------------------------------------------#
    #########################################   JOIN/LEAVE COMMANDS   ##############################################
    # -------------------------------------------------------------------------------------------------------------#
    '''
    Command: joinch - adds channel to channels.txt and joins bot to 
                    channel if they are not in the file.
    '''
    @commands.command(name='joinch')
    async def joinch(self, ctx):
        ch = ctx.author.name
        print(f'channel to be searched for: ' + ch)
        with open('channels.txt', 'r+') as fin:
            print(f'file: channels.txt - opened as readonly+')
            for l in fin.readlines():
                print(ch + '|' + l.strip())
                if (ch.lower() == l.strip().lower()):
                    await ctx.send(f'' + ch + ' is already in the list of joined channels')
                    print(f'status: breaking loop')
                    print(f'file: channels.txt - closed')
                    return
            fin.write('\n' + ch)
            print(f'file: channels.txt - appended string: "' + ch)
            fin.close()
            print(f'file: channels.txt - closed')
            # await self.event_join(ch)
            await ctx.send(f'' + ch + ' is now joined and added to the list of joined channels')

    '''
    Command: joinch - adds channel to channels.txt and joins bot to 
             channel if they are not in the file.
    '''
    @commands.command(name='channeladd')
    async def channeladd(self, ctx):
        if(ctx.author.name in superuser):
            ch = ctx.content[12:].strip()
            print(f'channel to be searched for: ' + ch)
            with open('channels.txt', 'r+') as fin:
                print(f'file: channels.txt - opened as readonly+')
                for l in fin.readlines():
                    print(ch + '|' + l.strip())
                    if (ch == l.strip()):
                        await ctx.send(f'' + ch + ' is already in the list of joined channels')
                        print(f'status: breaking loop')
                        print(f'file: channels.txt - closed')
                        return
                fin.write('\n' + ch)
                print(f'file: channels.txt - appended string: "' + ch)
                fin.close()
                print(f'file: channels.txt - closed')
                # await self.event_join(ch)
                await ctx.send(f'' + ch + ' is now joined and added to the list of joined channels')
        else:
            return

    '''

    '''
    @commands.command(name='leavech')
    async def leavech(self, ctx):
        succ = 0
        ch = ctx.author.name
        print(f'channel to be searched for: ' + ch)
        with open('channels.txt', 'r') as fin:
            print(f'file: channels.txt - opened as readonly')
            channels = fin.readlines()
            last = channels[-1].strip('\n')
            with open('channels.txt', 'w') as fin:
                for l in channels:
                    print(ch + '|' + l.strip('\n'))
                    if (l.strip('\n') != ch and l.strip(
                            '\n') == last):  # or l.strip('\n') == channels[-2].strip('\n')):
                        fin.write(l.strip('\n'))
                    elif (l.strip('\n') != ch):
                        fin.write(l.strip() + '\n')
                    else:
                        succ += 1
                        # await self.event_part(ch) #does nothing
                        await ctx.send(f'{self.nick} has left ' + ch + '')
                if (succ == 1):
                    return
                else:
                    await ctx.send(f'' + ch + ' is not in the list of joined channels')

    '''

    '''
    @commands.command(name='channelremove')
    async def channelremove(self, ctx):
        if(ctx.author.name in superuser):
            succ = 0
            ch = ctx.content[len('channelremove'):].strip()
            print(f'channel to be searched for: ' + ch)
            with open('channels.txt', 'r') as fin:
                print(f'file: channels.txt - opened as readonly')
                channels = fin.readlines()
                last = channels[-1].strip('\n')
                with open('channels.txt', 'w') as fin:
                    for l in channels:
                        print(ch + '|' + l.strip('\n'))
                        if (l.strip('\n') != ch and l.strip(
                                '\n') == last):  # or l.strip('\n') == channels[-2].strip('\n')):
                            fin.write(l.strip('\n'))
                        elif (l.strip('\n') != ch):
                            fin.write(l.strip() + '\n')
                        else:
                            succ += 1
                            # await self.event_part(ch) #does nothing
                            await ctx.send(f'{self.nick} has left ' + ch + '')
                    if (succ == 1):
                        return
                    else:
                        await ctx.send(f'' + ch + ' is not in the list of joined channels')
        else:
            return

    '''
    Command: !commandlist
    '''
    @commands.command(name='commandlist')
    async def my_command(self, ctx):
        await ctx.send(f'{ctx.author.name}, here are the current list of commands: "!cfb",'
                       f' "!grim" (NOT WORKING), "!lunch", "!carl", "!pyramid" (DEAD), '
                       f'"!mari <CHAT_MSG>", "!(aya, mari, tsuki, etrian, ame)pic", "!hornedanimegacha", "!etrian",'
                       f' "!joinch, !channeladd {ctx.author.name}", "!leavech, !channelremove {ctx.author.name}",'
                       f' and "!pasta"')

    '''
    
    '''
    @commands.command(name='infodump')
    async def infodump(self, ctx):
        global demons_nocturne
        await ctx.send(f'Pastas: {str(len(pasta_str))} |'
                       f' HornedAnimes: {str(len(ha_list))} |'
                       f' Etrians: {str(len(eo_classes))} |'
                       f' Meltys: {str(len(melty_chars) * 3)} |'
                       f' Melees: {str(len(melee_chars))} |'
                       f' Sokus: {str(len(soku_chars))} |'
                       f' Demons: {str(len(list(demons_nocturne.keys())))} |'
                       f' Dreamboum Tweets Locally Scraped: 1618 |'
                       f' Questionable lines of code: 1545')

'''             

'''
if(__name__ == '__main__'):
    print(f'Total Pastas: {str(len(pasta_str))}')
    print(f'Total HornedAnimes: {str(len(ha_list))}')
    print(f'Total Etrians: {str(len(eo_classes))}')
    '''x=0
    for i in pasta_str:
        if ("claude" in i or "Claude" in i or "Clod" in i or "clod" in i):
            x+=1
    print(f'Number of Claude Pastas: {x}')
    '''#with open('copypastas', 'w') as fin:
        #for i in pasta_str:
    #    fin.writelines(str(pasta_str))

    blueayachan = BlueAyaChan()
    blueayachan.run()