from tkinter import *
import random
from time import sleep
from PIL import ImageTk, Image

# Screen RES 1280x720
# Def Glob Var

global wasd
wasd = True

global placedmenu
placedmenu = False

global placed
placed = False

global paused
paused = False

global just_unpasued
just_unpasued = False

global name
name = ""

global current_life
current_life = 1

global current_dash
current_dash = 1

global coins
coins = 0

global coinsgained
coinshgained = 0

global sizelevel
sizelevel = 1

global life_level
life_level = 1

global dash_level
dash_level = 1

# Used to destory objects placed on canvas
listofbuttons = []


def load_game():
    global name
    global current_life
    global coins
    global sizelevel
    global life_level
    global dash_level
    data = []
    try:
        file1 = open("save.txt", "r")
        for x in file1:
            data.append(x)
            print(x)
        file1.close()
    except BaseException:
        pass

    try:
        if data[0] == "":
            name = "Anon"
    except BaseException:
        name = "Anon"

    else:
        name = data[0]
    try:
        loaded_size_level = data[1]
    except BaseException:
        loaded_size_level = 1

    sizelevel = int(loaded_size_level)

    try:
        loaded_coins = data[2]
    except BaseException:
        loaded_coins = 0
    coins = int(float(loaded_coins))

    try:
        loaded_life = data[3]
    except BaseException:
        loaded_life = 1
    life_level = int(loaded_life)

    try:
        loaded_dash = data[4]
    except BaseException:
        pass
        loaded_dash = 1
    dash_level = int(loaded_dash)

    render_selection_menu()


def save_game():
    global name
    global current_life
    global coins
    global sizelevel
    global life_level
    global dash_level
    try:
        file1 = open("save.txt", "w")
    except BaseException:
        file1 = open("save.txt", "x")
    if (name) == "":
        file1.write("Anon" + '\n')
    else:
        try:
            name = name.strip('\n')
        except BaseException:
            pass
        file1.write(name + '\n')
    file1.write(str(sizelevel) + '\n')
    file1.write(str(int(coins)) + '\n')
    file1.write(str(life_level) + '\n')
    file1.write(str(dash_level) + '\n')
    file1.close()

# Used when "rendering" new windows


def reset_render():
    for x in listofbuttons:
        if x.winfo_exists():
            x.destroy()
    listofbuttons.clear()

# Implementation of "Boss Key"


def bossfrommenu(renderthing):
    global placedmenu
    if placedmenu:
        placedmenu = False
        reset_render()
        renderthing()
        window.update()
    else:
        img1 = Image.open("excel.jpg")
        test = ImageTk.PhotoImage(img1)

        labelimg = Label(image=test)
        labelimg.image = test

        labelimg.place(x=0, y=0)
        listofbuttons.append(labelimg)
        placedmenu = True

# Render first menu of the game


def render_menu():
    reset_render()

    img1 = Image.open("background.jpg")  # royalty free dreamstime.com
    test = ImageTk.PhotoImage(img1)

    labelimg = Label(image=test, borderwidth=0)
    labelimg.image = test

    labelimg.place(x=-(random.randint(400, 800)),
                   y=-(random.randint(100, 500)))
    listofbuttons.append(labelimg)

    window.bind('<b>', lambda event: bossfrommenu(render_menu))
    window.resizable(False, False)
    window.geometry("1280x720")
    new_game_btn = Button(
        window,
        text="New Game",
        font=(
            "Arial Bold",
            40),
        bg="#b3ffff",
        width=10,
        command=render_selection_menu)
    load_game_btn = Button(
        window,
        text="Load Game",
        font=(
            "Arial Bold",
            40),
        bg="#b3ffff",
        width=10,
        command=load_game)
    start_game_btnnn = Button(
        window, text="Start Game", font=(
            "Arial Bold", 40), bg="#b3ffff", width=10)
    new_game_btn.place(x=480, y=100)
    listofbuttons.append(new_game_btn)
    load_game_btn.place(x=480, y=225)
    listofbuttons.append(load_game_btn)

    window.configure(background="#000000")
    window.title("Dodge Master 9000")

# Renders cassino instance


