import time

import click
from nba_py.constants import PerMode
from nba_py.league import PlayerStats
from nba_py.player import PlayerList

from nba_stats_api.playtypes import PlayTypeHandler
from nba_stats_api.utils import (get_shooting_stats,
                                 convert_dict,
                                 calc_extra_shooting_stats)
from nba_stats_api.constants import ALL_PLAY_TYPES


@click.group()
def cli():
    pass


@cli.command()
def update_all():
    print("In update all...")
    # PLAYER_ID - > {'PerGame': {<stats here>}, 'Totals': <stats>, etc}
    player_stats_dict = {}
    for per_mode in [PerMode.Totals, PerMode.PerGame,
                     PerMode.Per100Possessions, PerMode.Per36]:
        print(f"Working on {per_mode}")
        player_stats = PlayerStats(season="2016-17",
                                   per_mode=per_mode)
        time.sleep(1)
        for row in player_stats.overall():
            new_row = convert_dict(row)

            player_id = row['PLAYER_ID']
            if player_id not in player_stats_dict:
                player_stats_dict[player_id] = {}

            player_stats_dict[player_id][per_mode] = new_row

    play_type_handler = PlayTypeHandler(year="2016",
                                        season_type="Reg")
    for play_type in ALL_PLAY_TYPES:
        print(f"Working on {play_type}")
        play_type_handler.fetch_json(play_type)

        for player_id in play_type_handler.json:
            player_name = play_type_handler.json[player_id]['PLAYER_NAME']
            if player_id not in player_stats_dict:
                print(f"{player_name} has entries for PlayType Statistics, but not"
                      f"traditional stats. Skipping this player.")
                continue
            player_stats_dict[player_id][play_type] = play_type_handler.json[player_id]

        time.sleep(1)

    player_list = PlayerList(season="2016-17",
                             only_current=1)
    for player in player_list.info()[:5]:
        player_id = player['PERSON_ID']
        print(f"Working on shooting for {player_id}")
        shooting = get_shooting_stats(player_id=player_id,
                                      season="2016-17")
        player_stats_dict[player_id]['Shooting'] = convert_dict(shooting)
        calc_extra_shooting_stats(player_stats_dict[player_id])
        time.sleep(2.5)

    for player in player_stats_dict:
        this_player_stats = player_stats_dict[player]
        player_name = this_player_stats['Totals']['PLAYER_NAME']
        if "Shooting" in this_player_stats:
            with open(f"outputs/{player_name}_output.json", "w") as stat_file:
                stat_file.write(str(player_stats_dict[player]).replace("'", '"') + "\n")
                stat_file.close()


if __name__ == "__main__":
    cli()
