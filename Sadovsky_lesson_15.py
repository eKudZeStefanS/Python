def count_chars(data):
    if isinstance(data, tuple):
        return sum(len(str(x)) for x in data if isinstance(x, str))
    elif isinstance(data, list):
        letters_count = sum(len([c for c in x if c.isalpha()]) for x in data if isinstance(x, str))
        digits_count = sum(len([c for c in x if c.isdigit()]) for x in data if isinstance(x, str))
        return f"{digits_count} числа, {letters_count} буквы"
    elif isinstance(data, int):
        odd_digits_count = sum(1 for c in str(data) if c.isdigit() and int(c) % 2 != 0)
        return odd_digits_count
    elif isinstance(data, str):
        letters_count = sum(1 for c in data if c.isalpha())
        return letters_count
print(count_chars([1,2,3,'a','bc8?']))
print(count_chars(788))
print(count_chars('788'))
print(count_chars("Hello world"))
print(count_chars(2345))
print(count_chars([9,99,100]))
