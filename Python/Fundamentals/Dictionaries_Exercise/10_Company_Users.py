companies = {}
while True:
    command = input()
    if command == "End":
        for company, ids in companies.items():
            print(company)
            for Id in ids:
                print(f"-- {Id}")
        break
    name, employee_id = command.split(' -> ')
    if name in companies.keys() and employee_id not in companies[name]:
        companies[name].append(employee_id)
    elif name not in companies.keys():
        companies[name] = [employee_id]