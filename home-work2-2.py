#این برنامه یک عدد سه رقمی در نظر میگیرد. هربار عدد وسط را حدس میزند.
# اگر حدس ما از عدد مورد نظر بیشتر بود بازه حدس را کاهش میدهد.

import random

def generate_random_number():
    """Generates a random three-digit number."""
    while True:
        number = random.randint(100, 999)
        if number % 2 == 0:
            return number

def guess_number(number):
   
    low = 100
    high = 999
    while low <= high:
        mid = (low + high) // 2
        print("Guess:  ", mid)
        if mid == number:
            return mid
        elif mid < number:
            low = mid + 1
        else:
            high = mid - 1

    # If not found
    return None

def main():
    # Generate a random three-digit number
    number = generate_random_number()

    
    guessed_number = guess_number(number)

    if guessed_number is not None:
        print("The number is:", guessed_number)
    
if __name__ == "__main__":
    main()
