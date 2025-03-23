def calculate_discount(price, discount):
    if discount < 0 or discount > 100:
        raise ValueError("Скидка должна быть в пределах от 0% до 100%.")
    discount_amount = price * (discount / 100)
    final_price = price - discount_amount
    return round(final_price, 2), round(discount_amount, 2)

def main():
    try:
        price = float(input("Введите сумму покупки: "))
        discount = float(input("Введите размер скидки (в процентах): "))
        final_price, discount_amount = calculate_discount(price, discount)
        print(f"Размер скидки: {discount_amount} руб.")
        print(f"Итоговая сумма к оплате с учётом скидки (округлено): {final_price:.2f}")
    except ValueError :
        print(f"Ошибка: Неккоректная сумма покупки")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()
