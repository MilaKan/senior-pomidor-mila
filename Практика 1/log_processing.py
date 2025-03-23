def main():

    log_input = input("Введите строку лога: ")
    cleaned_log = log_input.strip()
    processed_log = cleaned_log.replace("Ошибка", "Ошибка критическая")

    words = processed_log.split()

    print("Обработанная строка:", processed_log)
    print("Разбитый текст:", words)

if __name__ == "__main__":
    main()