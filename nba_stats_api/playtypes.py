import requests
from nba_stats_api.constants import PlayTypeBase


class PlayTypeHandler:
    def __init__(self, year="2016", season_type="Reg"):
        self.year = year
        self.season_type = season_type
        self.base_url = PlayTypeBase
        self.json = None

    def _convert_json(self, nba_json):
        new_json = {}

        for row in nba_json:
            # print(("Row: ", row))
            player_name = row['PlayerFirstName'] + " " + row['PlayerLastName']
            new_row = {'PLAYER_ID': row['PlayerIDSID'],
                       'PLAYER_NAME': player_name,
                       'TEAM_ID': row['TeamIDSID'],
                       'TEAM_ABBREVIATION': row['TeamNameAbbreviation']}
            # TODO: Figure out wtf half of these are
            for key in ['GP', 'Poss', 'Time', 'PPP', 'Points', 'FGM', 'FGA',
                        'WorsePPP', 'BetterPPP', 'PossG', 'PPG', 'FGAG',
                        'FGMG', 'FGmG', 'FGm', 'FG', 'aFG', 'FT', 'TO',
                        'SF', 'PlusOne', 'Score']:
                new_row[key] = row[key]
            new_json[new_row['PLAYER_ID']] = new_row

        return new_json

    def fetch_json(self, play_type):
        full_url = self.base_url.format(year=self.year,
                                        category=play_type,
                                        season_type=self.season_type)
        response = requests.get(full_url)
        self.json = self._convert_json(response.json()['results'])