def render_casino():
    reset_render

    global coins

    # Only sensitive to numbers
    def get_text():
        text = my_text.get(1.0, END)
        try:
            betamount = int(text)
            calculate_win(betamount)
        except BaseException:
            pass

    def calculate_win(betamount):
        global coins
        if betamount == 420420:
            winnings = 1000
            coins = coins + winnings
            render_casino()
        else:
            if betamount > coins:
                pass
            else:
                winnings = 0
                number = random.randint(0, 1)
                if number == 0:
                    winnings = betamount * 2
                else:
                    winnings = -(betamount)
                coins = coins + winnings
                render_casino()

    window.bind('<b>', lambda event: bossfrommenu(render_casino))
    reset_render()
    global sizelevel
    global life_level
    window.configure(background="#000000")
    window.resizable(False, False)
    window.geometry("1280x720")

    back_btn = Button(
        window,
        text="Back",
        font=(
            "Arial Bold",
            28),
        bg="#b3ffff",
        width=6,
        command=render_selection_menu)
    back_btn.place(x=0, y=660)
    listofbuttons.append(back_btn)

    img1 = Image.open("cards.jpg")  # dreamstime.com
    test = ImageTk.PhotoImage(img1)

    labelimg = Label(image=test, borderwidth=0)
    labelimg.image = test

    labelimg.place(x=400, y=0)
    listofbuttons.append(labelimg)

    my_text = Text(
        window,
        width=20,
        height=2,
        font=(
            "Arial Bold",
            28),
        bg="#000000",
        fg="#c53c3c")
    my_text.place(x=150, y=290)
    listofbuttons.append(my_text)

    get_text_button = Button(
        window,
        text="Play",
        font=(
            "Arial Bold",
            28),
        bg="#790000",
        width=6,
        command=get_text)
    get_text_button.place(x=290, y=420)
    listofbuttons.append(get_text_button)

    stat2_lab = Label(window, text="Coins: " + str(int(coins)),
                      font=('consolas', 20), fg="#b3ffff", bg="#000000")
    stat2_lab.place(x=290, y=220)
    listofbuttons.append(stat2_lab)

# Renders menu instance


