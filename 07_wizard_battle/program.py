import characters


def print_banner():
    print('-------------------------------------')
    print('           WIZARD BATTLE')
    print('-------------------------------------')
    print()


def generate_env():
    enemies = [
        characters.SmallAnimal('toad', 1),
        characters.SmallAnimal('bat', 3),
        characters.Predator('tiger', 25),
        characters.Predator('bear', 30),
        characters.Dragon('silver dragon', 50),
        characters.Wizard('Evil Wizard', 1000),
    ]

    hero = characters.Wizard('Knox', 75)


def do_battle():



def game_loop():
    pass


def look():
    pass


def main():
    print_banner()
    generate_env()
    game_loop()


if __name__ == '__main__':
    main()
