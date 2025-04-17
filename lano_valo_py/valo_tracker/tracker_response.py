from typing import Any, List, Optional, Union

from pydantic import BaseModel, Field


class SegmentStatMetadata(BaseModel):
    tierName: Optional[str] = None


class SegmentStat(BaseModel):
    rank: Optional[Any] = None
    percentile: Optional[Any] = None
    displayName: str
    displayCategory: str
    category: str
    description: Optional[Any] = None
    metadata: SegmentStatMetadata
    value: Union[int, str]
    displayValue: str
    displayType: str


class SegmentSeasonStats(BaseModel):
    matchesPlayed: Optional[SegmentStat] = None
    matchesWon: Optional[SegmentStat] = None
    matchesLost: Optional[SegmentStat] = None
    matchesTied: Optional[SegmentStat] = None
    matchesWinPct: SegmentStat
    matchesDisconnected: Optional[SegmentStat] = None
    matchesDuration: Optional[SegmentStat] = None
    timePlayed: Optional[SegmentStat] = None
    mVPs: Optional[SegmentStat] = None
    roundsPlayed: Optional[SegmentStat] = None
    roundsWon: Optional[SegmentStat] = None
    roundsLost: Optional[SegmentStat] = None
    roundsWinPct: Optional[SegmentStat] = None
    roundsDuration: Optional[SegmentStat] = None
    score: Optional[SegmentStat] = None
    scorePerMatch: Optional[SegmentStat] = None
    scorePerRound: Optional[SegmentStat] = None
    kills: Optional[SegmentStat] = None
    killsPerRound: Optional[SegmentStat] = None
    killsPerMatch: Optional[SegmentStat] = None
    deaths: Optional[SegmentStat] = None
    deathsPerRound: Optional[SegmentStat] = None
    deathsPerMatch: Optional[SegmentStat] = None
    assists: Optional[SegmentStat] = None
    assistsPerRound: Optional[SegmentStat] = None
    assistsPerMatch: Optional[SegmentStat] = None
    kDRatio: Optional[SegmentStat] = None
    kDARatio: Optional[SegmentStat] = None
    kADRatio: Optional[SegmentStat] = None
    damage: Optional[SegmentStat] = None
    damageDelta: Optional[SegmentStat] = None
    damageDeltaPerRound: Optional[SegmentStat] = None
    damagePerRound: Optional[SegmentStat] = None
    damagePerMatch: Optional[SegmentStat] = None
    damagePerMinute: Optional[SegmentStat] = None
    damageReceived: Optional[SegmentStat] = None
    headshots: Optional[SegmentStat] = None
    headshotsPerRound: Optional[SegmentStat] = None
    headshotsPercentage: Optional[SegmentStat] = None
    grenadeCasts: Optional[SegmentStat] = None
    grenadeCastsPerRound: Optional[SegmentStat] = None
    grenadeCastsPerMatch: Optional[SegmentStat] = None
    ability1Casts: Optional[SegmentStat] = None
    ability1CastsPerRound: Optional[SegmentStat] = None
    ability1CastsPerMatch: Optional[SegmentStat] = None
    ability2Casts: Optional[SegmentStat] = None
    ability2CastsPerRound: Optional[SegmentStat] = None
    ability2CastsPerMatch: Optional[SegmentStat] = None
    ultimateCasts: Optional[SegmentStat] = None
    ultimateCastsPerRound: Optional[SegmentStat] = None
    ultimateCastsPerMatch: Optional[SegmentStat] = None
    dealtHeadshots: Optional[SegmentStat] = None
    dealtBodyshots: Optional[SegmentStat] = None
    dealtLegshots: Optional[SegmentStat] = None
    receivedHeadshots: Optional[SegmentStat] = None
    receivedBodyshots: Optional[SegmentStat] = None
    receivedLegshots: Optional[SegmentStat] = None
    econRating: Optional[SegmentStat] = None
    econRatingPerMatch: Optional[SegmentStat] = None
    econRatingPerRound: Optional[SegmentStat] = None
    suicides: Optional[SegmentStat] = None
    firstBloods: Optional[SegmentStat] = None
    firstBloodsPerRound: Optional[SegmentStat] = None
    firstBloodsPerMatch: Optional[SegmentStat] = None
    firstDeaths: Optional[SegmentStat] = None
    firstDeathsPerRound: Optional[SegmentStat] = None
    lastDeaths: Optional[SegmentStat] = None
    survived: Optional[SegmentStat] = None
    traded: Optional[SegmentStat] = None
    kAST: Optional[SegmentStat] = None
    mostKillsInMatch: Optional[SegmentStat] = None
    flawless: Optional[SegmentStat] = None
    thrifty: Optional[SegmentStat] = None
    aces: Optional[SegmentStat] = None
    teamAces: Optional[SegmentStat] = None
    clutches: Optional[SegmentStat] = None
    clutchesPercentage: Optional[SegmentStat] = None
    clutchesLost: Optional[SegmentStat] = None
    clutches1v1: Optional[SegmentStat] = None
    clutches1v2: Optional[SegmentStat] = None
    clutches1v3: Optional[SegmentStat] = None
    clutches1v4: Optional[SegmentStat] = None
    clutches1v5: Optional[SegmentStat] = None
    clutchesLost1v1: Optional[SegmentStat] = None
    clutchesLost1v2: Optional[SegmentStat] = None
    clutchesLost1v3: Optional[SegmentStat] = None
    clutchesLost1v4: Optional[SegmentStat] = None
    clutchesLost1v5: Optional[SegmentStat] = None
    kills1K: Optional[SegmentStat] = None
    kills2K: Optional[SegmentStat] = None
    kills3K: Optional[SegmentStat] = None
    kills4K: Optional[SegmentStat] = None
    kills5K: Optional[SegmentStat] = None
    kills6K: Optional[SegmentStat] = None
    esr: Optional[SegmentStat] = None
    plants: Optional[SegmentStat] = None
    plantsPerMatch: Optional[SegmentStat] = None
    plantsPerRound: Optional[SegmentStat] = None
    attackKills: Optional[SegmentStat] = None
    attackKillsPerRound: Optional[SegmentStat] = None
    attackDeaths: Optional[SegmentStat] = None
    attackKDRatio: Optional[SegmentStat] = None
    attackAssists: Optional[SegmentStat] = None
    attackAssistsPerRound: Optional[SegmentStat] = None
    attackRoundsWon: Optional[SegmentStat] = None
    attackRoundsLost: Optional[SegmentStat] = None
    attackRoundsPlayed: Optional[SegmentStat] = None
    attackRoundsWinPct: Optional[SegmentStat] = None
    attackScore: Optional[SegmentStat] = None
    attackScorePerRound: Optional[SegmentStat] = None
    attackDamage: Optional[SegmentStat] = None
    attackDamagePerRound: Optional[SegmentStat] = None
    attackHeadshots: Optional[SegmentStat] = None
    attackTraded: Optional[SegmentStat] = None
    attackSurvived: Optional[SegmentStat] = None
    attackFirstBloods: Optional[SegmentStat] = None
    attackFirstBloodsPerRound: Optional[SegmentStat] = None
    attackFirstDeaths: Optional[SegmentStat] = None
    attackFirstDeathsPerRound: Optional[SegmentStat] = None
    attackKAST: Optional[SegmentStat] = None
    defuses: Optional[SegmentStat] = None
    defusesPerMatch: Optional[SegmentStat] = None
    defusesPerRound: Optional[SegmentStat] = None
    defenseKills: Optional[SegmentStat] = None
    defenseKillsPerRound: Optional[SegmentStat] = None
    defenseDeaths: Optional[SegmentStat] = None
    defenseKDRatio: Optional[SegmentStat] = None
    defenseAssists: Optional[SegmentStat] = None
    defenseAssistsPerRound: Optional[SegmentStat] = None
    defenseRoundsWon: Optional[SegmentStat] = None
    defenseRoundsLost: Optional[SegmentStat] = None
    defenseRoundsPlayed: Optional[SegmentStat] = None
    defenseRoundsWinPct: Optional[SegmentStat] = None
    defenseScore: Optional[SegmentStat] = None
    defenseScorePerRound: Optional[SegmentStat] = None
    defenseDamage: Optional[SegmentStat] = None
    defenseDamagePerRound: Optional[SegmentStat] = None
    defenseHeadshots: Optional[SegmentStat] = None
    defenseTraded: Optional[SegmentStat] = None
    defenseSurvived: Optional[SegmentStat] = None
    defenseFirstBloods: Optional[SegmentStat] = None
    defenseFirstBloodsPerRound: Optional[SegmentStat] = None
    defenseFirstDeaths: Optional[SegmentStat] = None
    defenseFirstDeathsPerRound: Optional[SegmentStat] = None
    defenseKAST: Optional[SegmentStat] = None
    rank: Optional[SegmentStat] = None
    trnPerformanceScore: Optional[SegmentStat] = None
    peakRank: Optional[SegmentStat] = None


