# brain-games

## Hexlet tests and linter status:
[![Actions Status](https://github.com/alexa-brave/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/alexa-brave/python-project-49/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=alexa-brave_brain-games&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=alexa-brave_brain-games)

## Description
**«Игры разума»** — набор из пяти консольных игр, построенных по принципу популярных мобильных приложений для прокачки мозга. Каждая игра задает вопросы, на которые нужно дать правильные ответы. После трех правильных ответов считается, что игра пройдена. Неправильные ответы завершают игру и предлагают пройти ее заново. Игры:

* _Калькулятор._ Арифметические выражения, которые необходимо вычислить
* _Прогрессия._ Поиск пропущенных чисел в последовательности чисел
* _Определение четного числа_
* _Определение наибольшего общего делителя_
* _Определение простого числа_

## Links
This project was built using these tools:
| Tool | Description |
|:----:|-------------|
| [uv](https://docs.astral.sh/uv/) | An extremely fast Python package and project manager, written in Rust |
| [ruff](https://docs.astral.sh/ruff/) | An extremely fast Python linter and code formatter, written in Rust |

## Setup
```bash
python3 -m pip install -U pip && pip install uv
uv build
uv tool install --force dist/hexlet_code-0.1.0-py3-none-any.whl
```
## Examples
Run the game:
```bash
brain-even
brain-calc
brain-gcd
brain-progression
brain-prime
```

## Install and demo brain-game:
[![asciicast](https://asciinema.org/a/ISlo2bvdem0VXFwstEclVSRLu.svg)](https://asciinema.org/a/ISlo2bvdem0VXFwstEclVSRLu)
