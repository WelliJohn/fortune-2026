import random
import hashlib
from typing import Dict, List
from models import FortuneRequest, FortuneResponse, ScoresInfo, LuckyInfo


class FortuneService:
    """运势服务"""

    # 内存缓存
    _cache: Dict[str, FortuneResponse] = {}

    # 年度关键词池（50+个）
    KEYWORDS = [
        "破圈", "逆袭", "稳中爆发", "闷声发财", "翻盘", "跃迁",
        "爆改", "进阶", "人脉暴涨", "暗线升级", "厚积薄发", "静水流深",
        "暗线推进", "黑马潜伏", "势能爆发", "价值重估", "认知跃升",
        "破局", "蜕变", "进化", "升维", "复利", "爆款", "出圈",
        "高光", "封神", "王炸", "起飞", "开挂", "逆风翻盘", "破茧",
        "焕新", "突围", "上岸", "收获", "丰收", "盛放", "绽放",
        "开悟", "顿悟", "觉醒", "破晓", "曙光", "金榜", "加冕",
        "登顶", "破纪录", "里程碑", "质变", "飞跃", "巅峰", "高峰",
        "黄金", "钻石", "传奇"
    ]

    # 幸运月份
    MONTHS = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]

    # 幸运颜色
    COLORS = ["暗红", "酒红", "墨绿", "深蓝", "金色", "琥珀", "烟灰", "米白", "珊瑚橙", "香槟金", "宝石蓝", "橄榄绿"]

    # 运势解析模板
    ANALYSIS_TEMPLATES = [
        "2026年对你来说是一个充满机遇的年份。{keyword}将成为你今年的主旋律，特别是在{focus}方面会有突出表现。上半年适合积蓄力量，打磨技能，下半年则是收获期。建议保持开放心态，多尝试新领域，你会发现意外之喜。记住，每一个小进步都在为未来铺路，保持耐心和专注，好运自然而来。",

        "今年的你将迎来{keyword}的一年。{focus}领域会是你的重点突破口，整体运势呈上升趋势。前半年可能会遇到一些挑战，但这些都是成长的垫脚石。建议在关键时刻果断出手，不要犹豫。同时注意平衡工作与生活，适当的休息会让你更有战斗力。相信自己的判断，大胆前行，惊喜就在不远处。",

        "{keyword}是你2026年的关键词。今年在{focus}上会有显著提升，整体发展稳健向好。春季适合规划布局，夏秋是执行期，冬季则会看到成果。建议多与优秀的人交流，拓展视野和人脉圈。遇到困难时保持冷静，很多问题其实是成长的信号。把握住关键节点，你会发现这一年比想象中更精彩。",

        "2026年你将经历{keyword}的过程。{focus}方面的投入会带来超预期回报，整体趋势向上。上半年适合学习充电，下半年适合实战应用。建议设定清晰目标，分阶段推进，不急于求成。保持好奇心，对新事物保持敏感，机会往往藏在细节中。相信积累的力量，每一天的努力都在为蜕变做准备。",

        "今年{keyword}将是你的年度主题。在{focus}领域会有明显进展，整体运势平稳上扬。前期适合观察和准备，中期适合发力，后期则是巩固提升期。建议保持学习状态，不断更新认知，同时注重执行力。遇到好的机会要敢于抓住，但也要理性评估。稳扎稳打，循序渐进，你会收获满意的答案。"
    ]

    # 行动建议池
    SUGGESTIONS_POOL = [
        "上半年多布局，下半年主动争取机会",
        "提升一个核心技能，建立竞争优势",
        "扩大有效社交圈，链接优质资源",
        "定期复盘总结，及时调整策略",
        "保持学习习惯，每月读2-3本书",
        "锻炼身体，保持充沛精力",
        "培养一个新爱好，拓展生活维度",
        "建立个人品牌，提升影响力",
        "学会拒绝无效社交，专注重要事项",
        "制定月度计划，追踪执行进度",
        "投资自己，参加优质培训或课程",
        "整理人脉资源，定期维护关系",
        "关注行业趋势，保持敏锐嗅觉",
        "优化时间管理，提高工作效率",
        "建立反馈机制，持续改进提升",
        "拓展收入渠道，增强财务安全感",
        "保持好奇心，多尝试新领域",
        "记录重要时刻，积累个人资产",
        "培养早起习惯，掌控一天节奏",
        "定期断舍离，保持空间整洁"
    ]

    @classmethod
    def _get_seed(cls, nickname: str) -> int:
        """根据昵称生成稳定的随机种子"""
        hash_obj = hashlib.md5(nickname.encode('utf-8'))
        return int(hash_obj.hexdigest(), 16) % (10 ** 8)

    @classmethod
    def _generate_scores(cls, rng: random.Random) -> ScoresInfo:
        """生成运势指数（60-95分）"""
        return ScoresInfo(
            overall=rng.randint(60, 95),
            career=rng.randint(60, 95),
            wealth=rng.randint(60, 95),
            love=rng.randint(60, 95),
            health=rng.randint(60, 95)
        )

    @classmethod
    def _generate_analysis(cls, keyword: str, focus: List[str], rng: random.Random) -> str:
        """生成运势解析"""
        template = rng.choice(cls.ANALYSIS_TEMPLATES)
        focus_text = "、".join(focus) if focus else "各个方面"
        return template.format(keyword=keyword, focus=focus_text)

    @classmethod
    def _generate_suggestions(cls, rng: random.Random) -> List[str]:
        """生成行动建议（3条）"""
        return rng.sample(cls.SUGGESTIONS_POOL, 3)

    @classmethod
    def _generate_lucky(cls, rng: random.Random) -> LuckyInfo:
        """生成幸运彩蛋"""
        return LuckyInfo(
            month=rng.choice(cls.MONTHS),
            color=rng.choice(cls.COLORS),
            number=rng.randint(1, 9)
        )

    @classmethod
    def get_fortune(cls, request: FortuneRequest) -> FortuneResponse:
        """获取运势结果"""
        # 检查缓存
        if request.nickname in cls._cache:
            return cls._cache[request.nickname]

        # 使用昵称生成固定种子
        seed = cls._get_seed(request.nickname)
        rng = random.Random(seed)

        # 生成结果
        keyword = rng.choice(cls.KEYWORDS)
        scores = cls._generate_scores(rng)
        analysis = cls._generate_analysis(keyword, request.focus, rng)
        suggestions = cls._generate_suggestions(rng)
        lucky = cls._generate_lucky(rng)

        # 构建响应
        response = FortuneResponse(
            keyword=keyword,
            scores=scores,
            analysis=analysis,
            suggestions=suggestions,
            lucky=lucky
        )

        # 缓存结果
        cls._cache[request.nickname] = response

        return response
