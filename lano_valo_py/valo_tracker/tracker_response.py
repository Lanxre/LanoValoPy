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
    matchesPlayed: SegmentStat
    matchesWon: SegmentStat
    matchesLost: SegmentStat
    matchesTied: SegmentStat
    matchesWinPct: SegmentStat
    matchesDisconnected: SegmentStat
    matchesDuration: SegmentStat
    timePlayed: SegmentStat
    mVPs: SegmentStat
    roundsPlayed: SegmentStat
    roundsWon: SegmentStat
    roundsLost: SegmentStat
    roundsWinPct: SegmentStat
    roundsDuration: SegmentStat
    score: SegmentStat
    scorePerMatch: SegmentStat
    scorePerRound: SegmentStat
    kills: SegmentStat
    killsPerRound: SegmentStat
    killsPerMatch: SegmentStat
    deaths: SegmentStat
    deathsPerRound: SegmentStat
    deathsPerMatch: SegmentStat
    assists: SegmentStat
    assistsPerRound: SegmentStat
    assistsPerMatch: SegmentStat
    kDRatio: SegmentStat
    kDARatio: SegmentStat
    kADRatio: SegmentStat
    damage: SegmentStat
    damageDelta: SegmentStat
    damageDeltaPerRound: SegmentStat
    damagePerRound: SegmentStat
    damagePerMatch: SegmentStat
    damagePerMinute: SegmentStat
    damageReceived: SegmentStat
    headshots: SegmentStat
    headshotsPerRound: SegmentStat
    headshotsPercentage: SegmentStat
    grenadeCasts: SegmentStat
    grenadeCastsPerRound: SegmentStat
    grenadeCastsPerMatch: SegmentStat
    ability1Casts: SegmentStat
    ability1CastsPerRound: SegmentStat
    ability1CastsPerMatch: SegmentStat
    ability2Casts: SegmentStat
    ability2CastsPerRound: SegmentStat
    ability2CastsPerMatch: SegmentStat
    ultimateCasts: SegmentStat
    ultimateCastsPerRound: SegmentStat
    ultimateCastsPerMatch: SegmentStat
    dealtHeadshots: SegmentStat
    dealtBodyshots: SegmentStat
    dealtLegshots: SegmentStat
    receivedHeadshots: SegmentStat
    receivedBodyshots: SegmentStat
    receivedLegshots: SegmentStat
    econRating: SegmentStat
    econRatingPerMatch: SegmentStat
    econRatingPerRound: SegmentStat
    suicides: SegmentStat
    firstBloods: SegmentStat
    firstBloodsPerRound: SegmentStat
    firstBloodsPerMatch: SegmentStat
    firstDeaths: SegmentStat
    firstDeathsPerRound: SegmentStat
    lastDeaths: SegmentStat
    survived: SegmentStat
    traded: SegmentStat
    kAST: SegmentStat
    mostKillsInMatch: SegmentStat
    flawless: SegmentStat
    thrifty: SegmentStat
    aces: SegmentStat
    teamAces: SegmentStat
    clutches: SegmentStat
    clutchesPercentage: SegmentStat
    clutchesLost: SegmentStat
    clutches1v1: SegmentStat
    clutches1v2: SegmentStat
    clutches1v3: SegmentStat
    clutches1v4: SegmentStat
    clutches1v5: SegmentStat
    clutchesLost1v1: SegmentStat
    clutchesLost1v2: SegmentStat
    clutchesLost1v3: SegmentStat
    clutchesLost1v4: SegmentStat
    clutchesLost1v5: SegmentStat
    kills1K: SegmentStat
    kills2K: SegmentStat
    kills3K: SegmentStat
    kills4K: SegmentStat
    kills5K: SegmentStat
    kills6K: SegmentStat
    esr: SegmentStat
    plants: SegmentStat
    plantsPerMatch: SegmentStat
    plantsPerRound: SegmentStat
    attackKills: SegmentStat
    attackKillsPerRound: SegmentStat
    attackDeaths: SegmentStat
    attackKDRatio: SegmentStat
    attackAssists: SegmentStat
    attackAssistsPerRound: SegmentStat
    attackRoundsWon: SegmentStat
    attackRoundsLost: SegmentStat
    attackRoundsPlayed: SegmentStat
    attackRoundsWinPct: SegmentStat
    attackScore: SegmentStat
    attackScorePerRound: SegmentStat
    attackDamage: SegmentStat
    attackDamagePerRound: SegmentStat
    attackHeadshots: SegmentStat
    attackTraded: SegmentStat
    attackSurvived: SegmentStat
    attackFirstBloods: SegmentStat
    attackFirstBloodsPerRound: SegmentStat
    attackFirstDeaths: SegmentStat
    attackFirstDeathsPerRound: SegmentStat
    attackKAST: SegmentStat
    defuses: SegmentStat
    defusesPerMatch: SegmentStat
    defusesPerRound: SegmentStat
    defenseKills: SegmentStat
    defenseKillsPerRound: SegmentStat
    defenseDeaths: SegmentStat
    defenseKDRatio: SegmentStat
    defenseAssists: SegmentStat
    defenseAssistsPerRound: SegmentStat
    defenseRoundsWon: SegmentStat
    defenseRoundsLost: SegmentStat
    defenseRoundsPlayed: SegmentStat
    defenseRoundsWinPct: SegmentStat
    defenseScore: SegmentStat
    defenseScorePerRound: SegmentStat
    defenseDamage: SegmentStat
    defenseDamagePerRound: SegmentStat
    defenseHeadshots: SegmentStat
    defenseTraded: SegmentStat
    defenseSurvived: SegmentStat
    defenseFirstBloods: SegmentStat
    defenseFirstBloodsPerRound: SegmentStat
    defenseFirstDeaths: SegmentStat
    defenseFirstDeathsPerRound: SegmentStat
    defenseKAST: SegmentStat
    rank: SegmentStat
    trnPerformanceScore: SegmentStat
    peakRank: SegmentStat


