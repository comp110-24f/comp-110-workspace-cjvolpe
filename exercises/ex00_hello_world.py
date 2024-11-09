def view(my_list: list[str]):
    idx: int = 0
    while idx < len(my_list):
        print(my_list[idx])
        idx += 1


msg: list[str] = ["Hello", "World"]
view(msg)
