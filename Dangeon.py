import random, msvcrt, os


punkty = 0
poziom = 0
punkty_zycia = 100
walka = False


# wypisz legende
def legend():

    global punkty
    global poziom
    global punkty_zycia

    text = "-----Legenda-----      -----Poruszanie sie-----          -----Statystyki-----" + "\n\n" + "   gracz -> A                 gora -> w                      poziom -> " + str(poziom) + "\n" + "   przeciwnik -> ☺            dol -> s                       punkty -> " + str(punkty) + " \n" +  "   sciana -> ░                lewo -> a                      zycie -> " + str(punkty_zycia) + " hp\n" + "   przejscie dalej -> O       prawo -> d\n"
    return text


    # enemy tag = "☺"


# przetlumacz z liczb na stringa
def spawn_objects_in_map(string1, value, string2):
    string_value = ""
    if value == 8:
        string_value = "A"
    elif value == 1:
        string_value = "░"
    elif value == 5:
        string_value = "O"
    elif value == 7:
        string_value = "☺"
    else:
        string_value = " "

    return string1 + string_value + string2


# generuj siatke gry
def generate_grid(tab):
    grid_string = ""
    
    for i in range(len(tab)):

        if i == 0:
            for n in range(len(tab[i])): 
                grid_string += " ---"

            grid_string += "\n"
        for j in range(len(tab[i])):

            if j == 0:
                grid_string += "|"
            grid_string += spawn_objects_in_map(" ", tab[i][j], " |")

        grid_string += "\n"

        for nn in range(len(tab[i])):
            grid_string += " ---"
        grid_string += "\n"


    return grid_string


# generuje liste z wartosciami odopwiednimi dla danego przedmiotu
def generate_map_list(rozmiar, iloszScian, iloscPrzeciwnikow):
    map_table = []

    for i in range(rozmiar[0]):
        map_table.append([])
        for j in range(rozmiar[1]):
                map_table[i].append(0)
        

    # generuj pozycje gracza
    player_pos = [0, random.randint(0, rozmiar[1] - 1)]
    map_table[ player_pos[0] ] [ player_pos[1] ] = 8

    # generuj pozycje scian (iloscScian => ilosc generowanych scian)
    for i in range(iloszScian):
        wall_pos = [ random.randint( 1, rozmiar[0] - 2 ), random.randint( 0, rozmiar[1] - 1 ) ]
        map_table[ wall_pos[0] ] [ wall_pos[1] ] = 1

    for i in range(iloscPrzeciwnikow):
        x = random.randint( 0, rozmiar[1] - 1 )
        y = random.randint( 1, rozmiar[0] - 2 )
        if map_table[y][x] != 1:
            enemy_pos = [ y, x ]
            map_table[ enemy_pos[0] ] [ enemy_pos[1] ] = 7
    
    # generuj pozycje portalu
    portal_pos = [ rozmiar[0] - 1,  random.randint( 0, rozmiar[1] - 1 ) ]
    map_table[ portal_pos[0] ] [ portal_pos[1] ] = 5

    #wyswietl mape
    print(generate_grid(map_table))

    return map_table



# generuj mape zaleznie od poziomu
def generate_map():
    global poziom

    map_list = []

    if poziom < 5:
        map_list = generate_map_list([10,10], 25, 15)

    return map_list



# nasluchiwanie przycisku w, a, s, d
def input_system():
    inp = msvcrt.getwch()
    inp = str(inp.lower())


    if inp == "w":
        return 0
    if inp == "s":
        return 1
    if inp == "a":
        return 2
    if inp == "d":
        return 3
    else:
        return -1

# dodanie kierunkow poruszania sie po x, z
def movement_system():
    x_axis = 0
    z_axis = 0
    
    while True:

        inp = input_system()

        if inp == 0:
            x_axis = 0
            z_axis = -1
            return [x_axis, z_axis]
        elif inp == 1:
            x_axis = 0
            z_axis = 1
            return [x_axis, z_axis]
        elif inp == 2:
            x_axis = -1
            z_axis = 0
            return [x_axis, z_axis]
        elif inp == 3:
            x_axis = 1
            z_axis = 0
            return [x_axis, z_axis]
        else:
            x_axis = 0
            z_axis = 0

    return [ x_axis, z_axis]


    
def player_movement(map_table):

    global punkty
    global poziom
    global walka

    xz_axis = movement_system()
    player_pos = []
    before_player_pos = []

    for i in range(len(map_table)):

        if 8 in map_table[i]:
            player_pos = [i, map_table[i].index(8)]
            before_player_pos = [i, map_table[i].index(8)]

    if player_pos[0] + xz_axis[1] >= 0 and player_pos[0] + xz_axis[1] < len(map_table):
        player_pos[0] += xz_axis[1]

    if player_pos[1] + xz_axis[0] >= 0 and player_pos[1] + xz_axis[0] < len(map_table[0]):
        player_pos[1] += xz_axis[0]

    if map_table[player_pos[0]][player_pos[1]] == 5:
        poziom = poziom + 1

    if map_table[player_pos[0]][player_pos[1]] != 1 and map_table[player_pos[0]][player_pos[1]] != 7:
        map_table[before_player_pos[0]][before_player_pos[1]] = 0
        map_table[player_pos[0]][player_pos[1]] = 8

    if map_table[player_pos[0]][player_pos[1]] == 7:
        player_pos = before_player_pos
        walka = True


    punkty = punkty + 1

    os.system('cls')
    print(legend())
    print(generate_grid(map_table))
    return poziom



def display_fight_scene():
    global walka

    print("To Jest Walk z Trolem \n Elo Jesetm Zenek Nie Zabijesz mnie ahhaha \n gess  \n gergeg \n regergeg")

    xz_axis = movement_system()



def fight_with_enemy(map_table):
    global walka

    os.system('cls')
    display_fight_scene()

    walka = False

    os.system('cls')
    print(legend())
    print(generate_grid(map_table))






def update():
    map_table = []

    global poziom
    global walka

    print(legend())
    map_table = generate_map()
    while True:
        if walka == True:
            #os.system('cls')
            fight_with_enemy(map_table)

        if poziom != player_movement(map_table):
            os.system('cls')
            print(legend())
            map_table = generate_map()




update()
