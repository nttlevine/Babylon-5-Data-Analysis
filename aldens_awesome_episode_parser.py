"""Made as a favor for Naomi by Alden Bradford, at 1:00 AM on June 11th 2020."""
import pandas as pd
from math import isnan


def clean_episode(episode):
    return [
        line
        for line in episode
        if len(line) > 6 and line[:6] not in ["      ", "======", " Note:"]
    ]


def trim_ep_8(episodes):
    episodes[8] = [line[:41] for line in episodes[8]]


def clean_all(episodes):
    trim_ep_8(episodes)
    return [clean_episode(ep) for ep in episodes]


def isnum(string):
    try:
        float(str)
        return True
    except ValueError:
        return False


def line2scores(line):
    apart = line.split()
    try:
        score = float(apart[-1])
    except ValueError:
        score = float("nan")
    name_parts = [part for part in apart if part[0] not in "0123456789"]
    name = " ".join(name_parts)
    return name, score


def episode2series(episode):
    pairs = [line2scores(line) for line in episode]
    pairs = [pair for pair in pairs if not isnan(pair[1])]
    names = [pair[0] for pair in pairs]
    scores = [pair[1] for pair in pairs]
    return pd.Series(index=names, data=scores)


def parse_episodes(episodes):
    episodes = clean_all(episodes)
    data = pd.concat([episode2series(ep) for ep in episodes], axis=1, sort=True)
    return data.astype(float)
