if __name__ == "__main__":
    try:
        array = list(map(int,input("Enter your list as space-separated values: ").split()))
        if len(array) % 10 != 0:
            raise ValueError("Error: List length must be a multiple of 10.")
        result = [item for index, item in enumerate(array) if (index + 1) % 2 != 0 and (index + 1) % 3 != 0]
        print("Output List: ",result)
        
    except ValueError as e:
        print(str(e))

    except Exception as e:
        print(f"Unexpected error: {str(e)}")
