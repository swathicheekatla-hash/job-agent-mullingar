import requests
from bs4 import BeautifulSoup
import smtplib

EMAIL = "swathi.cheekatla@gmail.com"
PASSWORD = "ehprdurpwlqjwymb"

def send_mail(text):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL, PASSWORD)

    message = "New job found:\n" + text

    server.sendmail(EMAIL, EMAIL, message)
    server.quit()


def check():
    url = "https://ie.indeed.com/jobs?q=retail&l=Mullingar"

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    for job in soup.find_all("a"):
        t = job.text.lower()

        if "mullingar" in t and (
            "retail" in t or "shop" in t or "assistant" in t
        ):
            send_mail(t)


check()
