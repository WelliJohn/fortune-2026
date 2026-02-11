from pydantic import BaseModel, Field
from typing import List, Optional


class FortuneRequest(BaseModel):
    """抽签请求模型"""
    nickname: str = Field(..., min_length=1, max_length=20, description="用户昵称")
    birth_year: Optional[int] = Field(None, ge=1950, le=2020, description="出生年份")
    focus: List[str] = Field(default=[], description="关注方向")


class LuckyInfo(BaseModel):
    """幸运信息"""
    month: str
    color: str
    number: int


class ScoresInfo(BaseModel):
    """运势指数"""
    overall: int
    career: int
    wealth: int
    love: int
    health: int


class FortuneResponse(BaseModel):
    """抽签响应模型"""
    keyword: str
    scores: ScoresInfo
    analysis: str
    suggestions: List[str]
    lucky: LuckyInfo
