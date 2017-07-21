from decimal import Decimal
from nba_py.player import PlayerShootingSplits


class Player:
    def __init__(self, nba_id, name):
        self.nba_id = nba_id
        self.name = name


def get_shooting_stats(player_id, season):
    shooting_splits = PlayerShootingSplits(season=season,
                                           player_id=player_id)
    return shooting_splits.shot_5ft()[0]


def convert_dict(to_convert):
    return {key: to_convert[key] for key in to_convert if "rank" not in key.lower()}


def calc_true_shooting(player_stats_dict):
    totals = player_stats_dict['Totals']
    true_shooting_attempts = totals['FGA'] + (0.44 * totals['FTA'])
    true_shooting_percentage = Decimal(totals['PTS'] / (2 * true_shooting_attempts))
    return true_shooting_percentage


def calc_three_point_attempt_rate(player_stats_dict):
    totals = player_stats_dict['Totals']
    return Decimal(totals['FG3A'] / totals['FGA'])


def calc_free_throw_attempt_rate(player_stats_dict):
    totals = player_stats_dict['Totals']
    return Decimal(totals['FTA'] / totals['FGA'])


def calc_two_pt_percentage(player_stats_dict):
    totals = player_stats_dict['Totals']
    two_pt_makes = totals['FGM'] - totals['FG3M']
    two_pt_attempts = totals['FGA'] - totals['FG3A']
    return Decimal(two_pt_makes / two_pt_attempts)


def calc_extra_shooting_stats(player_stats_dict):
    player_stats_dict['Shooting']['TS_PCT'] = calc_true_shooting(player_stats_dict)
    player_stats_dict['Shooting']['3PAr'] = calc_three_point_attempt_rate(player_stats_dict)
    player_stats_dict['Shooting']['FTr'] = calc_free_throw_attempt_rate(player_stats_dict)
    player_stats_dict['Shooting']['2PT_PCT'] = calc_two_pt_percentage(player_stats_dict)
