from pathlib import Path

filters_path = Path("driver/filters.py")
source = filters_path.read_text(encoding="utf-8")
old = """def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES) & rate_limit"""
new = """# Arabic aliases are accepted alongside the original English commands.
ARABIC_COMMAND_ALIASES = {
    "play": ["شغل", "شغّل", "تشغيل"],
    "vplay": ["فيديو", "شغل_فيديو"],
    "vstream": ["بث", "بث_مباشر"],
    "search": ["بحث"], "radio": ["راديو"], "iptv": ["تلفاز"],
    "library": ["مكتبة"], "lplay": ["شغل_ملف"],
    "topic": ["موضوع"], "record": ["سجل"],
    "stoprec": ["انهاء_التسجيل"],
    "pause": ["ايقاف", "إيقاف", "توقيف"],
    "resume": ["استمرار", "واصل"],
    "continue": ["اكمل", "أكمل"], "skip": ["تخطي", "تجاوز"],
    "loop": ["تكرار"], "autoplay": ["تشغيل_تلقائي"],
    "shuffle": ["خلط"], "clear": ["مسح_القائمة"],
    "stop": ["انهاء", "إنهاء", "توقف"], "seek": ["تقديم"],
    "vmute": ["كتم"], "vunmute": ["الغاء_الكتم", "إلغاء_الكتم"],
    "playlist": ["قائمة", "قائمة_التشغيل"],
    "info": ["معلومات", "الان_يعمل"], "screenshot": ["لقطة"],
    "help": ["مساعدة", "الاوامر", "الأوامر"],
    "song": ["اغنية", "أغنية"], "video": ["تحميل_فيديو"],
    "userbotjoin": ["دخول_المساعد"],
    "userbotleave": ["خروج_المساعد"],
    "ping": ["فحص"], "alive": ["حي"], "uptime": ["مدة_العمل"],
    "volume": ["الصوت"],
}


def command(commands: Union[str, List[str]]):
    requested = [commands] if isinstance(commands, str) else list(commands)
    accepted = list(requested)
    for name in requested:
        accepted.extend(ARABIC_COMMAND_ALIASES.get(name.split("@", 1)[0], []))
    return filters.command(list(dict.fromkeys(accepted)), COMMAND_PREFIXES) & rate_limit"""
if old not in source:
    raise SystemExit("Expected command() implementation not found; no partial patch applied.")
filters_path.write_text(source.replace(old, new), encoding="utf-8")

readme_path = Path("README.md")
readme = readme_path.read_text(encoding="utf-8")
readme = readme.replace("# tg-streaming-bot", "# Abdou Telegram Media Player", 1)
readme = readme.replace(
    "git clone https://github.com/antlis/tg-streaming-bot.git",
    "git clone https://github.com/abdouhamadouch/abdou-telegram-media-player.git",
)
section = """## Arabic command aliases

These aliases work alongside the English commands:
- `/شغل` — `/play`
- `/فيديو` — `/vplay`
- `/بث` — `/vstream`
- `/بحث` — `/search`
- `/ايقاف` — `/pause`
- `/استمرار` — `/resume`
- `/تخطي` — `/skip`
- `/انهاء` — `/stop`
- `/قائمة` — `/playlist`
- `/مساعدة` — `/help`

This is a modified version of [antlis/tg-streaming-bot](https://github.com/antlis/tg-streaming-bot).
The upstream GNU GPL-3.0 license and original attribution are retained.

## ✨ Features"""
readme = readme.replace("## ✨ Features", section, 1)
readme_path.write_text(readme, encoding="utf-8")
