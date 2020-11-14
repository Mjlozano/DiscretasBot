from telegram import InlineQueryResultArticle, InputTextMessageContent, \
    InlineQueryResultVideo, ParseMode
import numpy as np
import matplotlib.pyplot as plt
from combi1 import Combi


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
        word = params(update.message.text)[0]
        p = params(update.message.text)[1]
        k = params(update.message.text)[2]
        c = Combi(word, p, k)
        update.message.reply_text(
            "Estos son sus parametros: \n\n"
            + "Palabra: "
            + word
            + "\np: "
            + p
            + "\nk: "
            + k
        )
        update.message.reply_text(c.firstP(word, int(p), int(k))+"\n\n"+c.lastP(word, int(p), int(k)))
        update.message.reply_text(f'Se pueden formar {c.getSize(word, int(p), int(k))} palabras de longitud {k} para la palabra "{word}"')
        fields = c.getCategories(word, int(p), int(k))
        plt.figure(figsize=(10, 10))
        plt.bar(fields[0],fields[1])
        plt.suptitle('Histograma')
        plt.savefig("histograma1.png")
        context.bot.send_photo(chat_id,open("histograma1.png", "rb"))
    else:
        update.message.reply_text("Aqui se manda la parte 2")


def parte1(update, context):
    global part1
    part1 = True
    update.message.reply_text(
        "Analisis Combinatorio Parte 1 \nIngrese la palabra y los parametros p y k separados por comas\n\nEjemplo:\nmissisipi,4,5"
    )


def parte2(update, context):
    global part1
    part1= False
    update.message.reply_text("Menu Problema 2:")

