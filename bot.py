from telegram import InlineQueryResultArticle, InputTextMessageContent, \
    InlineQueryResultVideo, ParseMode
import numpy as np
import matplotlib.pyplot as plt
from combi1 import Combi
from combi2 import Combi2


#Vars
part1 = None

#Call functions
def start(update, context):
    update.message.reply_text("¡Bienvenido al bot! Usa los comandos /parte1 y /parte2 para acceder a los respectivos ejercicios")


def help_command(update, context):
    update.message.reply_text("Usa el comando /parte1 para acceder al ejercicio 1 \n /parte2 para el segundo ejercicio.")


def params(text):
    parametros = text.split(",")
    return parametros


def echo(update,context):
    chat_id = update.message.chat.id
    if part1 == True:
        word = params(update.message.text)[0].upper()
        p = params(update.message.text)[1]
        k = params(update.message.text)[2]
        c = Combi(word, p, k)
        update.message.reply_text(
            "Estos son sus parametros: \n\n"
            + "M: "
            + word
            + "\np: "
            + p
            + "\nk: "
            + k
        )
        update.message.reply_text(c.firstP(word, int(p), int(k))+"\n\n"+c.lastP(word, int(p), int(k)))
        update.message.reply_text(f'Se pueden formar {c.getSize(word, int(p), int(k))} palabras de longitud {k} para la palabra "{word}"')
        if c.getSize(word, int(p), int(k))>0:
            fields = c.getCategories(word, int(p), int(k))
            fields[0].sort()
            plt.figure(figsize=(10, 10))
            plt.bar(fields[0],fields[1])
            plt.suptitle('Histograma de totales',fontsize=40)
            plt.xlabel("Letra", fontsize=20)
            plt.ylabel("Total",fontsize=20)
            plt.savefig("multimedia/histograma1.png")
            context.bot.send_photo(chat_id,open("multimedia/histograma1.png", "rb"))
    else:
        n = params(update.message.text)[0]
        p = params(update.message.text)[1]
        k = params(update.message.text)[2]
        c2 = Combi2(n,k,p)
        update.message.reply_text('Estos son sus parámetros:\n\n'+
        'n: '+n+'\np: '+p+'\nk: '+k)
        update.message.reply_text(f'Se puen distribuir {n} objetos en {k} grupos de {c2.distribution(int(n),int(k))} formas.\n')
        nAry=c2.stringConstruction(int(n))
        result2=c2.combAnalisis(nAry,int(p),int(k))
        update.message.reply_text(f'Se pueden formar {len(result2)} cadenas (para un conjunto de {n} elementos) con longitud {k} de tal modo que el 0 y el 1 aparezcan al menos una vez')
        update.message.reply_text(c2.firstandLastP(result2,int(p),int(k)))
        if len(result2)>0:
            fields = c2.getCategories(result2, int(p), int(k))
            fields[0].sort()
            plt.figure(figsize=(10, 10))
            plt.bar(fields[0],fields[1])
            plt.suptitle('Histograma de Promedios',fontsize=40)
            plt.xlabel("Número", fontsize=20)
            plt.ylabel("Promedio",fontsize=20)
            plt.savefig("multimedia/histograma1.png")
            context.bot.send_photo(chat_id,open("multimedia/histograma1.png", "rb"))
        


def parte1(update, context):
    global part1
    part1 = True
    update.message.reply_text(
        "Analisis Combinatorio Parte 1 \nIngrese la palabra y los parametros p y k usando el mismo orden y separados por comas\n\nEjemplo:\nmissisipi,4,5"
    )


def parte2(update, context):
    global part1
    part1= False
    update.message.reply_text("Análisis Combinatorio Parte 2 \nIngrese los parámetros n, p y k  usando el mismo orden y separados por comas\n\nEjemplo:\n5,4,10")

