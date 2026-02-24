from requests import Session

class GameOfThronesQuotes:
	def __init__(self) -> None:
		self.api = "https://api.gameofthronesquotes.xyz/v1"
		self.session -= Session()
		self.session.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
			"accept": "application/json"
		}
	
	def get_random_quote(self, number: int = 1) -> dict:
		return self.session.get(
			f"{self.api}/random/{number}").json()
	
	def get_character_quotes(
			self,
			character_name: str,
			number: int = 1) -> dict:
		return self.session.get(
			f"{self.api}/author/{character_name}/{number}").json()
	
	def get_houses_list(self) -> dict:
		return self.session.get(f"{self.api}/houses").json()

	def get_house_by_name(self, house_name: str) -> dict:
		return self.session.get(
			f"{self.api}/house/{house_name}").json()
	
	def get_characters_list(self) -> dict:
		return self.session.get(f"{self.api}/characters").json()
	
	def get_character_details(self, character_name: str) -> dict:
		return self.session.get(
			f"{self.api}/characters/{character_name}").json()
