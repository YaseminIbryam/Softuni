class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
while True:
    information = input().split()
    if "Stop" in information:
        break
    emails.append(information)

indices = list(map(int, input().split(", ")))
for index, email in enumerate(emails):
    email = Email(email[0], email[1], email[2])
    if index in indices:
        email.send()
    print(email.get_info())