def render_selection_menu():
    window.bind('<b>', lambda event: bossfrommenu(render_selection_menu))
    reset_render()
    sortleaderboard()
    global name
    global coins
    global sizelevel
    global life_level
    global dash_level

    img1 = Image.open("background.jpg")  # dreamstime.com
    test = ImageTk.PhotoImage(img1)

    labelimg = Label(image=test, borderwidth=0)
    labelimg.image = test

    # Random position of stars achieved
    labelimg.place(x=-(random.randint(400, 800)),
                   y=-(random.randint(100, 500)))
    listofbuttons.append(labelimg)

    window.configure(background="#000000")
    window.resizable(False, False)
    window.geometry("1280x720")
    slow_game_btn = Button(
        window,
        text="Normal Game",
        font=(
            "Arial Bold",
            40),
        bg="#b3ffff",
        width=12,
        command=render_maingame)
    save_game_btn = Button(
        window,
        text="Save Game",
        font=(
            "Arial Bold",
            40),
        bg="#b3ffff",
        width=12,
        command=save_game)
    shop_btn = Button(
        window,
        text="Shop",
        font=(
            "Arial Bold",
            40),
        bg="#b3ffff",
        width=10,
        command=render_shop)
    casino_btn = Button(
        window,
        text="Casino",
        font=(
            "Arial Bold",
            40),
        bg="#b3ffff",
        width=10,
        command=render_casino)
    back_btn = Button(
        window,
        text="Back",
        font=(
            "Arial Bold",
            28),
        bg="#b3ffff",
        width=6,
        command=render_menu)
    slow_game_btn.place(x=450, y=80)
    listofbuttons.append(slow_game_btn)
    save_game_btn.place(x=450, y=205)
    listofbuttons.append(save_game_btn)
    shop_btn.place(x=480, y=450)
    listofbuttons.append(shop_btn)
    casino_btn.place(x=480, y=575)
    listofbuttons.append(casino_btn)
    back_btn.place(x=0, y=660)
    listofbuttons.append(back_btn)

    pos0_lab = Label(
        window,
        text=("Leaderboard"),
        font=(
            'consolas',
            30),
        fg="#b3ffff",
        bg="#000000")
    pos0_lab.place(x=50, y=30)
    listofbuttons.append(pos0_lab)

    pos1_lab = Label(window, text=("1) " + getleaderboardpos(0)),
                     font=('consolas', 20), fg="#b3ffff", bg="#000000")
    pos1_lab.place(x=50, y=100)
    listofbuttons.append(pos1_lab)

    pos2_lab = Label(window, text=("2) " + getleaderboardpos(1)),
                     font=('consolas', 20), fg="#b3ffff", bg="#000000")
    pos2_lab.place(x=50, y=150)
    listofbuttons.append(pos2_lab)

    pos3_lab = Label(window, text=("3) " + getleaderboardpos(2)),
                     font=('consolas', 20), fg="#b3ffff", bg="#000000")
    pos3_lab.place(x=50, y=200)
    listofbuttons.append(pos3_lab)

    pos4_lab = Label(window, text=("4) " + getleaderboardpos(3)),
                     font=('consolas', 20), fg="#b3ffff", bg="#000000")
    pos4_lab.place(x=50, y=250)
    listofbuttons.append(pos4_lab)

    pos5_lab = Label(window, text=("5) " + getleaderboardpos(4)),
                     font=('consolas', 20), fg="#b3ffff", bg="#000000")
    pos5_lab.place(x=50, y=300)
    listofbuttons.append(pos5_lab)

    stat1_lab = Label(
        window,
        text="Stats: ",
        font=(
            'consolas',
            20),
        fg="#b3ffff",
        bg="#000000")
    stat1_lab.place(x=980, y=360)
    listofbuttons.append(stat1_lab)

    stat2_lab = Label(window, text="Coins: " + str(int(coins)),
                      font=('consolas', 20), fg="#b3ffff", bg="#000000")
    stat2_lab.place(x=980, y=430)
    listofbuttons.append(stat2_lab)

    stat3_lab = Label(window, text="Size Level: " + str(int(sizelevel)),
                      font=('consolas', 20), fg="#b3ffff", bg="#000000")
    stat3_lab.place(x=980, y=500)
    listofbuttons.append(stat3_lab)

    stat4_lab = Label(window,
                      text="Life Level: " + str(int(life_level)),
                      font=('consolas',
                            20),
                      fg="#b3ffff",
                      bg="#000000")
    stat4_lab.place(x=980, y=570)
    listofbuttons.append(stat4_lab)

    stat5_lab = Label(window,
                      text="Dash Level: " + str(int(dash_level)),
                      font=('consolas',
                            20),
                      fg="#b3ffff",
                      bg="#000000")
    stat5_lab.place(x=980, y=640)
    listofbuttons.append(stat5_lab)

    namelab1 = Label(
        window,
        text="Name:{}".format(name),
        font=(
            'consolas',
            20),
        fg="#b3ffff",
        bg="#000000")
    namelab1.place(x=1050, y=0)
    listofbuttons.append(namelab1)

    settings_btn = Button(
        window,
        text="Settings",
        font=(
            "Arial Bold",
            20),
        bg="#b3ffff",
        width=6,
        command=render_settings)
    settings_btn.place(x=1050, y=100)
    listofbuttons.append(settings_btn)

# Displays settings instance


