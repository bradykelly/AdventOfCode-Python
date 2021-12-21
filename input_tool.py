import os
import requests
from pathlib import Path
from dotenv import load_dotenv

class InputTool:

    def __init__(self):
        load_dotenv()   


    def input_for_day(self, day: int, year: int=2021) -> str:
        """
        Returns the input for the given day as a string
        """
        path = Path(f"input_files/{year}_{day}_Input.txt")
        if not path.is_file():
            path.parents[0].mkdir(parents=True, exist_ok=True)
            url = f"https://adventofcode.com/{year}/day/{day}/input"

            text = self.downloadText(url)
            with open(path, "w") as file:
                file.write(text)
            return text
            
        else:
            with open(path, "r") as file:
                return file.read()
 

    def downloadText(self, url: str) -> str:
        """
        Downloads the text from the given url and returns it as a string
        """
        cookies_dict = {"session": os.getenv("SESSION_COOKIE")}
        response = requests.get(url, cookies=cookies_dict)
        return response.text

    def clean_split(self, input: str, delim: str) -> list[str]:
        """
        Splits a string on a given delimiter and returns a list of non-empty strings
        """        
        return [x for x in input.split(delim) if x]

    def input_lines_for_day(self, day: int, year: int=2019) -> list[str]:
        """
        Returns the input for the given day as a list of lines
        """
        return self.clean_split(self.input_for_day(day, year), "\n")