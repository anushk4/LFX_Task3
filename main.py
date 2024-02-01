if __name__ == "__main__":
    # Main function
    try:
        # Input format: 1 2 3 4 5...
        array = list(map(int,input("Enter your list as space-separated values: ").split()))
        """
        Displays error: invalid literal for int() with base 10: {str}
        if non-integer values are entered
        """

        # Error handling to check length of array
        if len(array) % 10 != 0:
            raise ValueError("Error: List length must be a multiple of 10.")
        
        # 1-based indexing
        # Skipping values at position of multiples of 2 and 3
        result = [item for index, item in enumerate(array) if (index + 1) % 2 != 0 and (index + 1) % 3 != 0]
        print("Output List: ",result)
        
    # Action when ValueError is encountered
    except ValueError as e:
        print(str(e))

    # Handling miscellaneous errors
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
