import requests
from bs4 import BeautifulSoup

KEYWORDS = ["retail", "shop", "sales assistant", "store assistant"]
LOCATION = "Mullingar"

URLS = [
    "https://ie.indeed.com/jobs?q=retail&l=Mullingar",
    "https://www.irishjobs.ie/Jobs/Mullingar-Retail",
]

def check_jobs():
    for url in URLS:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")

        jobs = soup.find_all("a")

        for job in jobs:
            text = job.text.lower()

            if LOCATION.lower() in text:
                for k in KEYWORDS:
                    if k in text:
                        print("FOUND:", text)


if __name__ == "__main__":
    check_jobs()
