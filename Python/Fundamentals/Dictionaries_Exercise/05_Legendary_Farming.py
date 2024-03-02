is_legendary_item_won = False
legendary_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junks = {}
while not is_legendary_item_won:
    materials_list = input().split()
    materials = [material.lower() for material in materials_list if materials_list.index(material) % 2 != 0]
    quantities = [int(quantity) for quantity in materials_list if materials_list.index(quantity) % 2 == 0]
    for index, material in enumerate(materials):
        if material in key_materials.keys():
            key_materials[material] += quantities[index]
            if key_materials[material] >= 250:
                key_materials[material] -= 250
                legendary_item = legendary_items[material]
                is_legendary_item_won = True
                print(f"{legendary_item} obtained!")
                for key_material, material_quantity in key_materials.items():
                    print(f"{key_material}: {material_quantity}")
                for junk, material_quantity in junks.items():
                    print(f"{junk}: {material_quantity}")
                break
        elif material in junks:
            junks[material] += quantities[index]
        else:
            junks[material] = quantities[index]
    if is_legendary_item_won:
        break
