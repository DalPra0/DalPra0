#!/usr/bin/env python3
"""Atualiza seções dinâmicas do README do perfil GitHub."""

from __future__ import annotations

import json
import os
import re
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

USERNAME = os.environ.get("GITHUB_USERNAME", "DalPra0")
README_PATH = Path(__file__).resolve().parent.parent / "README.md"
API_BASE = "https://api.github.com"


def api_get(path: str) -> list | dict:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "DalPra0-profile-readme-updater",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    request = urllib.request.Request(f"{API_BASE}{path}", headers=headers)
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read().decode())


def fetch_repos() -> list[dict]:
    repos: list[dict] = []
    page = 1
    while True:
        batch = api_get(
            f"/users/{USERNAME}/repos?per_page=100&page={page}&sort=pushed"
        )
        if not isinstance(batch, list) or not batch:
            break
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return [repo for repo in repos if not repo.get("fork") and repo.get("name") != USERNAME]


def aggregate_languages(repos: list[dict]) -> dict[str, int]:
    totals: dict[str, int] = {}
    for repo in repos:
        language = repo.get("language")
        if language:
            totals[language] = totals.get(language, 0) + 1
    return dict(sorted(totals.items(), key=lambda item: item[1], reverse=True))


def format_date(iso_date: str) -> str:
    parsed = datetime.fromisoformat(iso_date.replace("Z", "+00:00"))
    return parsed.astimezone(timezone.utc).strftime("%d/%m/%Y")


def replace_section(content: str, name: str, body: str) -> str:
    pattern = re.compile(
        rf"(<!--START:{name}-->)(.*?)(<!--END:{name}-->)",
        re.DOTALL,
    )
    replacement = rf"\1\n{body}\n\3"
    updated, count = pattern.subn(replacement, content, count=1)
    if count != 1:
        raise RuntimeError(f"Seção {name} não encontrada no README.")
    return updated


def build_activity_section(repos: list[dict]) -> str:
    if not repos:
        return "_Nenhum repositório público encontrado._"

    latest = max(repos, key=lambda repo: repo["pushed_at"])
    name = latest["name"]
    url = latest["html_url"]
    language = latest.get("language") or "—"
    pushed = format_date(latest["pushed_at"])
    description = latest.get("description") or "Sem descrição no GitHub."

    recent = sorted(repos, key=lambda repo: repo["pushed_at"], reverse=True)[:5]
    recent_lines = "\n".join(
        f"- [`{repo['name']}`]({repo['html_url']}) · {repo.get('language') or '—'} · {format_date(repo['pushed_at'])}"
        for repo in recent
    )

    return f"""**Último push:** [`{name}`]({url}) · `{language}` · {pushed}

> {description}

**Repositórios recentes**

{recent_lines}"""


def build_stats_section(repos: list[dict], languages: dict[str, int]) -> str:
    total = len(repos)
    top = languages.items().__iter__()
    top_three = list(top)[:3]
    lang_line = " · ".join(f"`{name}` ×{count}" for name, count in top_three) or "`—`"
    updated_at = datetime.now(timezone.utc).strftime("%d/%m/%Y %H:%M UTC")

    return f"""| Métrica | Valor |
| --- | --- |
| Repositórios públicos | **{total}** |
| Linguagens mais usadas | {lang_line} |
| Atualizado em | {updated_at} |"""


def main() -> None:
    repos = fetch_repos()
    languages = aggregate_languages(repos)
    content = README_PATH.read_text(encoding="utf-8")

    content = replace_section(content, "ACTIVITY", build_activity_section(repos))
    content = replace_section(content, "STATS", build_stats_section(repos, languages))

    README_PATH.write_text(content, encoding="utf-8")
    print(f"README atualizado com {len(repos)} repositórios.")


if __name__ == "__main__":
    try:
        main()
    except urllib.error.HTTPError as error:
        raise SystemExit(f"Erro na API do GitHub: {error.code} {error.reason}") from error