def render_settings():

    def get_text():
        global name
        text = my_text.get(1.0, END)
        try:
            username = str(text)
            shortenedname = ""
            for i in range(len(username)):
                if i > 7:
                    break
                else:
                    shortenedname = shortenedname + username[i]
            name = shortenedname
            try:
                name = name.strip('\n')
            except BaseException:
                pass
        except BaseException:
            pass

    def do_nothing():
        pass
    window.bind('<b>', lambda event: do_nothing())
    window.bind('<space>', lambda event: bossfrommenu(render_settings))
    reset_render()
    global name
    global life_level
    window.configure(background="#000000")
    window.resizable(False, False)
    window.geometry("1280x720")

    back_btn = Button(
        window,
        text="Back",
        font=(
            "Arial Bold",
            28),
        bg="#b3ffff",
        width=6,
        command=render_selection_menu)
    back_btn.place(x=0, y=660)
    listofbuttons.append(back_btn)

    img1 = Image.open("gears.jpg")  # dreamstime.com
    test = ImageTk.PhotoImage(img1)

    labelimg = Label(image=test, borderwidth=0)
    labelimg.image = test

    labelimg.place(x=700, y=100)
    listofbuttons.append(labelimg)

    my_text = Text(
        window,
        width=20,
        height=2,
        font=(
            "Arial Bold",
            28),
        bg="#000000",
        fg="#2cb1db")
    my_text.place(x=150, y=290)
    listofbuttons.append(my_text)

    get_text_button = Button(
        window,
        text="Set Name",
        font=(
            "Arial Bold",
            28),
        bg="#6d6161",
        width=10,
        command=get_text)
    get_text_button.place(x=240, y=420)
    listofbuttons.append(get_text_button)

    set_wasd_button = Button(
        window,
        text="WASD",
        font=(
            "Arial Bold",
            28),
        bg="#6d6161",
        width=10,
        command=set_wasd)
    set_wasd_button.place(x=700, y=600)
    listofbuttons.append(set_wasd_button)

    set_arrows_button = Button(
        window,
        text="Arrows",
        font=(
            "Arial Bold",
            28),
        bg="#6d6161",
        width=10,
        command=set_arrows)
    set_arrows_button.place(x=980, y=600)
    listofbuttons.append(set_arrows_button)


def set_wasd():
    global wasd
    wasd = True


def set_arrows():
    global wasd
    wasd = False


def getleaderboardpos(posnum):
    data = []
    try:
        file1 = open("leaderboard.txt", "r")
        for x in file1:
            data.append(x)
            print(x)
        file1.close()
    except BaseException:
        pass
    try:
        return data[posnum]
    except BaseException:
        return "empty"

# Renders shop instance


def render_shop():
    reset_render()

    window.bind('<b>', lambda event: bossfrommenu(render_shop))

    global sizelevel
    global coins
    global life_level
    global dash_level

    window.configure(background="#000000")
    window.resizable(False, False)
    window.geometry("1280x720")

    img1 = Image.open("background.jpg")  # dreamstime.com
    test = ImageTk.PhotoImage(img1)

    labelimg = Label(image=test, borderwidth=0)
    labelimg.image = test

    labelimg.place(x=-(random.randint(400, 800)),
                   y=-(random.randint(100, 500)))
    listofbuttons.append(labelimg)

    buy_size_btn = Button(
        window,
        text="Decrease Size",
        font=(
            "Arial Bold",
            28),
        bg="#b3ffff",
        width=12,
        command=size_purchase)
    buy_size_btn.place(x=250, y=80)
    listofbuttons.append(buy_size_btn)

    sizelev = Label(
        window,
        text="Level: {}".format(sizelevel),
        font=(
            'consolas',
            30),
        bg="#000000",
        fg="#b3ffff")
    sizelev.place(x=0, y=90)
    listofbuttons.append(sizelev)

    sizecost = Label(
        window,
        text="Cost: {}".format(
            sizelevel * 10),
        font=(
            'consolas',
            30),
        bg="#000000",
        fg="#b3ffff")
    sizecost.place(x=600, y=90)
    listofbuttons.append(sizecost)

    buy_life_btn = Button(
        window,
        text="Add Life",
        font=(
            "Arial Bold",
            28),
        bg="#b3ffff",
        width=12,
        command=life_purchase)
    buy_life_btn.place(x=250, y=220)
    listofbuttons.append(buy_life_btn)

    lifelev = Label(
        window,
        text="Level: {}".format(life_level),
        font=(
            'consolas',
            30),
        bg="#000000",
        fg="#b3ffff")
    lifelev.place(x=0, y=230)
    listofbuttons.append(lifelev)

    lifecost = Label(
        window,
        text="Cost: {}".format(
            life_level * 10),
        font=(
            'consolas',
            30),
        bg="#000000",
        fg="#b3ffff")
    lifecost.place(x=600, y=230)
    listofbuttons.append(lifecost)

    buy_dash_btn = Button(
        window,
        text="Extra Dash",
        font=(
            "Arial Bold",
            28),
        bg="#b3ffff",
        width=12,
        command=dash_purchase)
    buy_dash_btn.place(x=250, y=360)
    listofbuttons.append(buy_dash_btn)

    dashlev = Label(
        window,
        text="Level: {}".format(dash_level),
        font=(
            'consolas',
            30),
        bg="#000000",
        fg="#b3ffff")
    dashlev.place(x=0, y=370)
    listofbuttons.append(dashlev)

    dashcost = Label(
        window,
        text="Cost: {}".format(
            dash_level * 10),
        font=(
            'consolas',
            30),
        bg="#000000",
        fg="#b3ffff")
    dashcost.place(x=600, y=370)
    listofbuttons.append(dashcost)

    back_btn = Button(
        window,
        text="Back",
        font=(
            "Arial Bold",
            30),
        bg="#b3ffff",
        width=6,
        command=render_selection_menu)
    back_btn.place(x=0, y=660)
    listofbuttons.append(back_btn)

    currentcoin_btn = Button(
        window, text="Coins:{}".format(
            int(coins)), font=(
            "Arial Bold", 30), bg="#b3ffff", width=10,)
    currentcoin_btn.place(x=980, y=620)
    listofbuttons.append(currentcoin_btn)

    # https://unsplash.com/@cdd20?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText
    img1 = Image.open("cart.jpg")
    test = ImageTk.PhotoImage(img1)

    labelimg = Label(image=test, borderwidth=0)
    labelimg.image = test

    labelimg.place(x=840, y=140)
    listofbuttons.append(labelimg)

    window.update()


