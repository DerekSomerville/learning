def fizzBuzz(number):
    result = str(number)
    if number % 3 == 0:
        result = "Fizz"
    elif number % 5 == 0:
        result = "Buzz"

    return result

def firstNumbers(highest):
    listOfResults = []
    for counter in range(1,highest+1):
        listOfResults.append(fizzBuzz(counter))
    return listOfResults

if __name__ == "__main__":
    print(firstNumbers(5))