class SegmentAgentStats(BaseModel):
    ability1Kills: SegmentStat
    ability1KillsPerMatch: SegmentStat
    ability2Kills: SegmentStat
    ability2KillsPerMatch: SegmentStat
    grenadeKills: SegmentStat
    grenadeKillsPerMatch: SegmentStat
    primaryKills: SegmentStat
    primaryKillsPerMatch: SegmentStat
    ultimateKills: SegmentStat
    ultimateKillsPerMatch: SegmentStat


class SegmentAgentRoleStats(BaseModel):
    matchesPlayed: SegmentStat
    matchesWon: SegmentStat
    matchesLost: SegmentStat
    matchesTied: SegmentStat
    matchesWinPct: SegmentStat
    timePlayed: SegmentStat
    scorePerRound: SegmentStat
    kills: SegmentStat
    deaths: SegmentStat
    assists: SegmentStat
    kDRatio: SegmentStat
    kADRatio: SegmentStat
    damageDelta: SegmentStat
    damageDeltaPerRound: SegmentStat
    damagePerRound: SegmentStat
    kAST: SegmentStat


class SegmentPeakRatingStats(BaseModel):
    peakRating: SegmentStat


class SegmentAttributes(BaseModel):
    playlist: Optional[str] = None
    seasonId: Optional[str] = None
    key: Optional[str] = None


class SegmentMetadata(BaseModel):
    name: str
    shortName: str
    playlistName: str
    startTime: str
    endTime: str
    schemav2: str


class Segment(BaseModel):
    type: str  # 'season' | 'agent' | 'agent-role' | 'peak-rating'
    attributes: SegmentAttributes
    metadata: Optional[SegmentMetadata] = None
    stats: Union[
        SegmentSeasonStats,
        SegmentAgentStats,
        SegmentAgentRoleStats,
        SegmentPeakRatingStats,
    ]
    expiryDate: str


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

