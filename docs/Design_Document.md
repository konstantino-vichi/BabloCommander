
# Design Document

## Project Overview

Project Name: BabloCommander

Objective: Build functionality within a Telegram bot to collect, categorize, and store spending details on a daily basis from chat messages between two users (me and Dmitry).

## User Stories

1. As a user, I want to send a chat message with my spending details to the bot.
2. As a user, I want the bot to categorize my spending based on the details I provided.
3. As a user, I want the bot to store my spending details in the database each day.
4. As a user, I want the bot to handle and notify me of any errors or unsuccessful attempts at storing my spending information.
5. As a user, I want the bot to confirm when it has successfully stored my spending information.

## Bot Commands

List of commands the bot should handle:

1. A new command that allows a user to input their spending details.

## Proposed Workflow

1. The user sends a message with their spending details. Syntax could be e.g. `SPEND CATEGORY AMOUNT DESCRIPTION`.
2. Bot parses the message.
3. Bot categorizes the spending based on the CATEGORY provided by the user.
4. Bot stores the categorized data in a database.
5. Bot sends a confirmation message to the user once data is successfully stored.
6. If any errors occur, the bot sends a message to the user detailing the error.

## Database

Database schema and kind of database will be determined once provided by the user.

## Bot Setup

Details about the existing bot setup and how the bot will run are yet to be provided. The bot could either run continuously in the background or run at specified intervals (e.g. once a day at a specific time).

## Potential Enhancement for Future Development

1. Command for querying the database: A command could be added that allows the user to ask the bot for specific data from the database. For example, a command that returns total spending in a certain category or a specific time period.

## Updated Workflow and Spending Data Accumulation

1. User inputs spending details into the chat.
2. The bot attempts to interpret the category, amount, and description from the text.
3. If the bot cannot clearly understand these details, it prompts the user to make clarifications.
4. This back-and-forth continues until the bot has the required amount of detailed spending data.
5. The bot then presents the user with a summary of the processed spending data for confirmation.
6. After the user confirms the accuracy of the data, the bot adds the spending details to a temporary in-memory store.
