def guessNumber():
    low, high = 1, 1000
    print("Think of a number between 1 and 1000 and I will try to guess it.")
    while low <= high:
        mid = low + (high - low) // 2
        print(f"Is your number {mid}? (Enter 'higher', 'lower', or 'yes')")
        response = input().lower()
        if response == 'yes':
            print("Hooray! I've guessed your number.")
            break
        elif response == 'lower':
            high = mid - 1
        elif response == 'higher':
            low = mid + 1
        else:
            print("Invalid response. Please enter 'higher', 'lower', or 'yes'.")

guessNumber()