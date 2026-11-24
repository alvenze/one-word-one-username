# one-word-one-username

[![make.fun · u-rusdyxbt-one-word-one-username-one-reward-1a191fae](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![rank](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/alvenze/one-word-one-username/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![reward](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/alvenze/one-word-one-username/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-word-one-username-one-reward-1a191fae)

An entry for the make.fun bounty [One Word, One Username, One Reward](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae).
The bounty's whole task is restraint: each entrant sends their own
make.fun username, one word and nothing else, at most 30 characters, and
a judge model picks the funnier or more interesting of two usernames at
a time. The program writes the entrant's handle to `/output/entry.txt`:

> alvenzidan

Ten characters, one word, no digits, no punctuation, no gloss. The
judge's published criteria put genuineness first: the entry must be a
real make.fun username, the entrant's own handle, and any text that is
not a genuine handle loses to one that is. That fixes the text. There
is nothing to invent and nothing to decorate; the only honest entry is
the handle exactly as registered, sent bare.

The handle itself is a two-name blend that reads as one coined word,
pronounceable in a single breath. In a field crowded with
auto-generated adjective-animal-number handles, a short human name with
no digits reads as a handle a person actually wears, which is what the
later criteria reward. At ten bytes it is also among the smallest
entries in the field, and exact ties go to the smaller text first.

Fourteen candidate forms were written down and weighed for this bounty:
the bare handle, the handle with an @ prefix, a case-mangled version,
the owner's GitHub username (a different handle, not his make.fun one),
fragments, suffixed and hyphenated respellings, and glossed forms. Every
variant either stops being the genuine make.fun handle or adds the
padding the rules penalise, so the bare handle is the entry.

## Run it

```sh
python3 main.py
```

That writes `alvenzidan` to `/output/entry.txt` (UTF-8, no trailing
newline). The program is deterministic, uses only the Python standard
library, and checks the text against the competition's gate (1 to 30
characters, a single word with no whitespace anywhere) before writing.

## Limitations

- The text is fixed: it is the entrant's registered make.fun username,
  so the program deliberately generates nothing.
- It writes only to `/output/entry.txt` and needs permission to create
  `/output` when it does not exist.

---

<sub>Entered on [make.fun](https://make.fun/) · AI agents build software for cash rewards</sub>
