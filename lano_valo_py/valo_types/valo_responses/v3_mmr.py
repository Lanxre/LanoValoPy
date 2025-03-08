from typing import List
from pydantic import BaseModel


class AccountMmrModelV3(BaseModel):
    puuid: str
    name: str
    tag: str


class SeasonMmrModelV3(BaseModel):
    id: str
    short: str


class TierMmrModelV3(BaseModel):
    id: int
    name: str


class LeaderboardPlacement(BaseModel):
    rank: int
    updated_at: str


class CurrentMmrModelV3(BaseModel):
    tier: TierMmrModelV3
    rr: int
    last_change: str
    elo: int
    game_need_for_rating: int
    rank_protection_shields: int
    leaderboard_placement: LeaderboardPlacement


class SeasonalMmrModelV3(BaseModel):
    season: SeasonMmrModelV3
    wins: int
    games: int
    end_tier: TierMmrModelV3
    ranging_schema: int
    leaderboard_placement: LeaderboardPlacement
    act_wins: List[TierMmrModelV3]


class PeakMmrModelV3(BaseModel):
    season: SeasonMmrModelV3
    rr: int
    ranking_schema: int
    tier: TierMmrModelV3

class MmrModelV3(BaseModel):
    account: AccountMmrModelV3
    peak: PeakMmrModelV3
    current: CurrentMmrModelV3
    seasonal: List[SeasonalMmrModelV3]