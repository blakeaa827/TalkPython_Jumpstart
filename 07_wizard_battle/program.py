import random
import time

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
        # characters.Wizard('Evil Wizard', 1000),
    ]

    hero = characters.Wizard('Knox', 75)

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


def look(enemies, hero):
    print()
    print(f'{hero.name} scans the immediate area and sees the following creatures:')
    for enemy in enemies:
        print(f'A(n) {enemy.name} of level {enemy.level}')


def main():
    print_banner()
    enemies, hero = generate_env()
    look(enemies, hero)
    while enemies:
        enemy = random.choice(enemies)
        print()
        print(f'A(n) {enemy.name} jumps out from behind a tree.')
        action = input('What do you do? [A]ttack, [R]un, or [L]ook Around: ').lower().strip()
        if action == 'a':
            if do_battle(hero, enemy):
                enemies.remove(enemy)
            else:
                print(f'{hero.name} flees to recover.')
                time.sleep(5)

        elif action == 'r':
            print(f'{hero.name} runs away to fight another day!')
        elif action == 'l':
            look(enemies, hero)
        elif action == 'q':
            exit(0)
        else:
            print(f'Sorry, I don\'t understand {action}')
    print(f'The Grand Wizard {hero.name} has defeated all of the enemies!  Goodbye!')


if __name__ == '__main__':
    main()
