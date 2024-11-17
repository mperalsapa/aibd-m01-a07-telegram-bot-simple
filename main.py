# importa l'API de Telegram
from telegram.ext import Application, CommandHandler,ContextTypes
from telegram import Update

import psutil

# defineix una funció start que saluda i que s'executarà quan el bot rebi el missatge /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Inform user about what this bot can do"""
    await update.message.reply_text(
        "👏👏 Felicitats! Tot el món mundial ja pot parlar amb el bot!!! 🎉 🎊"
    )

async def cpu_usage(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f"L'us de la CPU es de: {psutil.cpu_percent(1)} %"
    )

async def ram_usage(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    memoria = psutil.virtual_memory()
    await update.message.reply_text(
        f"L'us de la memoria RAM es de: {memoria[2]} %.\nL'us de memoria RAM es de: {memoria[3]/1024/1024/1024} GB.\nLa memoria total es de {memoria[0]/1024/1024/1024} GB."
    )


def main():
    # declara una constant amb el access token que llegeix de token.txt
    TOKEN = open('./token.txt').read().strip()
    print(TOKEN)
    
    application = Application.builder().token(TOKEN).build()
    #Definim les opcions que podrà executar
    application.add_handler(CommandHandler("start", start))

    # Definim les opcions personalitzades
    application.add_handler(CommandHandler("cpu_usage", cpu_usage))
    application.add_handler(CommandHandler("ram_usage", ram_usage))


    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()