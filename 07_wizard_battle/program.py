import random

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
        characters.Dragon('silver dragon', 50, fire_breath=True),
        characters.Wizard('Evil Wizard', 1000),
    ]

    hero = characters.Wizard('Knox', 75)

    # for char in enemies:
    #     print(char)
    #
    # print(hero)

    return enemies, hero


def do_battle(hero, enemy):
    print(f'You attack the {enemy.name}')
    hero_roll = hero.attack_roll()
    print(f'{hero.name} rolls {hero_roll}.')
    enemy_roll = enemy.attack_roll()
    print(f'The {enemy.name} rolls {enemy_roll}.')

    if hero_roll >= enemy_roll:
        print(f'{hero.name} has defeated the {enemy.name}!')
        return True
    else:
        print(f'Our grand hero {hero.name} has been smited!')
        return False



def look():
    pass


def main():
    print_banner()
    enemies, hero = generate_env()
    do_battle(hero, random.choice(enemies))


if __name__ == '__main__':
    main()
