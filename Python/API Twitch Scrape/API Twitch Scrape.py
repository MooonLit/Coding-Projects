import requests
import pandas as pd
import datetime
import logging
import time

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

CLIENT_ID = 'my_client_id'  # I would replace this with my Twitch Client ID
CLIENT_SECRET = 'my_client_secret'  # I would replace this with my Twitch Client Secret
BASE_URL = 'https://api.twitch.tv/helix'

# Function to get OAuth token from Twitch
def get_twitch_token(client_id, client_secret):
    url = f'{BASE_URL}/oauth2/token'
    params = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }
    try:
        response = requests.post(url, params=params)
        response.raise_for_status()
        return response.json()['access_token']
    except requests.exceptions.HTTPError as err:
        logging.error(f"HTTP error occurred: {err}")
    except Exception as err:
        logging.error(f"An error occurred: {err}")

# Function to handle Twitch API pagination
def paginate_through_results(url, headers, params={}):
    all_data = []
    while url:
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            all_data.extend(data['data'])
            url = data['pagination'].get('cursor')
            time.sleep(1)  # Respect Twitch's rate limit
        except requests.exceptions.HTTPError as err:
            logging.error(f"HTTP error occurred: {err}")
            break
        except Exception as err:
            logging.error(f"An error occurred: {err}")
            break
    return all_data

# Function to get game viewer statistics
def get_game_viewer_stats(access_token):
    url = f'{BASE_URL}/games/top'
    headers = {
        'Client-ID': CLIENT_ID,
        'Authorization': f'Bearer {access_token}'
    }
    games_data = paginate_through_results(url, headers)

    games_list = [{
        'game_id': game['id'],
        'game_name': game['name'],
        # Assuming the API provides viewer count
        'viewers': game.get('viewers', 'Not available')
    } for game in games_data]

    return pd.DataFrame(games_list)

# Main process
try:
    token = get_twitch_token(CLIENT_ID, CLIENT_SECRET)
    if token:
        game_stats = get_game_viewer_stats(token)

        # Output to CSV
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        output_file = f'twitch_game_stats_{current_date}.csv'
        game_stats.to_csv(output_file, index=False)
        logging.info(f"Data successfully written to {output_file}")
    else:
        logging.error("Failed to retrieve access token")
except Exception as e:
    logging.error(f"An unexpected error occurred: {e}")
