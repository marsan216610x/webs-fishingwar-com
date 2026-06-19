from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

SAMPLE_URL = "https://webs-fishingwar.com"
SAMPLE_KEYWORD = "捕鱼大作战"

@dataclass
class KeywordNote:
    keyword: str
    source_url: str
    tags: List[str]
    note: str
    created_at: Optional[str] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def summary(self) -> str:
        tag_str = ", ".join(self.tags)
        return f"[{self.keyword}] 标签: {tag_str} | 来源: {self.source_url}"

    def full_note(self) -> str:
        lines = [
            f"关键词：{self.keyword}",
            f"来源网址：{self.source_url}",
            f"创建时间：{self.created_at}",
            f"标签：{', '.join(self.tags)}",
            f"备注：{self.note}",
        ]
        return "\n".join(lines)


def format_notes_as_table(notes: List[KeywordNote]) -> str:
    if not notes:
        return "（无笔记）"
    header = f"{'关键词':<12} {'来源':<30} {'标签':<20} {'备注':<30}"
    sep = "-" * 90
    rows = [header, sep]
    for n in notes:
        kw = n.keyword[:10]
        src = n.source_url[:28]
        tag = ", ".join(n.tags)[:18]
        nt = n.note[:28]
        rows.append(f"{kw:<12} {src:<30} {tag:<20} {nt:<30}")
    return "\n".join(rows)


def format_notes_as_list(notes: List[KeywordNote]) -> str:
    if not notes:
        return "（无笔记）"
    parts = []
    for i, n in enumerate(notes, 1):
        parts.append(f"{i}. {n.keyword} — {n.note[:40]}")
    return "\n".join(parts)


def create_sample_notes() -> List[KeywordNote]:
    return [
        KeywordNote(
            keyword=SAMPLE_KEYWORD,
            source_url=SAMPLE_URL,
            tags=["游戏", "娱乐", "捕鱼"],
            note="这是一款流行的休闲捕鱼游戏，玩家可以体验多种鱼群和武器。",
        ),
        KeywordNote(
            keyword="捕鱼大作战 新手攻略",
            source_url=f"{SAMPLE_URL}/guide",
            tags=["攻略", "新手"],
            note="新手推荐先使用基础炮弹，熟悉鱼群分值后再升级武器。",
        ),
        KeywordNote(
            keyword="捕鱼大作战 武器种类",
            source_url=f"{SAMPLE_URL}/weapons",
            tags=["武器", "分类"],
            note="包含普通炮、激光炮、散射炮等多种武器，不同武器消耗金币不同。",
        ),
    ]


def main():
    notes = create_sample_notes()
    print("=== 笔记摘要 ===")
    for n in notes:
        print(n.summary())
    print()
    print("=== 详细笔记（表格） ===")
    print(format_notes_as_table(notes))
    print()
    print("=== 简要列表 ===")
    print(format_notes_as_list(notes))


if __name__ == "__main__":
    main()