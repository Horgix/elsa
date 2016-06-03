# -*- coding: utf-8 -*-

from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import random
import re
import json

def main():
    bot = Bot()
    print('Bot initialized')
    bot.run()

answersmap = {'tais toi elsa': 'wtf ?',
            'coucou elsa': 'wesh',
            'ansible': 'Salt > Ansible',
            'Hi elsa': 'Hi'}

pollquestion = None
polloptions = []
pollres = []

@listen_to('!startpoll "(.*)" (.*)', re.IGNORECASE)
@respond_to('!startpoll "(.*)" (.*)', re.IGNORECASE)
def startpoll(message, question, options):
    global pollquestion
    global polloptions
    global pollres
    pollquestion = None
    polloptions = []
    pollres = []
    message.send("Poll starting: " + question)
    message.send("Options:")
    for option in options.split():
        polloptions.append(option)
        pollres.append(0)
        message.send(str(len(polloptions)) + '. ' + option)
    pollquestion = question

@listen_to('!vote ([0-9]+)', re.IGNORECASE)
#@respond_to('!vote ([0-9]+)', re.IGNORECASE)
def poll(message, vote):
    global pollquestion
    global polloptions
    global pollres
    res = int(vote)
    if res > len(pollres) or res == 0:
        message.send('Out of range ;)')
    else:
        pollres[res - 1] += 1

@listen_to('!result')
@respond_to('!result')
def result(message):
    for option, res in zip(polloptions, pollres):
        message.send(option + ': ' + str(res))

@listen_to('!source')
@respond_to('!source')
def result(message):
    message.send('https://github.com/Horgix/elsa ; et OUI c\'est sale. Très.')

@listen_to('!battletag (.*)', re.IGNORECASE)
def battletag(message, nick):
    tags = {
            'horgix':   'Horgix#2738',
            'joraf':    'Nekonyaa#2495',
            'jubon':    'Ryf7#2504',
            'kehou':    'Qwazerty#2418'
            }
    if nick in tags:
        message.send(tags[nick])
    else:
        message.send("Sorry, no battletag found for " + nick + " :(\n"
                "You can still get the list of which battletags I can handle "
                "using !battletag list in private")

@respond_to('!battletag (.*)', re.IGNORECASE)
def battletagpriv(message, nick):
    tags = {
            'horgix':   'Horgix#2738',
            'joraf':    'Nekonyaa#2495',
            'jubon':    'Ryf7#2504',
            'kehou':    'Qwazerty#2418'
            }
    if nick in tags:
        message.send(tags[nick])
    elif nick == 'list':
        message.send("People I know about : " + ', '.join(tags.keys()))
    else:
        message.send("Sorry, no battletag found for " + nick + " :(")
        message.send("People I know about : " + ', '.join(tags.keys()))

@listen_to('critical')
@respond_to('critical')
def github(message):
    attachments = [
    {
        'fallback': 'LHG is burning !',
        'text': 'LHG is burning !',
        'color': 'danger',
    }]
    print(attachments)
    message.send_webapi('', attachments)

@listen_to('lulog !', re.IGNORECASE)
@respond_to('lulog !', re.IGNORECASE)
def lulog(message):
    replies = [
            u"Lulog, l'alternant ?"
            ]
    message.send(random.choice(replies))

@listen_to('kehou !', re.IGNORECASE)
@respond_to('kehou !', re.IGNORECASE)
def kehou(message):
    replies = [
            u"Mais kehou,  pas là, kehou mais t'es pas là, mais kehou, pas là...",
            u"♫ Coucou kehou, coucou kehou...",
            u"Kehou, le bordelais ?",
            u"Quoi, qu'est ce qu'il a cassé encore ?"
            ]
    message.send(random.choice(replies))

@listen_to('jarou !', re.IGNORECASE)
@respond_to('jarou !', re.IGNORECASE)
def jarou(message):
    replies = [
            u"Jarou, l'intermittent ?",
            u"Jarou, le roi du bricolage !",
            ]
    message.send(random.choice(replies))

@listen_to('loic !', re.IGNORECASE)
@respond_to('loic !', re.IGNORECASE)
def loic(message):
    replies = [
            u"Loic raison !"
            ]
    message.send(random.choice(replies))

@listen_to('joraf !', re.IGNORECASE)
@respond_to('joraf !', re.IGNORECASE)
def loic(message):
    replies = [
            u"Drakaaaaaaaar !",
            u"Joraf la joraxe !",
            u"Joraf ? Il est toujours sur une autre planète; Evry qu'elle s'appelle",
            u"Vodka !"
            ]
    message.send(random.choice(replies))

@listen_to('alelb !', re.IGNORECASE)
@respond_to('alelb !', re.IGNORECASE)
def loic(message):
    replies = [
            u"Alelb, le ninja ?",
            u"Heyyy Marriiiiio"
            ]
    message.send(random.choice(replies))

#@listen_to('!whois ([a-b]+)', re.IGNORECASE)
#@respond_to('!whois ([a-b]+)', re.IGNORECASE)
#def kehou(message, nick):
#    nicks = {
#            'kehou': "Qwazerty"
#            }
#    if nick in nicks:
#        message.send(nicks[nick])
#    else:
#        message.send("I don't know " + nick + ", sorry")

@listen_to('segir !', re.IGNORECASE)
@respond_to('segir !', re.IGNORECASE)
def kehou(message):
    replies = [
            u"Segir, l'ivoirien ?",
            ]
    message.send(random.choice(replies))

@listen_to('(.*)')
@respond_to('(.*)')
def debug(message, content):
    for c in [ answersmap[s] for s in answersmap if s in content.lower() ]:
        message.send(c)
    print(content)

@listen_to('warning')
@respond_to('warning')
def github(message):
    attachments = [
    {
        'fallback': 'Risel fait des origamis',
        'text': 'Risel fait des origamis',
        'color': 'warning',
    }]
    print(attachments)
    message.send_webapi('', attachments)

if __name__ == "__main__":
    main()
