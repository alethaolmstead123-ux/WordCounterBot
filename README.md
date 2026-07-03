# WordCounterBot

A Telegram bot that provides detailed text analysis including word count, character count, sentence count, readability scores, parts of speech extraction, and much more.

## Features

- Word, character, sentence & paragraph counting
- Characters count with and without spaces
- Syllable count
- Unique & repeated word detection
- Longest & shortest words identification
- Average word length & words per sentence
- Parts of speech extraction (nouns, verbs, adjectives, adverbs)
- Flesch Reading Ease score
- Word frequency analysis
- Full comprehensive analysis

## Commands

| Command | Description |
|---------|-------------|
| `/start` | Show welcome message |
| `/help` | Show help message |
| `/count` | Quick word & character count |
| `/full_analysis` | Complete text analysis |
| `/word_count` | Count words |
| `/char_count` | Count characters |
| `/sentence_count` | Count sentences |
| `/paragraph_count` | Count paragraphs |
| `/syllable_count` | Count syllables |
| `/unique_words` | Count unique words |
| `/repeated_words` | Find repeated words |
| `/longest_words` | Show longest words |
| `/shortest_words` | Show shortest words |
| `/average_length` | Average word length |
| `/readability` | Check readability score |
| `/word_frequency` | Show word frequency |

## Deployment

This bot is ready to deploy on Railway.

### Environment Variables Required

- `BOT_TOKEN` - Your Telegram bot token from @BotFather

## Technologies Used

- Python 3.10
- pyTelegramBotAPI (Telegram Bot API wrapper)
