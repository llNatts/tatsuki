import json
from datetime import datetime
from os import path
import json

class utils:
    def ReactRoleCreate_json(self,channelID,messageID,roleID,emoji):
        data = {
            'Id': {
                "guid_id"
                "channel_id": channelID,
                "message_id": messageID,
                "role_id": roleID,
                "emoji": emoji
            },
            "Date": "NOW",
            "Owner": "me",
        }
        with open('reactionrole.json', 'w') as f:
            json.dump(data, f)
            print(self)
utils.ReactRoleCreate_json(utils,12,34,56,78)