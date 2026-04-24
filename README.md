<div align="center">
  <img src="https://gameofthronesquotes.xyz/img/logo.png" width="120" />

# game_of_thrones_quotes.py
> Web-API for [Game of Thrones Quotes](https://gameofthronesquotes.xyz) a REST API with quotes, characters, and houses from the Game of Thrones universe.
</div>

## Quick Start
```python
from game_of_thrones_quotes import GameOfThronesQuotes

got = GameOfThronesQuotes()

# Get a random quote
print(got.get_random_quote())

# Get 5 quotes from Tyrion
print(got.get_character_quotes("tyrion", number=5))

# List all houses
print(got.get_houses_list())
```

---

## Quotes

| Method | Description |
|--------|-------------|
| `get_random_quote(number)` | Get one or more random quotes (default: `1`) |
| `get_character_quotes(character_name, number)` | Get quotes by a character (default: `1`) |

---

## Characters

| Method | Description |
|--------|-------------|
| `get_characters_list()` | Get all characters |
| `get_character_details(character_name)` | Get details for a specific character |

---

## Houses

| Method | Description |
|--------|-------------|
| `get_houses_list()` | Get all houses |
| `get_house_by_name(house_name)` | Get details for a specific house |
