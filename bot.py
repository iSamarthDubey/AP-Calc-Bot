import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')

# Function to calculate nth term of Arithmetic Progression
def calculate_ap(first_term, common_diff, num_terms):
    nth_term = first_term + (num_terms - 1) * common_diff
    return nth_term

async def start(update: Update, context) -> None:
    await update.message.reply_text('Hi! I can calculate Arithmetic Progressions for you. '
                                    'Send values in the format: first_term, common_diff, num_terms')

async def calculate(update: Update, context) -> None:
    try:
        user_input = update.message.text.split(',')
        first_term = float(user_input[0].strip())
        common_diff = float(user_input[1].strip())
        num_terms = int(user_input[2].strip())
        
        result = calculate_ap(first_term, common_diff, num_terms)
        
        await update.message.reply_text(f'The {num_terms}th term of the AP is: {result}')
    
    except (IndexError, ValueError):
        await update.message.reply_text('Please enter the values correctly in the format: first_term, common_diff, num_terms')

async def main():
    # Create the application
    application = Application.builder().token("7432759523:AAHaIa7pCsd94ATzNTUgNZBCwkkaZxbkZz0").build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, calculate))

    # Initialize and run the bot
    await application.initialize()
    await application.start()
    await application.stop()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())