from analysis import *
import telebot
import os
from config import BOT_TOKEN

# Initialize bot
bot = telebot.TeleBot(BOT_TOKEN)

# Helper function to extract text from message
def get_text_from_message(message):
    # If replying to a message, use that text
    if message.reply_to_message and message.reply_to_message.text:
        return message.reply_to_message.text
    # If command has text after it
    elif message.text and len(message.text.split()) > 1:
        return message.text.split(' ', 1)[1]
    # If just text message
    elif message.text and not message.text.startswith('/'):
        return message.text
    else:
        return None

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = """
📝 **WordCounterBot** 📝

Your complete text analysis tool!

**Available Commands:**
/start - Show this message
/help - Show this message
/count - Quick word & character count
/full_analysis - Complete text analysis
/word_count - Count words
/char_count - Count characters
/sentence_count - Count sentences
/paragraph_count - Count paragraphs
/syllable_count - Count syllables
/unique_words - Count unique words
/repeated_words - Find repeated words
/longest_words - Show longest words
/shortest_words - Show shortest words
/average_length - Average word length
/readability - Check readability score
/word_frequency - Show word frequency

**How to use:**
Send any text or use /command followed by text
Example: /word_count Hello world

Made with ❤️
"""
    bot.reply_to(message, welcome_text, parse_mode='Markdown')

@bot.message_handler(commands=['count'])
def quick_count(message):
    """Quick word and character count"""
    text = get_text_from_message(message)
    if text:
        words = count_words(text)
        chars = count_characters(text)
        chars_no_space = count_characters_no_spaces(text)
        sentences = count_sentences(text)
        
        response = f"📊 **Quick Count**\n\n"
        response += f"📝 Words: {words}\n"
        response += f"🔤 Characters: {chars}\n"
        response += f"🔤 Characters (no spaces): {chars_no_space}\n"
        response += f"📖 Sentences: {sentences}\n"
        response += f"\nSend `/full_analysis` for detailed analysis!"
        
        bot.reply_to(message, response, parse_mode='Markdown')
    else:
        bot.reply_to(message, "❌ Please send text after the command.\nExample: `/count Hello world`", parse_mode='Markdown')

@bot.message_handler(commands=['word_count'])
def word_count_command(message):
    text = get_text_from_message(message)
    if text:
        bot.reply_to(message, f"📝 **Word Count:** {count_words(text)}", parse_mode='Markdown')
    else:
        bot.reply_to(message, "❌ Please send text after the command.\nExample: `/word_count Hello world`", parse_mode='Markdown')

@bot.message_handler(commands=['char_count'])
def char_count_command(message):
    text = get_text_from_message(message)
    if text:
        chars = count_characters(text)
        chars_no_space = count_characters_no_spaces(text)
        response = f"🔤 **Character Count**\n\nWith spaces: {chars}\nWithout spaces: {chars_no_space}"
        bot.reply_to(message, response, parse_mode='Markdown')
    else:
        bot.reply_to(message, "❌ Please send text after the command.\nExample: `/char_count Hello world`", parse_mode='Markdown')

@bot.message_handler(commands=['sentence_count'])
def sentence_count_command(message):
    text = get_text_from_message(message)
    if text:
        bot.reply_to(message, f"📖 **Sentence Count:** {count_sentences(text)}", parse_mode='Markdown')
    else:
        bot.reply_to(message, "❌ Please send text after the command.\nExample: `/sentence_count Hello world. How are you?`", parse_mode='Markdown')

@bot.message_handler(commands=['paragraph_count'])
def paragraph_count_command(message):
    text = get_text_from_message(message)
    if text:
        bot.reply_to(message, f"📄 **Paragraph Count:** {count_paragraphs(text)}", parse_mode='Markdown')
    else:
        bot.reply_to(message, "❌ Please send text after the command.\nExample: `/paragraph_count Hello\\n\\nWorld`", parse_mode='Markdown')

