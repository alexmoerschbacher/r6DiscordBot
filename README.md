# R6Bot

R6Bot is a Discord bot designed to provide Rainbow Six Siege player statistics and squad management features. The bot fetches player stats from various APIs and displays them in Discord channels.

## Features

- **Rank Us**: Displays squad members ranked by their K/D ratio
- **MMR**: Displays squad members ranked by their MMR
- **Kill Chart**: Generates a chart displaying the kills of squad members
- **Add User**: Adds a user to your squad
- **Remove User**: Removes a user from your squad

## Commands

- `/r6bot rankUs`: Returns ranks in order of K/D
- `/r6bot mmr`: Returns ranks in order of MMR
- `/r6bot kill chart`: Returns a chart displaying all kills
- `/r6bot add user <username>`: Adds a user to your squad (use their Uplay name)
- `/r6bot remove user <username>`: Removes a user from your squad
- `/r6bot help`: Displays Avaliable commands information

## Installation

1. Clone the repository

`
git clone https://github.com/yourusername/r6Bot.git
cd r6Bot
`

2. Create a virtual environment and activate it:
`
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
`

3. Install the required dependencies:
`
pip install -r requirements.txt
`
4. Create a .env file in the root directory and add your environment variables:
`
TOKEN=your_discord_bot_token
AUTHORIZATION=Ubisoft Base64EncodedUsername:Password
DBSCHEMA=your_database_schema
DBUSERNAME=your_database_username
DBPASSWORD=your_database_password
DBPORT=your_database_port
`
## Usage

Run the bot:
`
python r6_bot.py
`

## Project Structure

### Auth
- **auth.py**: Handles authentication with the Ubisoft API

### Services
- **botService.py**: Main service for handling bot commands
- **chartService.py**: Service for generating charts

### Mappers
- **r6ProfileDataMapper.py**: Maps R6 profile data to PlayerStats
- **tabStatsProfileDataMapper.py**: Maps TabStats profile data to PlayerStats

### Models
- **playerStats.py**: Model for player statistics

### Database
- **tables.py**: Defines database tables using Peewee ORM

### Repository
- **repository.py**: Handles CRUD operations for users and squads

### Service Clients
- **r6ServiceClient.py**: Client for interacting with the R6 API
- **tabStatsServiceClient.py**: Client for interacting with the TabStats API

### Main Files
- **r6_bot.py**: Main entry point for the Discord bot
- **r6Service.py**: Service for fetching current season stats
- **requirements.txt**: Lists the Python dependencies
- **.gitignore**: Specifies files and directories to be ignored by Git

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.