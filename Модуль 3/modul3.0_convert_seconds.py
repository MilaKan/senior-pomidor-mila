def convert_seconds(second):
    hours = second// 3600
    remaining_seconds = second % 3600
    minuts = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return print(f" В {second} секундах содержится {hours} час(ов) , {minuts} минут и {seconds} секунд.")
convert_seconds(3672)
