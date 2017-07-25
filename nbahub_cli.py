import click
import json
from nba_stats_api.utils import update_all_player_stats, DecimalEncoder


@click.group()
def cli():
    pass


@cli.command()
@click.option("--season", default="2016-17")
def update_all(season):
    print(f"Updating all player statistics for {season}")
    # PLAYER_ID - > {'PerGame': {<stats here>}, 'Totals': <stats>, etc}
    player_stats_dict = update_all_player_stats(season)

    for player in player_stats_dict:
        this_player_stats = player_stats_dict[player]
        player_name = this_player_stats['BasicInfo']['PLAYER_NAME']
        if "Shooting" in this_player_stats:
            with open(f"outputs/{player_name}_output.json", "w") as stat_file:
                stat_file.write(json.dumps(player_stats_dict[player],
                                           cls=DecimalEncoder))
                stat_file.close()


if __name__ == "__main__":
    cli()
