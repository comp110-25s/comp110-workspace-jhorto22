def fizzbuzz(n: int) -> str:
    if n % 3 == 0 and n % 5 == 0:
        return "fizzbuzz"
    else:
        if n % 5 == 0 and not n % 3 == 0:
            return "buzz"
        else:
            if n % 3 == 0 and not n % 5 == 0:
                return "fizz"
            else:
                return str(n)
