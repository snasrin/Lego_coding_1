webex_token="M2NhYjdlOWMtNjdmZC00ZDllLTgwNzYtMThjZTUxNWI5OWM2OWMxYmQyNTMtMTZk_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
message=input("Message to Support:")
print(message)

import requests
room_id = "Y2lzY29zcGFyazovL3VzL1JPT00vNDc4NjEwYjAtNTQ0MC0xMWVhLWIzMTYtZjNhMzllZWVlZTRj"
headers = {"Content-type":"application/json", "Authorization": "Bearer " + webex_token}
body = {"roomId": room_id, "text":message}
response = requests.post(url="https://webexapis.com/v1/messages",json=body, headers=headers)
print (response.status_code)