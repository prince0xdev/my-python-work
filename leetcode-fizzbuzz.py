def fizzbuzz(n: int) -> list[str] | None:
    
    """Return a string array answer (1-indexed) where:
       Params:
       - n: an integer
       Returns:
       - a list of strings
    """
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return print(result)

fizzbuzz(15)