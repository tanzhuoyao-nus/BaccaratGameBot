from BaccaratGameBot import BaccaratGame_bot
import telegram

START_CMD = "/start@WhereToMeetBot"
JOIN_CMD = "/join@WhereToMeetBot"
GO_CMD = "/go@WhereToMeetBot"
STOP_CMD = "/stop@WhereToMeetBot"


update_id = None

# initialises the WhereToMeet_bot class
bot = BaccaratGame_bot("config.cfg")

def make_reply(msg):
    if msg is not None:
        reply = msg
    return reply

while True:
    print("...")
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]

    if updates:
        for item in updates:
            update_id = item["update_id"]
            print(item)

    