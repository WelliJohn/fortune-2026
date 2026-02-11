from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import FortuneRequest, FortuneResponse
from service import FortuneService

app = FastAPI(title="2026 开年运势签 API", version="1.0.0")

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境应该配置具体域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """根路径"""
    return {"message": "2026 开年运势签 API", "version": "1.0.0"}


@app.post("/api/fortune", response_model=FortuneResponse)
async def get_fortune(request: FortuneRequest):
    """
    获取运势

    参数:
    - nickname: 昵称（必填）
    - birth_year: 出生年份（选填）
    - focus: 关注方向列表（选填）

    返回:
    - keyword: 年度关键词
    - scores: 运势指数
    - analysis: 运势解析
    - suggestions: 行动建议
    - lucky: 幸运信息
    """
    try:
        result = FortuneService.get_fortune(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"生成运势失败: {str(e)}")


@app.get("/health")
async def health_check():
    """健康检查"""
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
