import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def is_very_long(password):
    return 2 * (len(password) > 12)


def has_digit(password):
    return 2 * any(char.isdigit() for char in password)


def has_upper_letters(password):
    return 2 * any(char.isupper() for char in password)


def has_lower_letters(password):
    return 2 * any(char.islower() for char in password)


def has_symbols(password):
    return 2 * any(
        (not ch.isalnum()) and (not ch.isspace())
        for ch in password
    )


def main():
    password = input("Введите пароль: ")

    checks = [
        is_very_long,
        has_digit,
        has_upper_letters,
        has_lower_letters,
        has_symbols,
    ]

    score = 0

    for check in checks:
        score += check(password)

    logging.info(f"Рейтинг пароля: {score}")


if __name__ == "__main__":
    main()


