import requests
from bs4 import BeautifulSoup
from twilio.rest import Client


# =========================
# ===== USER SETTINGS =====
# =========================

LOCATION_WORDS = [
    "mullingar",
    "westmeath",
]

KEYWORDS = [

    # retail
    "retail",
    "shop",
    "store",
    "sales",
    "sales assistant",
    "shop assistant",
    "store assistant",
    "retail assistant",
    "retail associate",

    # supermarket
    "cashier",
    "checkout",
    "till",
    "customer assistant",
    "team member",
    "crew member",
    "shop floor",

    # part time
    "part time",
    "part-time",
    "full time",
    "temporary",
    "weekend",
    "evening",
    "morning shift",

    # no experience
    "no experience",
    "no experience required",
    "training provided",
    "entry level",
    "junior",
    "trainee",

    # office / desk
    "office",
    "admin",
    "administrator",
    "receptionist",
    "data entry",
    "clerk",
    "assistant",
    "office assistant",
    "front desk",

    # simple jobs
    "cleaner",
    "kitchen assistant",
    "counter",
    "bar staff",
    "server",
    "waitress",
    "waiter",
    "housekeeping",

    # stores
    "tesco",
    "centra",
    "supervalu",
    "aldi",
    "lidl",
    "dunnes",
    "penneys",
    "dealz",
    "spar",
    "mace",
]


SITES = [

    "https://ie.indeed.com/jobs?q=&l=Mullingar",

    "https://www.irishjobs.ie/Jobs/Mullingar",

    "https://www.jobs.ie/jobs.aspx?location=Mullingar",

    "https://jobsireland.ie",

]



# =========================
# ===== WHATSAPP SETUP =====
# =========================

TWILIO_SID = "PUT_SID"
TWILIO_TOKEN = "PUT_TOKEN"

FROM_WHATSAPP = "whatsapp:+14155238886"
TO_WHATSAPP = "whatsapp:+353XXXXXXXXX"



client = Client(TWILIO_SID, TWILIO_TOKEN)



# =========================
# ===== FUNCTIONS =====
# =========================


def send_whatsapp(msg):

    try:

        client.messages.create(

            body=msg,
            from_=FROM_WHATSAPP,
            to=TO_WHATSAPP,

        )

        print("Sent:", msg)

    except Exception as e:

        print("Error sending:", e)



def match_location(text):

    text = text.lower()

    for w in LOCATION_WORDS:
        if w in text:
            return True

    return False



def match_keywords(text):

    text = text.lower()

    for k in KEYWORDS:
        if k in text:
            return True

    return False



def check_page(url):

    print("Checking:", url)

    try:

        r = requests.get(url, timeout=10)

        soup = BeautifulSoup(r.text, "html.parser")

        for a in soup.find_all("a"):

            t = a.text.lower()

            if match_location(t) and match_keywords(t):

                send_whatsapp(t)

    except Exception as e:

        print("Error:", e)



def run():

    for s in SITES:
        check_page(s)



# =========================
# ===== RUN =====
# =========================

if __name__ == "__main__":
    run()
