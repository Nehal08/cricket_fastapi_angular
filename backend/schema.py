from typing import Optional
from pydantic import BaseModel

class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True


class TeamBase(OurBaseModel):
    name: str

class PlayerBase(OurBaseModel):
    team_id: int
    name: str
    age: int
    role: str
    runs: int

class MatchBase(OurBaseModel):
    venue: str
    team_1_id:int
    team_2_id:int

class InningBase(OurBaseModel):
    id: int
    inning_id: str
    team_playing: int
    m_id: int
    score: Optional[str] = None


class OverBase(OurBaseModel):
    over_id: int
    m_id: int
    in_id: int
    # on_strike: Optional[str] = None
    this_over: Optional[str] = None
    summary: Optional[str] = None



class TeamRead(TeamBase): # for get calls
    team_id: int

class PlayerRead(PlayerBase): # for get calls
    player_id:int


class TeamAdd(TeamRead):
    team_players: list[PlayerRead] = []


class PlayerAdd(PlayerRead):
    team: TeamBase

class MatchRead(MatchBase):
    match_id: int
    venue: str
    toss_won: Optional[str] = None
    first_batting_team: Optional[str] = None
    result: Optional[str] = None
    mvp: Optional[str] = None

    team_1_id: int
    team_2_id: int

    team_1:  TeamRead
    team_2: TeamRead

# class MovieBase(BaseModel):
#     movie_name: str
#     director: str
#     geners: str
#     cast: str


# class MovieAdd(MovieBase):
#     movie_id: str
#     # Optional[str] is just a shorthand or alias for Union[str, None].
#     # It exists mostly as a convenience to help function signatures look a little cleaner.
#     streaming_platform: Optional[str] = None
#     membership_required: bool

#     # Behaviour of pydantic can be controlled via the Config class on a model
#     # to support models that map to ORM objects. Config property orm_mode must be set to True
#     class Config:
#         orm_mode = True


# class Movie(MovieAdd):
#     id: int

#     # Behaviour of pydantic can be controlled via the Config class on a model
#     # to support models that map to ORM objects. Config property orm_mode must be set to True
#     class Config:
#         orm_mode = True


# class UpdateMovie(BaseModel):
#     # Optional[str] is just a shorthand or alias for Union[str, None].
#     # It exists mostly as a convenience to help function signatures look a little cleaner.
#     streaming_platform: Optional[str] = None
#     membership_required: bool

#     # Behaviour of pydantic can be controlled via the Config class on a model
#     # to support models that map to ORM objects. Config property orm_mode must be set to True
#     class Config:
#         orm_mode = True