class SegmentAgentStats(BaseModel):
    ability1Kills: Optional[SegmentStat] = None
    ability1KillsPerMatch: Optional[SegmentStat] = None
    ability2Kills: Optional[SegmentStat] = None
    ability2KillsPerMatch: Optional[SegmentStat] = None
    grenadeKills: Optional[SegmentStat] = None
    grenadeKillsPerMatch: Optional[SegmentStat] = None
    primaryKills: Optional[SegmentStat] = None
    primaryKillsPerMatch: Optional[SegmentStat] = None
    ultimateKills: Optional[SegmentStat] = None
    ultimateKillsPerMatch: Optional[SegmentStat] = None


class SegmentAgentRoleStats(BaseModel):
    matchesPlayed: Optional[SegmentStat] = None
    matchesWon: Optional[SegmentStat] = None
    matchesLost: Optional[SegmentStat] = None
    matchesTied: Optional[SegmentStat] = None
    matchesWinPct: Optional[SegmentStat] = None
    timePlayed: Optional[SegmentStat] = None
    scorePerRound: Optional[SegmentStat] = None
    kills: Optional[SegmentStat] = None
    deaths: Optional[SegmentStat] = None
    assists: Optional[SegmentStat] = None
    kDRatio: Optional[SegmentStat] = None
    kADRatio: Optional[SegmentStat] = None
    damageDelta: Optional[SegmentStat] = None
    damageDeltaPerRound: Optional[SegmentStat] = None
    damagePerRound: Optional[SegmentStat] = None
    kAST: Optional[SegmentStat] = None


