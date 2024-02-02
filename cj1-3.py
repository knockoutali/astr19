def cubed(x):
    return x**3 + 8

def main():
    answer = cubed(9)

    print(f"{answer}\n")

    if answer > 27:
        print("YAY!\n")


main()