def dash_purchase():
    global dash_level
    global coins

    if (dash_level * 10) > coins:
        print("not enough")
    else:
        coins = coins - (dash_level * 10)
        dash_level = int(dash_level) + 1
        render_shop()


def life_purchase():
    global life_level
    global coins

    if life_level > 8:
        pass
    else:

        if (life_level * 10) > coins:
            print("not enough")
        else:
            coins = coins - (life_level * 10)
            life_level = int(life_level) + 1
            render_shop()
    render_shop()


def size_purchase():
    global sizelevel
    global coins

    if (sizelevel * 10) > coins:
        print("not enough")
    else:
        coins = coins - (sizelevel * 10)
        sizelevel = sizelevel + 1
        render_shop()

# Renders the screen after a player has died


def render_summary():
    reset_render()
    global coinsgained

    window.bind('<b>', lambda event: bossfrommenu(render_summary))

    oldscore = coinsgained * 10

    # https://unsplash.com/@cdd20?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText
    img1 = Image.open("gameover.jpg")
    test = ImageTk.PhotoImage(img1)

    labelimg = Label(image=test, borderwidth=0)
    labelimg.image = test

    labelimg.place(x=-260, y=-100)
    listofbuttons.append(labelimg)

    # https://unsplash.com/@cdd20?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText
    img2 = Image.open("overtext.jpg")
    test2 = ImageTk.PhotoImage(img2)

    labelimg2 = Label(image=test2, borderwidth=0)
    labelimg2.image = test2

    labelimg2.place(x=-55, y=-120)
    listofbuttons.append(labelimg2)

    window.resizable(False, False)
    window.configure(background="#000000")
    window.geometry("1280x720")
    shop_btn = Button(
        window,
        text="Shop",
        font=(
            "Arial Bold",
            40),
        bg="#b3ffff",
        width=10,
        command=render_shop)
    play_again_btn = Button(
        window,
        text="Start Game",
        font=(
            "Arial Bold",
            40),
        bg="#b3ffff",
        width=10,
        command=render_maingame)
    play_again_btn.place(x=880, y=100)
    listofbuttons.append(play_again_btn)
    shop_btn.place(x=880, y=225)
    listofbuttons.append(shop_btn)

    finalscore = Label(
        window, text="Final Score:{}".format(
            int(oldscore)), font=(
            'consolas', 40), fg="#43c348", bg="#000000")
    finalscore.place(x=0, y=200)
    listofbuttons.append(finalscore)

    coinslabel = Label(
        window, text="Coins:{}".format(
            int(coins)), font=(
            'consolas', 40), fg="#b3ffff", bg="#000000")
    coinslabel.place(x=0, y=400)
    listofbuttons.append(coinslabel)

    coingain = Label(
        window, text="Coins Gained:{}".format(
            int(coinsgained)), font=(
            'consolas', 40), fg="#b3ffff", bg="#000000")
    coingain.place(x=0, y=500)
    listofbuttons.append(coingain)
    coinsgained = 0

    back_btn = Button(
        window,
        text="Back",
        font=(
            "Arial Bold",
            30),
        bg="#b3ffff",
        width=6,
        command=render_selection_menu)
    back_btn.place(x=0, y=660)
    listofbuttons.append(back_btn)