class SegmentPeakRatingStats(BaseModel):
    peakRating: Optional[SegmentStat] = None


class SegmentAttributes(BaseModel):
    playlist: Optional[str] = None
    seasonId: Optional[str] = None
    key: Optional[str] = None


class SegmentMetadata(BaseModel):
    name: Optional[str] = None
    shortName: Optional[str] = None
    playlistName: Optional[str] = None
    startTime: Optional[str] = None
    endTime: Optional[str] = None
    schemav2: Optional[str] = None


class Segment(BaseModel):
    type: Optional[str | dict] = None  # 'season' | 'agent' | 'agent-role' | 'peak-rating'
    attributes: Optional[SegmentAttributes] = None
    metadata: Optional[SegmentMetadata] = None
    stats: Optional[Union[
        SegmentSeasonStats,
        SegmentAgentStats,
        SegmentAgentRoleStats,
        SegmentPeakRatingStats,
    ]] = None
    expiryDate: Optional[str | dict] = None


class TrackerPlatformInfo(BaseModel):
    platformSlug: str
    platformUserId: str
    platformUserHandle: str
    platformUserIdentifier: str
    avatarUrl: str
    additionalParameters: Optional[Any] = None


class TrackerUserInfo(BaseModel):
    userId: Any
    isPremium: bool
    isVerified: bool
    isInfluencer: bool
    isPartner: bool
    countryCode: Optional[str] = None
    customAvatarUrl: Optional[str] = None
    customHeroUrl: Optional[str] = None
    customAvatarFrame: Any
    customAvatarFrameInfo: Any
    premiumDuration: Any
    socialAccounts: List[Any]
    pageviews: int
    xpTier: Any
    isSuspicious: Optional[bool] = None


class Season(BaseModel):
    id: str
    name: str
    shortName: str
    episodeName: str
    actName: str
    playlists: None


class Playlist(BaseModel):
    id: str
    name: str
    platform: str


class TrackerMetadata(BaseModel):
    activeShard: str
    schema_: str = Field(..., alias="schema")
    privacy: str
    defaultPlaylist: str
    defaultSeason: str
    premierRosterId: Optional[str] = None
    premierCrests: Optional[Any] = None
    accountLevel: int
    seasons: List[Season]
    playlists: List[Playlist]


class Error(BaseModel):
    message: str


class TrackerData(BaseModel):
    platformInfo: TrackerPlatformInfo
    userInfo: TrackerUserInfo
    metadata: TrackerMetadata
    segments: List[Segment]
    availableSegments: List[Any]
    expiryDate: str


class TrackerResponse(BaseModel):
    data: TrackerData
    errors: Optional[List[Error]] = None


# Internal types


class TrackerUserData(BaseModel):
    platform: str
    uuid: str
    name: str
    userid: str
    avatar: str
    pageViews: int
    rank: str
    peakRank: str