@bot.message_handler(commands=['syllable_count'])
def syllable_count_command(message):
    text = get_text_from_message(message)
    if text:
        bot.reply_to(message, f"🔊 **Syllable Count:** {count_syllables(text)}", parse_mode='Markdown')
    else:
        bot.reply_to(message, "❌ Please send text after the command.\nExample: `/syllable_count Hello`", parse_mode='Markdown')

@bot.message_handler(commands=['unique_words'])
def unique_words_command(message):
    text = get_text_from_message(message)
    if text:
        unique = count_unique_words(text)
        total = count_words(text)
        response = f"🔢 **Unique Words**\n\nUnique: {unique}\nTotal: {total}\nRatio: {round((unique/total)*100, 2)}%"
        bot.reply_to(message, response, parse_mode='Markdown')
    else:
        bot.reply_to(message, "❌ Please send text after the command.\nExample: `/unique_words Hello world hello`", parse_mode='Markdown')

@bot.message_handler(commands=['repeated_words'])
def repeated_words_command(message):
    text = get_text_from_message(message)
    if text:
        repeated = find_repeated_words(text)
        if repeated:
            response = "🔄 **Repeated Words:**\n" + "\n".join([f"- {word}: {count} times" for word, count in repeated.items()])
            bot.reply_to(message, response, parse_mode='Markdown')
        else:
            bot.reply_to(message, "✅ No repeated words found.", parse_mode='Markdown')
    else:
        bot.reply_to(message, "❌ Please send text after the command.\nExample: `/repeated_words Hello world hello`", parse_mode='Markdown')

@bot.message_handler(commands=['longest_words'])
def longest_words_command(message):
    text = get_text_from_message(message)
    if text:
        longest = find_longest_words(text, 5)
        if longest:
            response = "📏 **Longest Words:**\n" + "\n".join([f"- {word} ({len(word)} letters)" for word in longest])
            bot.reply_to(message, response, parse_mode='Markdown')
        else:
            bot.reply_to(message, "No words found.", parse_mode='Markdown')
    else:
        bot.reply_to(message, "❌ Please send text after the command.\nExample: `/longest_words This is a sample text`", parse_mode='Markdown')

@bot.message_handler(commands=['shortest_words'])
def shortest_words_command(message):
    text = get_text_from_message(message)
    if text:
        shortest = find_shortest_words(text, 5)
        if shortest:
            response = "📏 **Shortest Words:**\n" + "\n".join([f"- {word} ({len(word)} letters)" for word in shortest])
            bot.reply_to(message, response, parse_mode='Markdown')
        else:
            bot.reply_to(message, "No words found.", parse_mode='Markdown')
    else:
        bot.reply_to(message, "❌ Please send text after the command.\nExample: `/shortest_words This is a sample text`", parse_mode='Markdown')

@bot.message_handler(commands=['average_length'])
def average_length_command(message):
    text = get_text_from_message(message)
    if text:
        avg = average_word_length(text)
        bot.reply_to(message, f"📊 **Average Word Length:** {avg} characters", parse_mode='Markdown')
    else:
        bot.reply_to(message, "❌ Please send text after the command.\nExample: `/average_length This is a sample text`", parse_mode='Markdown')

@bot.message_handler(commands=['readability'])
def readability_command(message):
    text = get_text_from_message(message)
    if text:
        score = readability_score(text)
        # Interpret the score
        if score >= 90:
            level = "Very Easy (5th grade level)"
        elif score >= 80:
            level = "Easy (6th grade level)"
        elif score >= 70:
            level = "Fairly Easy (7th grade level)"
        elif score >= 60:
            level = "Standard (8th-9th grade level)"
        elif score >= 50:
            level = "Fairly Difficult (10th-12th grade level)"
        elif score >= 30:
            level = "Difficult (College level)"
        else:
            level = "Very Difficult (College graduate level)"
        
        response = f"📊 **Readability Score:** {score}/100\n**Level:** {level}"
        bot.reply_to(message, response, parse_mode='Markdown')
    else:
        bot.reply_to(message, "❌ Please send text after the command.\nExample: `/readability This is a sample text`", parse_mode='Markdown')

