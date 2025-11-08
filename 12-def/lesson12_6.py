def show_info(**info):
    for key, value in info.items():
        print(key, "=", value)


show_info(name="Alice", age=25, country="Japan")
