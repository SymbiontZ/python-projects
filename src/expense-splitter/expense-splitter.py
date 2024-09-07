def calculate_split(total_amount: float, n_people: int, uneven_split: None | list[float] = None):
    raise NotImplementedError("Not implemented")


def main():
    opt: list [str] = ["Y", "y", "N", "n"]

    while True:
        try:
            total_amount: float = float(input("Enter total amount of the expense: "))

            num_people: int = int(input("Enter the number of people: "))
            if num_people < 2:
                raise ValueError("To split expense need at least 2 people")

            even_split : str = input("Do even split? [y/n]")
            while even_split not in opt:
                even_split = input("Please, enter a valid option: ")

            if even_split == "y" or even_split == "Y":
                calculate_split(total_amount, num_people, )
            else:
                calculate_split(total_amount, num_people)
            break
        except ValueError as e:
            print(f"    Error: {e}\n")
            continue


if __name__ == "__main__":
    main()