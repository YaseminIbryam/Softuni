def add(username: str, sent: int, received: int):
    if username not in messages.keys():
        messages[username] = {'sent': sent, 'received': received}


def message(sender: str, receiver: str):
    if sender in messages.keys() and receiver in messages.keys():  # what if sender and receiver are the same person???
        messages[sender]['sent'] += 1
        messages[receiver]['received'] += 1
        if messages[sender]['received'] + messages[sender]['sent'] == capacity:
            print(f"{sender} reached the capacity!")
            del messages[sender]
        if messages[receiver]['received'] + messages[receiver]['sent'] == capacity:
            print(f"{receiver} reached the capacity!")
            del messages[receiver]


def empty(username: str):
    if username in messages.keys():
        del messages[username]
    elif username == 'All':
        messages.clear()


messages = {}
capacity = int(input())
while True:
    command_list = input().split('=')
    command = command_list[0]
    if command == 'Statistics':
        break
    if command == 'Add':
        add(command_list[1], int(command_list[2]), int(command_list[3]))
    elif command == 'Message':
        message(command_list[1], command_list[2])
    elif command == 'Empty':
        empty(command_list[1])
print(f'Users count: {len(messages.keys())}')
for name, sent_and_received in messages.values():
    print(f"{name}-{sent_and_received['sent'] + sent_and_received['received']}")
