import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from services.channels import Channels
from services.data_processing import DataProcessing

load_dotenv()
app = App(token=os.environ["BOT_TOKEN"])

res = Channels.get_all_channel_names(app)
DataProcessing.output_array_to_csv(res)

# if __name__ == "__main__":
#     SocketModeHandler(app, os.environ["APP_TOKEN"]).start()
