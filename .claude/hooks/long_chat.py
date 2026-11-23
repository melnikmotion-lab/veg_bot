#!/usr/bin/env python3
"""Перед каждым сообщением Лилы считает, сколько занимает чат.
Если больше порога — Claude получает напоминание: сказать Лиле, что чат длинный,
и создать новый чат со сводкой. Срабатывает ДО того, как система сожмёт историю."""
import json, sys

WARN_TOKENS = 200_000   # предупреждать заранее (сжатие истории — около 196 000)

try:
    data = json.load(sys.stdin)
    used = 0
    with open(data["transcript_path"], encoding="utf-8") as f:
        for line in f:
            try:
                d = json.loads(line)
            except Exception:
                continue
            if d.get("type") == "assistant" and not d.get("isSidechain"):
                u = (d.get("message") or {}).get("usage") or {}
                t = (u.get("input_tokens", 0) + u.get("cache_read_input_tokens", 0)
                     + u.get("cache_creation_input_tokens", 0) + u.get("output_tokens", 0))
                if t:
                    used = t
    if used >= WARN_TOKENS:
        msg = (f"АВТОМАТИЧЕСКОЕ УВЕДОМЛЕНИЕ: чат стал слишком длинным (занято ~{used // 1000} тыс. токенов, "
               f"порог {WARN_TOKENS // 1000} тыс.). Правило Лилы: 1) коротко ответь на её сообщение; "
               "2) если новый чат ещё не создан — создай его через mcp__claude-code-remote__create_session "
               "с source_url=https://github.com/melnikmotion-lab/veg_bot (ТОЛЬКО этот репозиторий; she-bot потом через add_repo), "
               "в prompt — полная сводка, первым пунктом ДОСЛОВНО «ГЛАВНЫЕ ПРАВИЛА» из CLAUDE.md; "
               "3) напиши Лиле в начале ответа: «Этот чат стал слишком длинным. Новый чат создан — переходите, пожалуйста, туда: <ссылка>». "
               "Если новый чат уже создан — коротко ответь и снова напомни перейти по ссылке.")
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit",
                                                 "additionalContext": msg}}, ensure_ascii=False))
except Exception:
    pass
sys.exit(0)
