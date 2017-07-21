

# Note that {year} refers to the pre-New Year's portion of the season in question.
# For example, if you want 2016-17 stats, year = 2016.
PlayTypeBase = ("http://stats-prod.nba.com/wp-json/statscms/v1/synergy/player/?"
        "category={category}&limit=500&names=offensive&q=2501056&season={year}&"
        "seasonType={season_type}")

Transition = "Transition"
Isolation = "Isolation"
PnRBallHandler = "PRBallHandler"
PnRRollMan = "PRRollman"
PostUp = "Postup"
SpotUp = "Spotup"
HandOff = "Handoff"
Cut = "Cut"
OffScreen = "OffScreen"
PutBacks = "OffRebound"
Misc = "Misc"

ALL_PLAY_TYPES = [Transition, Isolation, PnRBallHandler, PnRRollMan,
                  PostUp, SpotUp, HandOff, Cut, OffScreen, PutBacks, Misc]
