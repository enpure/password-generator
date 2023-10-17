import random

# Строковые константы
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

def get_user_input():
    global chars
    num_passwords = int(input("Количество паролей для генерации: "))
    password_length = int(input("Длину одного пароля: "))
    
    if input("Включать ли цифры 0123456789? (да/нет): ").lower() == 'да':
        chars += digits
    if input("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (да/нет): ").lower() == 'да':
        chars += uppercase_letters
    if input("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (да/нет): ").lower() == 'да':
        chars += lowercase_letters
    if input("Включать ли символы !#$%&*+-=?@^_? (да/нет): ").lower() == 'да':
        chars += punctuation
    if input("Исключать ли неоднозначные символы il1Lo0O? (да/нет): ").lower() == 'да':
        chars = chars.translate(str.maketrans('', '', 'il1Lo0O'))
    
    return num_passwords, password_length

def generate_password(length, chars):
    password = ''.join(random.choice(chars) for i in range(length))
    return password

def main():
    num_passwords, password_length = get_user_input()
    for i in range(num_passwords):
        print(f'Пароль {i+1}: {generate_password(password_length, chars)}')

# Запустить функцию main
if __name__ == "__main__":
    main()
