def indian_currency_format(num):
    integer, *fraction = str(num).split(".")
    n = len(integer)
    
    if n <= 3:
        formatted = integer
    else:
        last_three = integer[-3:]
        rest = integer[:-3]
        parts = []
        while len(rest) > 2:
            parts.append(rest[-2:])
            rest = rest[:-2]
        if rest:
            parts.append(rest)
        formatted = ",".join(parts[::-1]) + "," + last_three

    return formatted + ("." + fraction[0] if fraction else "")


print(indian_currency_format(123456.7891))
