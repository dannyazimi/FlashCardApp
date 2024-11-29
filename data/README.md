# Flashcard Learning App

This is a Python-based flashcard app that helps users learn using flash cards. The app initially displays French words on a card and shows their English meanings after 3 seconds. Users can mark words as known or unknown, and the app tracks the progress by saving unlearned words to a file.

## Features

- **Interactive Flashcards**: Displays French words with English translations.
- **Progress Tracking**: Saves the words you haven't learned yet into a CSV file.
- **Simple Navigation**: Use the buttons to indicate if you know a word or not.

## How to Use

1. **Prepare the Data**:
   - Place the `french_words.csv` file in the `data` folder. This file should contain French words and their English translations.
   - Example CSV format:
     ```csv
     French,English
     Bonjour,Hello
     Merci,Thank you
     ```
2. **Run the Program**:
   - Execute the script in your Python environment.
   - Use the ✅ button if you know the word, or the ❌ button if you don't.

3. **Track Your Progress**:
   - Known words are removed from the learning list.
   - Remaining words are saved in `data/what_to_learn.csv`.

## Requirements

- Python 3.x
- Libraries:
  - `tkinter` (built-in with Python)
  - `pandas` (install using `pip install pandas`)

## Future Enhancements

1. **Custom CSV Upload**: Allow users to upload their own CSV files with custom words.

2. **Statistics Tracking**: Show progress, such as:
   - Percentage of words learned.
   - Number of words remaining.

3. **Custom Timer**: Let users adjust the time delay before flipping the card.

4. **Audio Pronunciation**: Play audio for the displayed words to improve pronunciation.

5. **Mobile Version**:
   - Build a mobile-friendly version.
6. Add Pomodoro

## Known Limitations

- The app currently supports only the `french_words.csv` file structure.
- Images for the flashcards and buttons must be placed in the `images` folder.