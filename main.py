def create_cookbook(filename):
    ingrid_num = 0
    cur_list = []
    cur_dish = ''
    cookbook = {}

    with open(filename) as file:
        for line in file:
            line = line[:-1]
            if not line:
                continue
            try:
                ingrid_num = int(line)
            except Exception:
                if ingrid_num > 0:
                    # Ингридиент
                    ing_name, ing_number, ing_type = line.split(' | ')
                    ing_dct = {'ingridient_name': ing_name, 'quantity': ingrid_num, 'measure': ing_type}
                    cur_list.append(ing_dct)
                    ingrid_num -= 1
                    if not ingrid_num:
                        cookbook[cur_dish] = cur_list
                        cur_list = []
                else:
                    # Блюдо
                    cur_dish = line
    return cookbook


def get_shop_list_by_dishes(dishes, person_count):
    cookbook = create_cookbook('еда.txt')
    for dish in dishes:
        book = cookbook[dish]
        for ing in book:
            ing['quantity'] *= person_count
        print(book)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
