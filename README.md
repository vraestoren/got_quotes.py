# got_quotes.py
Web-API for [gameofthronesquotes.xyz](https://gameofthronesquotes.xyz) website to retrieve some quotes of Game of Thrones

## Example
```python
from got_quotes import GameOfThronesQuotes

got_quotes = GameOfThronesQuotes()
random_quote = got_quotes.get_random_quote()
print(random_quote)
```
