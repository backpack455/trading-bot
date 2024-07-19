# ML Algorithmic Trading Bot (Python, Alpaca, FinBERT)

## Overview

This repository contains a machine learning-based trading bot designed to analyze sentiment from live news events using the FinBERT model and execute trades on the Alpaca platform. The bot aims to enhance trading decisions and improve returns by leveraging sentiment analysis and backtesting strategies.

## Features

- **Sentiment Analysis**: Utilizes the FinBERT model to analyze live news events and determine trading signals.
- **Automated Trading**: Executes buy and sell orders automatically based on the sentiment analysis.
- **Backtesting**: Leverages Lumibot for backtesting with Yahoo Finance API, allowing performance evaluation over a multi-year period.
- **High Performance**: Achieves significant returns, with a reported 234% ROI on backtested data.

## Project Structure

- **core/**: Contains the core logic and helper functions for the trading bot.
- **config/**: Configuration files for setting up the bot.
- **models/**: Machine learning models including the FinBERT model for sentiment analysis.
- **scripts/**: Scripts for data processing and backtesting.
- **README.md**: Project documentation.
- **requirements.txt**: Python dependencies.

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Alpaca API key and secret
- Sufficient funds for trading pairs
- Optional: Telegram bot for notifications

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/backpack455/trading-bot.git
    cd trading-bot
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Configure the environment variables:
    ```sh
    cp config/.env.example config/.env
    # Edit the config/.env file with your API credentials and other configurations
    ```

### Environment Variables

Configure the `config/.env` file with the following variables:
- `ALPACA_API_KEY`: Your Alpaca API key
- `ALPACA_API_SECRET`: Your Alpaca API secret
- `SYMBOL`: The trading pair (e.g., `AAPL_USD`)
- `FINBERT_MODEL`: Path to the FinBERT model
- `NUMBER_OF_GRIDS`: Number of grids for trading strategy (e.g., `100`)
- `QUANTITY_PER_GRID`: Quantity per grid (e.g., `0.07`)
- `TELEGRAM_BOT_API_TOKEN`: Telegram bot token (optional)
- `TELEGRAM_TARGET_CHAT_ID`: Telegram chat ID (optional)

### Running the Bot

To start the trading bot, run:
```sh
python main.py