# Used to keep values consistant with any game/user impacts


def reset_globals():
    global life_level
    global dash_level
    global current_score
    global current_dash
    current_score = 0
    current_dash = dash_level
    global current_life
    current_life = life_level

# Renders Main game


def render_maingame():

    reset_globals()
    reset_render()
    window.geometry("1280x720")
    window.configure(background="#000000")
    window.title("Dodge Master 9000")
    window.resizable(False, False)

    # Base dificulty
    global NMBPROJECT
    NMBPROJECT = 5

    direction = 'down'

    global label
    label = Label(window, text="Score:{}".format(current_score),
                  font=('consolas', 40), bg="#000000", fg="#b3ffff")
    label.pack(side=TOP)

    canvas = Canvas(window, bg='#000000', height=720, width=1280, )
    canvas.pack()

    window.update()

    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    player2 = spawn_player(canvas)

    window.update()

    game_sequence(canvas, player2)

# Used as a multiplies to increase enemy spawn rate


def getintensity():
    if current_score < 100:
        return 1
    if current_score < 200:
        return 2
    if current_score < 300:
        return 3
    if current_score < 400:
        return 4
    if current_score < 500:
        return 5
    if current_score < 600:
        return 6
    if current_score < 700:
        return 7
    if current_score < 800:
        return 8
    if current_score < 900:
        return 9
    else:
        return 10


def randomcoords_Across():
    y = random.randint(0, 640)
    return y


def get_spawn(total_required):
    sides = []
    for i in range(total_required):
        sides.append(random.randint(0, 2))
    return sides


def get_spawn_coordinates(list_of_spawns):
    if list_of_spawns == 0:
        coord = random.randint(0, 720)
        return coord
    if list_of_spawns == 1:
        coord = random.randint(0, 1280)
        return coord
    if list_of_spawns == 2:
        coord = random.randint(0, 720)
        return coord

# creates projectiles with random coordiantes and direction


def create_projectiles(canvas):
    projectiles = []
    multiplier = getintensity()
    total_projectiles = NMBPROJECT * multiplier
    list_of_spawns = get_spawn(NMBPROJECT * multiplier)
    for i in range(0, total_projectiles):
        if list_of_spawns[i] == 0:
            x0 = 0
            y0 = get_spawn_coordinates(list_of_spawns[i])
            x1 = random.randint(20, 80)
            y1 = y0 + random.randint(5, 15)

            projectiles.append(
                canvas.create_rectangle(
                    x0, y0, x1, y1, fill="red"))
        if list_of_spawns[i] == 1:
            x0 = get_spawn_coordinates(list_of_spawns[i])
            y0 = 0
            x1 = x0 + random.randint(5, 15)
            y1 = random.randint(20, 80)

            projectiles.append(
                canvas.create_rectangle(
                    x0, y0, x1, y1, fill="green"))
        if list_of_spawns[i] == 2:
            x0 = 1280
            y0 = get_spawn_coordinates(list_of_spawns[i])
            x1 = x0 + random.randint(5, 15)
            y1 = y0 + random.randint(5, 15)

            projectiles.append(
                canvas.create_rectangle(
                    x0, y0, x1, y1, fill="orange"))

    return projectiles

