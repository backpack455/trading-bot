# Trading Bot

## Overview

This repository contains a highly configurable grid trading bot for the Backpack Exchange. It is designed to automate trading strategies and maximize returns through precise execution of trades based on pre-defined grid levels.

## Features

- **Automated Trading**: Executes buy and sell orders automatically based on grid levels.
- **Configurable Parameters**: Easily adjustable parameters to suit different trading strategies.
- **Real-time Notifications**: Integration with Telegram to receive live updates on trading activities.
- **High Performance**: Optimized for low latency and high-frequency trading.

## Project Structure

- **lib/**: Contains the core logic and helper functions for the trading bot.
- **.env.copy**: Template for environment variables configuration.
- **app.ts**: Main application file to start the bot.
- **package.json**: Project metadata and dependencies.
- **tsconfig.json**: TypeScript configuration file.

## Setup Instructions

### Prerequisites

- Node.js
- Backpack Exchange API key and secret
- Sufficient funds for trading pairs
- Optional: Telegram bot for notifications

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/backpack455/trading-bot.git
    cd trading-bot
    ```

2. Install dependencies:
    ```sh
    npm install
    npm install -g pm2 typescript
    ```

3. Configure the environment variables:
    ```sh
    cp .env.copy .env
    # Edit the .env file with your API credentials and other configurations
    ```

### Environment Variables

Configure the `.env` file with the following variables:
- `BACKPACK_API_KEY`: Your Backpack Exchange API key
- `BACKPACK_API_SECRET`: Your Backpack Exchange API secret
- `SYMBOL`: The trading pair (e.g., `SOL_USDC`)
- `LOWER_PRICE`: The bottom price of the grid (e.g., `170`)
- `UPPER_PRICE`: The top price of the grid (e.g., `200`)
- `PRICE_DECIMAL`: Decimal places for price precision
- `NUMBER_OF_GRIDS`: Number of grids (e.g., `100`)
- `QUANTITY_PER_GRID`: Quantity per grid (e.g., `0.07`)
- `TELEGRAM_BOT_API_TOKEN`: Telegram bot token (optional)
- `TELEGRAM_TARGET_CHAT_ID`: Telegram chat ID (optional)

### Running the Bot

To start the trading bot, run:
```sh
yarn start
