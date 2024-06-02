from enum import Enum

from pydantic import BaseModel
from typing import Optional, Union, List, Dict, Any


class RewardByDays(BaseModel):
    days: int
    rewardCoins: int


class Task(BaseModel):
    id: Union[str, int]
    isCompleted: Optional[bool] = None
    link: Optional[str] = None
    periodicity: Optional[str] = None
    rewardCoins: Optional[int] = None
    rewardsByDays: Optional[List[RewardByDays]] = None
    days: Optional[int] = None


class TaskList(BaseModel):
    tasks: List[Task]


class Upgrade(BaseModel):
    id: str
    level: int
    lastUpgradeAt: int
    snapshotReferralsCount: Optional[int] = None


class Friend(BaseModel):
    isBot: bool
    firstName: str
    lastName: Optional[str] = None
    addedToAttachmentMenu: Optional[Any] = None
    id: int
    isPremium: Optional[Any] = None
    canReadAllGroupMessages: Optional[Any] = None
    languageCode: str
    canJoinGroups: Optional[Any] = None
    supportsInlineQueries: Optional[Any] = None
    photos: List = []
    username: str
    welcomeBonusCoins: int


class Referral(BaseModel):
    friend: Friend


class ClickerUser(BaseModel):
    id: str
    totalCoins: float
    balanceCoins: float
    level: int
    availableTaps: int
    lastSyncUpdate: int
    exchangeId: str
    boosts: Dict = {}
    upgrades: Dict[str, Upgrade]
    tasks: Dict = {}
    airdropTasks: Dict = {}
    referralsCount: int
    maxTaps: int
    earnPerTap: int
    earnPassivePerSec: float
    earnPassivePerHour: int
    lastPassiveEarn: float
    tapsRecoverPerSec: int
    referral: Referral


class ClickerUserWrapper(BaseModel):
    clickerUser: ClickerUser


class TelegramUser(BaseModel):
    id: int
    isBot: bool
    firstName: str
    lastName: Optional[str] = None
    languageCode: str


class ResponseGetMe(BaseModel):
    telegramUser: TelegramUser
    status: str


class BoostId(str, Enum):
    BoostEarnPerTap = "BoostEarnPerTap"
    BoostMaxTaps = "BoostMaxTaps"
    BoostFullAvailableTaps = "BoostFullAvailableTaps"


class Boost(BaseModel):
    id: BoostId
    price: int
    earnPerTap: int
    maxTaps: Optional[int] = 0
    cooldownSeconds: Optional[int] = 0
    level: int
    maxTapsDelta: int
    earnPerTapDelta: int
    maxLevel: Optional[int] = None


class BoostsForBuy(BaseModel):
    boostsForBuy: List[Boost]


class ResponseModelBuyBoost(BaseModel):
    clickerUser: ClickerUser
    boostsForBuy: List[Boost]


class ErrorResponse(BaseModel):
    error_code: str
    error_message: str
