import os
import dotenv
from chatbot.freepikBot import FreepikBot

dotenv.load_dotenv()
token = os.getenv("BOT_TOKEN")

def main():
    bot = FreepikBot(token)
    bot.run()


if __name__ == '__main__':
    main()
