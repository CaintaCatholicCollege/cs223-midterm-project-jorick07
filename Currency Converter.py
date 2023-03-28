def main():
    import sys
    choice = 0
    PHP = 0.0
    USD = 0.0
    CNY = 0.0
    HKD = 0.0
    CAD = 0.0
    JPY = 0.0
    EURO = 0.0
    quit = '\0'
    power = '\0'
    while quit != 'z':
        print("Select an currency that you want to convert from Philippine Peso.")
        print("\n 1: US Dollar ")
        print("\n 2: Euro ")
        print("\n 3: HongKong Dollar")
        print("\n 4: Chinese Yuan ")
        print("\n 5: Canadian Dollar ")
        print("\n 6: Japanese Yen ")
        print("\n 7: Exit")
        print("\n Enter the choice:")
        choice = int(input())

        if choice == 1:
            print("\nEnter How Many Peso You want To Convert: ")
            PHP = float(input())
            USD = PHP * 0.019
            print(PHP, "Peso convert into: ",USD)

        if choice == 2:
            print("\nEnter How Many Peso You want To Convert: ")
            PHP = float(input())
            EURO = PHP * 0.01
            print(PHP, "Peso convert into: ",EURO)

        if choice == 3:
            print("\nEnter How Many Peso You want To Convert: ")
            PHP = float(input())
            HKD = PHP * 0.15
            print(PHP, "Peso convert into: ",HKD)

        if choice == 4:
            print("\nEnter How Many Peso You want To Convert: ")
            PHP = float(input())
            CNY = PHP * 0.12
            print(PHP, "Peso convert into: ",CNY)

        if choice == 5:
            print("\nEnter How Many Peso You want To Convert: ")
            PHP = float(input())
            CAD = PHP * 0.02
            print(PHP, "Peso convert into: ",CAD)

        if choice == 6:
            print("\nEnter How Many Peso You want To Convert: ")
            PHP = float(input())
            JPY = PHP * 0.41
            print(PHP, "Peso convert into: ",JPY)

        if choice == 7:
            print("Exiting Program...")
            break
if __name__ == "__main__":
    main()