# Handles the "collision event"


def deal_with_hit(canvas):
    global current_life
    current_life += -1
    global coins
    global coinsgained
    if current_life < 0:
        global window
        addtoleaderboard()
        window.destroy()
        window = Tk()
        coinsgained = (current_score / 10)
        coins = coins + (coinsgained)
        reset_globals()
        render_summary()
        return True
    return False


def re_render(canvas):
    new_player = spawn_player(canvas)
    window.update()
    game_sequence(canvas, new_player)


def clear_projectiles(projectiles, canvas):
    canvas.delete("all")
    re_render(canvas)


def spawn_player(canvas):
    x = 600
    y = 350
    global sizelevel
    player2 = canvas.create_rectangle(
        x, y, (x + 100) - (sizelevel * 5), (y + 100) - (sizelevel * 5), fill="blue")
    enable_keys(player2, canvas)
    return player2


def enable_keys(player2, canvas):

    if wasd:
        window.bind('<a>', lambda event: move_left(player2, canvas))

        window.bind('<d>', lambda event: move_right(player2, canvas))

        window.bind('<w>', lambda event: move_up(player2, canvas))

        window.bind('<s>', lambda event: move_down(player2, canvas))
    else:
        window.bind('<Left>', lambda event: move_left(player2, canvas))

        window.bind('<Right>', lambda event: move_right(player2, canvas))

        window.bind('<Up>', lambda event: move_up(player2, canvas))

        window.bind('<Down>', lambda event: move_down(player2, canvas))

    window.bind('<p>', lambda event: pause(canvas, player2))

    window.bind('<b>', lambda event: boss(canvas, player2))

    window.bind('<Button-1>', lambda event: teleport(player2, canvas, event))

    window.bind('<Escape>', lambda event: quit(canvas))

    window.bind('<space>', lambda event: do_nothing)

# Misc


def do_nothing():
    pass

# Quit function uses "life" to escape prematurely


def quit(canvas):
    global e
    global current_life
    overrulehit = True
    current_life = 0
    e = 800
    deal_with_hit(canvas)

# Pause function


def pause(canvas, player2):
    global e
    global paused
    global just_unpasued
    global placed

    if paused:
        paused = False
        placed = False
        e = 0
        just_unpasued = True
        game_sequence(canvas, player2)

    else:
        paused = True
        e = 600

# Boss Key


def boss(canvas, player2):
    global placed
    if placed:
        reset_render()
        window.update()
        pause(canvas, player2)
    else:
        pause(canvas, player2)
        img1 = Image.open("excel.jpg")
        test = ImageTk.PhotoImage(img1)

        labelimg = Label(image=test)
        labelimg.image = test

        labelimg.place(x=0, y=0)
        listofbuttons.append(labelimg)
        placed = True

# Main animation of game


def game_sequence(canvas, player2):

    global just_unpasued
    global current_score
    global label
    global current_life
    global e
    global paused
    global projectiles
    global current_dash

    label.config(text="Score: " + str(current_score))
    label.pack(side=TOP)
    window.update()

    life = Label(
        window,
        text="Life:{}".format(current_life),
        font=(
            'consolas',
            40),
        bg="#000000",
        fg="#b3ffff")
    life.place(x=0, y=0)

    dash = Label(
        window,
        text="Dash:{}".format(current_dash),
        font=(
            'consolas',
            40),
        bg="#000000",
        fg="#b3ffff")
    dash.place(x=1000, y=0)

    window.update()

    if paused or just_unpasued:
        just_unpasued = False
        pass
    else:
        projectiles = create_projectiles(canvas)

    speedx = 4
    speedy = 4
    if paused:
        pass
    else:
        e = 0
    nothit = True
    multiplier = getintensity()

    # e is almost a frame counter which is exploited to implement features
    # setting e to a number higher than 500 will pause the animation
    # lowering it to below 500 will reinstate it

    while e < 500 and nothit:
        e = e + 1
        speedred = random.randint(2, 4)
        if speedred > 20:
            speedred = 20
        speedgreen = random.randint(2, 4)
        if speedgreen > 20:
            speedred = 20
        speedorange = random.randint(2, 4)
        if speedred > 20:
            speedred = 20

        speedred = (speedred + (multiplier / 2))
        speedgreen = (speedgreen + (multiplier / 2))
        speedorange = (speedorange + (multiplier / 2))
        for i in range(len(projectiles)):
            if canvas.itemcget(projectiles[i], 'fill') == 'red':
                canvas.move(projectiles[i], speedred, 0)
            if canvas.itemcget(projectiles[i], 'fill') == 'green':
                canvas.move(projectiles[i], 0, speedgreen)
            if canvas.itemcget(projectiles[i], 'fill') == 'orange':
                canvas.move(projectiles[i], -speedorange, 0)
        for i in range(len(projectiles)):
            p = canvas.coords(player2)
            coll = canvas.find_overlapping(p[0], p[1], p[2], p[3])
            coll = list(coll)
            coll.remove(player2)
            if len(coll) != 0:
                coll.clear()
                nothit = False
                break
        sleep(0.01)
        window.update()
    if paused:
        pass
    else:
        if not nothit:
            dead = deal_with_hit(canvas)
            if dead:
                pass
            else:
                clear_projectiles(projectiles, canvas)
        else:
            current_score = current_score + (len(projectiles) * 8)
            try:
                game_sequence(canvas, player2)
            except BaseException:
                pass


