from fast_bitrix24 import Bitrix
import time, json

webhook = webhook 
b = Bitrix(webhook, respect_velocity_policy=True)

params = {
        "FILTER": {"CATEGORY_ID": 8},
        "SELECT": ["*", "UF_*"]
    }

time.sleep(2)
u.waitQue()

alldeal = b.get_all("crm.deal.list", params=params)

with open("deal/full.txt", "w") as file:
    json.dump(alldeal, file, indent=1)