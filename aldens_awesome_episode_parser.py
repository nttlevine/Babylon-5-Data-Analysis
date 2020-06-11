"""Made as a favor for Naomi by Alden Bradford, at 1:00 AM on June 11th 2020."""
import pandas as pd


def clean_episode(episode):
    return [
        line
        for line in episode
        if len(line) > 6 and line[:6] not in ["      ", "======", " Note:"]
    ]


def clean_all(episodes):
    return [clean_episode(ep) for ep in episodes]


def line2scores(line):
    apart = line.split()
    score = apart[-1]
    name_parts = [part for part in apart if part[0] not in "0123456789"]
    name = " ".join(name_parts)
    return name, score


def episode2series(episode):
    pairs = [line2scores(line) for line in episode]
    names = [pair[0] for pair in pairs]
    scores = [pair[1] for pair in pairs]
    return pd.Series(index=names, data=scores)


def parse_episodes(episodes):
    episodes = clean_all(episodes)
    data = pd.concat([episode2series(ep) for ep in episodes], axis=1, sort=True)
    return data
