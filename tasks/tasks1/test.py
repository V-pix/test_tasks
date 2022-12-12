def customers_technic(old: list) -> tuple:
    converted_technic: dict[str, list[str, int]] = {}
    for device, price, name_owner, phone in old:
        client_id = name_owner + " " + phone
        if client_id not in converted_technic:
            converted_technic[client_id] = []
        converted_technic[client_id].append([device, price])
    for client, devices in converted_technic.items():
        return (client, ":", *devices)


if __name__ == "__main__":
    technic = [
        ("Ноутбук", 1500, "Татьяна", "89002001020"),
        ("Смартфон", 500, "Анна", "89202202325"),
        ("Проектор ", 300, "Андрей", "89505205656"),
        ("Принтер", 750, "Игорь", "89303303236"),
        ("Планшет", 2300, "Игорь", "89303303236"),
        ("Смартфон", 1000, "Андрей", "89505205656"),
        ("Ноутбук", 4800, "Татьяна", "89002001020"),
        ("Наушники", 780, "Марина", "89562002350"),
        ("Сканер", 550, "Сергей", "89808564559"),
        ("Планшет", 1200, "Анна", "89202202325"),
        ("Ноутбук", 1100, "Игорь", "89303303236"),
        ("Смартфон", 3500, "Татьяна", "89002001020"),
    ]
    print(customers_technic(technic))
