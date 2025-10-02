the_day = "Thu"

match the_day:
    case "Mon":
        print("月曜日")
    case "Tue":
        print("火曜日")
    case "Sun":
        print("日曜日")
    case _:
        print("その他")