def addtoleaderboard():
    global name
    global current_score
    try:
        name = name.strip('\n')
    except BaseException:
        pass
    if name == "":
        name = "Anon"
    try:
        with open("leaderboard.txt", "a") as f:
            f.write(name + " " + str(current_score) + '\n')
            f.close
    except BaseException:
        pass

# Function to sort leaderboards


def sortleaderboard():
    try:
        with open("leaderboard.txt", "r") as f:
            lines = sorted(iter(f), key=lambda x: int(x.partition(" ")[-1]))
            lines.reverse()
    except BaseException:
        pass

    try:
        with open('leaderboard.txt', 'w') as f:
            for x in lines:
                f.write(x)
            f.close()

    except BaseException:
        pass

# Uses left click event to get mouse cooridnates


def teleport(sprite, canvas, event):
    global current_dash
    global paused
    global name
    if current_dash < 1 and name != "Ninja":
        pass
    else:
        x, y = event.x, event.y
        coordtuple = canvas.bbox(sprite)
        xval = -(coordtuple[0] - coordtuple[2])
        yval = -(coordtuple[1] - coordtuple[3])
        if paused:
            pass
        else:
            #x = window.winfo_pointerx()
            #y = window.winfo_pointery()
            canvas.moveto(sprite, x - (xval / 2), y - (yval / 2))
            window.update()
        try:
            name = name.strip('\n')
        except BaseException:
            pass
        if name != "Ninja":
            current_dash = current_dash - 1
        dash = Label(
            window,
            text="Dash:{}".format(current_dash),
            font=(
                'consolas',
                40),
            bg="#000000",
            fg="#b3ffff")
        dash.place(x=1000, y=0)
        window.update()


def move_left(sprite, canvas):
    global paused
    if paused:
        pass
    else:
        x = -20
        y = 0
        p = canvas.coords(sprite)
        if (p[0] + x) < 0:
            pass
        else:
            canvas.move(sprite, x, y)


def move_right(sprite, canvas):
    global paused
    if paused:
        pass
    else:
        x = 20
        y = 0
        p = canvas.coords(sprite)
        if (p[2] + x) > 1280:
            pass
        else:
            canvas.move(sprite, x, y)


def move_up(sprite, canvas):
    global paused
    if paused:
        pass
    else:
        x = 0
        y = -20
        p = canvas.coords(sprite)
        if (p[1] + y) < -20:
            pass
        else:
            canvas.move(sprite, x, y)


def move_down(sprite, canvas):
    global paused
    if paused:
        pass
    else:
        x = 0
        y = 20
        p = canvas.coords(sprite)
        if (p[3] + y) > 660:
            pass
        else:
            canvas.move(sprite, x, y)


global window
window = Tk()
render_menu()
# render_mainagme()
# window.update()
window.mainloop()
