def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return


    except Exception as e:
        print(e)
        return


    finally:
        print("Hey I am inside of finally") # if we use finally then it always run if we use return code in def function

main()
