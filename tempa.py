import requests
 
myToken = "xoxb-2065052070515-2065055793955-p5ZVzRniMbn6vym7CVOVYaBJ"

def post_message(token, channel, text):
    """슬랙 메시지 전송"""
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )

post_message(myToken,"#자동매매", "tlqnksdnfksd")