@bot.message_handler(commands=['word_frequency'])
def word_frequency_command(message):
    text = get_text_from_message(message)
    if text:
        freq = word_frequency(text)
        # Get top 10 most common words
        top_words = freq.most_common(10)
        response = "📊 **Word Frequency (Top 10):**\n\n"
        for word, count in top_words:
            response += f"- {word}: {count} times\n"
        bot.reply_to(message, response, parse_mode='Markdown')
    else:
        bot.reply_to(message, "❌ Please send text after the command.\nExample: `/word_frequency This is a sample text`", parse_mode='Markdown')

@bot.message_handler(commands=['full_analysis'])
def full_analysis_command(message):
    text = get_text_from_message(message)
    if text:
        analysis = full_analysis(text)
        response = f"📝 **Full Text Analysis**\n\n"
        response += f"📝 Words: {analysis['Word Count']}\n"
        response += f"🔤 Characters: {analysis['Character Count']}\n"
        response += f"🔤 Characters (no spaces): {analysis['Characters (no spaces)']}\n"
        response += f"📖 Sentences: {analysis['Sentence Count']}\n"
        response += f"📄 Paragraphs: {analysis['Paragraph Count']}\n"
        response += f"🔊 Syllables: {analysis['Syllable Count']}\n"
        response += f"🔢 Unique Words: {analysis['Unique Words']}\n"
        response += f"📏 Avg Word Length: {analysis['Average Word Length']}\n"
        response += f"📊 Avg Words/Sentence: {analysis['Average Words per Sentence']}\n"
        response += f"🔣 Special Characters: {analysis['Special Characters']}\n"
        response += f"🔢 Numbers Found: {analysis['Numbers Found']}\n"
        response += f"📊 Readability Score: {analysis['Readability Score']}/100\n\n"
        
        # Add repeated words if any
        if analysis['Repeated Words']:
            response += "**Repeated Words:**\n"
            for word, count in list(analysis['Repeated Words'].items())[:5]:
                response += f"- {word}: {count} times\n"
            if len(analysis['Repeated Words']) > 5:
                response += f"... and {len(analysis['Repeated Words']) - 5} more\n"
            response += "\n"
        
        # Add longest words
        if analysis['Longest Words']:
            response += "**Longest Words:**\n"
            for word in analysis['Longest Words']:
                response += f"- {word}\n"
            response += "\n"
        
        # Add parts of speech
        response += f"**Nouns:** {', '.join(analysis['Nouns'][:5])}{'...' if len(analysis['Nouns']) > 5 else ''}\n"
        response += f"**Verbs:** {', '.join(analysis['Verbs'][:5])}{'...' if len(analysis['Verbs']) > 5 else ''}\n"
        response += f"**Adjectives:** {', '.join(analysis['Adjectives'][:5])}{'...' if len(analysis['Adjectives']) > 5 else ''}\n"
        response += f"**Adverbs:** {', '.join(analysis['Adverbs'][:5])}{'...' if len(analysis['Adverbs']) > 5 else ''}\n"
        
        bot.reply_to(message, response, parse_mode='Markdown')
    else:
        bot.reply_to(message, "❌ Please send text after the command.\nExample: `/full_analysis Your text here`", parse_mode='Markdown')

# Handle plain text messages (auto-analyze)
@bot.message_handler(func=lambda message: True)
def auto_analyze(message):
    text = get_text_from_message(message)
    if text and not message.text.startswith('/'):
        # Quick analysis
        words = count_words(text)
        chars = count_characters(text)
        sentences = count_sentences(text)
        unique = count_unique_words(text)
        
        response = f"📊 **Quick Analysis:**\n\n"
        response += f"📝 Words: {words}\n"
        response += f"🔤 Characters: {chars}\n"
        response += f"📖 Sentences: {sentences}\n"
        response += f"🔢 Unique Words: {unique}\n\n"
        response += f"Send `/full_analysis` for detailed analysis!\n"
        response += f"Send `/count` for more stats!"
        
        bot.reply_to(message, response, parse_mode='Markdown')
