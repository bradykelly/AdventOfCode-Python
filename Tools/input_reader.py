import os
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

def inputForDay(day, year=2021) -> str:
    """
    Returns the input for the given day as a string
    """
    path = Path(f"input_files/{year}_{day}_Input.txt")
    if not path.is_file():
        path.parents[0].mkdir(parents=True, exist_ok=True)
        url = f"https://adventofcode.com/{year}/day/{day}/input"
        text = downloadText(url)
        with open(path, "w") as file:
            file.write(text)
        return text
    else:
        with open(path, "r") as file:
            return file.read()
 

def downloadText(url) -> str:
    """
    Downloads the text from the given url and returns it as a string
    """
    cookies_dict = {"session": os.getenv("SESSION_COOKIE")}
    response = requests.get(url, cookies=cookies_dict)
    return response.text