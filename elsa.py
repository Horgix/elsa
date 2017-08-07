#! /usr/bin/env python

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
def vote(message, vote):
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
def source(message):
    message.send('https://github.com/Horgix/elsa ; et OUI c\'est sale. Très.')

@listen_to('!how')
@respond_to('!how')
def how(message):
    message.send('How do I run ? Well... I **might** be running inside a tmux, directly called from the CLI. But that would be ugly, wouldn\'t it ? Eh.')

@listen_to('!why')
@respond_to('!why')
def why(message):
    message.send('Because jubon. Oh, and Olaf !')

@listen_to('!when')
@respond_to('!when')
def why(message):
    message.send('Really ? Maybe you should stop here, no ? :)')

@listen_to('!400')
@respond_to('!400')
def badr_request(message):
    message.send('400 Badr Request')

@listen_to('!502')
@respond_to('!502')
def badr_gateway(message):
    message.send('502 Badr Gateway')

@listen_to('!battletag (.*)', re.IGNORECASE)
def battletag(message, nick):
    tags = {
            'horgix':   'Horgix#2738',
            'joraf':    'Nekonyaa#2495',
            'jubon':    'Ryf7#2504',
            'kehou':    'Qwazerty#2418',
            'lefer':    'Ahuri3#2473',
            'lulog':    'Krast#2725'
            }
    if nick in tags:
        message.send(tags[nick])
    else:
        message.send("Sorry, no battletag found for " + nick + " :(\n"
                "You can still get the list of which battletags I can handle "
                "using !battletag list in private")

@listen_to('weee', re.IGNORECASE)
@respond_to('weee', re.IGNORECASE)
def weeee(message):
    message.send("https://www.youtube.com/watch?v=wiMGFoOT3aQ")

@listen_to('nuke', re.IGNORECASE)
@respond_to('nuke', re.IGNORECASE)
def weeee(message):
    message.send("https://a-team-survivors.slack.com/files/joraf/F29JQHSS3/nope_nuke.gif")

@listen_to('topkek', re.IGNORECASE)
@respond_to('topkek', re.IGNORECASE)
def topkek(message):
    message.send("https://a-team-survivors.slack.com/files/joraf/F2C2BNBDG/pasted_image_at_2016_09_15_15_39.png")

@respond_to('!battletag (.*)', re.IGNORECASE)
def battletagpriv(message, nick):
    tags = {
            'horgix':   'Horgix#2738',
            'joraf':    'Nekonyaa#2495',
            'jubon':    'Ryf7#2504',
            'kehou':    'Qwazerty#2418',
            'lefer':    'Ahuri3#2473',
            'lulog':    'Krast#2725'
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
def critical(message):
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
            u"Lulog, l'alternant ?",
            u"Quoi les logs ?"
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

@listen_to('ermar !', re.IGNORECASE)
@respond_to('ermar !', re.IGNORECASE)
def ermar(message):
    replies = [
            u"Ermar le canard ! coin \_o< \_o< \__O<",
            u"Eric le porc-épic !",
            u"Eric le nasique !",
            u"Non, c'est Supermar !"
            ]
    message.send(random.choice(replies))

@listen_to(u'l[ée]o !', re.IGNORECASE)
@respond_to(u'l[ée]o !', re.IGNORECASE)
def leo(message):
    replies = [
            u"Léo glassfish !",
            u"Léo mailfish !",
            u"Léo goldfish !",
            u"Léo scalefish !",
            u"Léo cloudfish !",
            u"Léo whiskfish !",
            u"Le ROI léo !"
            ]
    message.send(random.choice(replies))

@listen_to('lefer !', re.IGNORECASE)
@respond_to('lefer !', re.IGNORECASE)
def lefer(message):
    replies = [
            u"La barre lefer, elle peut tout faire !",
            u"Il faut battre lefer quand il est chaud."
            ]
    message.send(random.choice(replies))

@listen_to('joraf !', re.IGNORECASE)
@respond_to('joraf !', re.IGNORECASE)
def joraf(message):
    replies = [
            u"Drakaaaaaaaar !",
            u"Joraf la joraxe !",
            u"Joraf ? Il est toujours sur une autre planète; Evry qu'elle s'appelle",
            u"Vodka !"
            ]
    message.send(random.choice(replies))

@listen_to('alelb !', re.IGNORECASE)
@respond_to('alelb !', re.IGNORECASE)
def alelb(message):
    replies = [
            u"Alelb, le ninja ?",
            u"Heyyy Marriiiiio"
            ]
    message.send(random.choice(replies))

@listen_to('alcho !', re.IGNORECASE)
@respond_to('alcho !', re.IGNORECASE)
def alcho(message):
    replies = [
            u"Alcho, le mangeur de poussins ?",
            u"Créateur ! Gloire à vous !"
            ]
    message.send(random.choice(replies))

@listen_to('popi !', re.IGNORECASE)
@respond_to('popi !', re.IGNORECASE)
def popi(message):
    replies = [
            u"Chocobisous !",
            u"Popi popi, popi pou, popi popi, popi pou...♫",
            u"Je sais bien que tu l'adores (Popineau, Popineau) et qu'elle a de jolis yeux (Popineau, Popineau)...♫"
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
def segir(message):
    replies = [
            u"Segir, l'ivoirien ?",
            u"Couscous !",
            ]
    message.send(random.choice(replies))

@listen_to('seb !', re.IGNORECASE)
@respond_to('seb !', re.IGNORECASE)
def seb(message):
    replies = [
            u"Seb c'est bien.",
            ]
    message.send(random.choice(replies))

@listen_to('ansible', re.IGNORECASE)
@respond_to('ansible', re.IGNORECASE)
def ansible(message):
    r = random.randint(1, 3)
    if r == 1:
        message.send('Salt > Ansible')

@listen_to('(.*)')
@respond_to('(.*)')
def debug(message, content):
    for c in [ answersmap[s] for s in answersmap if s in content.lower() ]:
        message.send(c)
    print(content)

@listen_to('warning')
@respond_to('warning')
def warning(message):
    attachments = [
    {
        'fallback': 'Risel fait des origamis',
        'text': 'Risel fait des origamis',
        'color': 'warning',
    }]
    print(attachments)
    message.send_webapi('', attachments)

@listen_to('!cgtgate')
@respond_to('!cgtgate')
def cgtgate(message):
    excuses = [
        "de la loi travail",
        "de Léo",
        "du gouvernement",
        "de puppet",
        "de gescom",
        "des pluies de grenouilles",
        "du réchauffement climatique",
        "de la panne de la machine à café",
        "des devs",
        "du manager",
        "des outils",
        "du kernel (méchant @joraf)",
        "du suffrage universel direct",
    ]
    message.send("C'est la faute %s !" % random.choice(excuses))

if __name__ == "__main__":
    main()
