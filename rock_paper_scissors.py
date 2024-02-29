"""
This is game named rock paper scissors please follow the instructions
"""
import random
def r_p_s():
    """Запрашивает выбор игрока.
    Args:
        None
    Returns:
    str: Выбор игрока.
    """
    print('Добро пожаловать в камень ножницы бумага')
def game_logic():
    """Определяет логику игры.
    Args:
        user_input (str): Выбор игрока.
    Returns:
        result (str): Результат иг
    """
    computer_data = ['камень','ножницы','бумага']
    while True:
        computer_choice =  random.choice(computer_data)
        user_input = input("Введите ваш ход (камень/ножницы/бумага): ")
        if user_input != computer_choice:
            print(f'Вы поставили {user_input} - опонент ставит {computer_choice}\n Вы проигали.\nЕще раз? y/n')
            user_choice =  input()
            if user_choice == 'y':
                continue
            if user_choice == 'n':
                print('Игра закончена.')
                break
        if user_input == computer_choice:
            print(f'Вы поставили {user_input} - опонент ставит {computer_choice}\n Вы выиграли!.')
            break
r_p_s()
game_logic()
