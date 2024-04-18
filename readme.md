```
# Discord Scoreboard Bot

The Discord Scoreboard Bot is a Python-based Discord bot designed to manage and display scoreboards in Discord channels. It allows users to generate and update scoreboards based on data provided in CSV files, and it automatically sends update messages and images at regular intervals.

## Features

- Generate and display scoreboards based on data from CSV files.
- Automatically update scoreboards and send update messages and images at regular intervals.
- Command-based interaction for managing and updating scoreboards.

## Installation

To use the Discord Scoreboard Bot, you need to have Python installed on your system. You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## Configuration

Before running the bot, you need to configure the following:

1. Discord Bot Token: Replace `'YOUR_DISCORD_BOT_TOKEN'` in the code with your actual Discord bot token.
2. CSV Files: Prepare CSV files containing the scoreboard data (`template.csv` and `template_coordinates.csv` in the provided code).
3. Image and Font Files: Replace `template_image.jpg` with your image file and `template_font.ttf` with your font file.

## Usage

### Commands

- `$scoreboard`: Generates and displays the scoreboard based on data from CSV files. Clears all messages in the channel before sending the update message and image.

### Background Task

The bot also includes a background task that runs every hour to update the scoreboard and send update messages and images automatically.

## Deploy to Heroku

You can deploy this bot to Heroku with one click using the button below:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Contributing

Contributions to the Discord Scoreboard Bot are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on GitHub.

## License

This project is licensed under the [MIT License](LICENSE).
```
