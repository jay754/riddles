def num_to_words(n):
    ones = {
        1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine"
    }

    teens = {
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
        16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"
    }

    tens = {
        10: "ten", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
        60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
    }

    hundred = "hundred"
    thousand = "onethousand"

    # Special case for 1000
    if n == 1000:
        return thousand

    words = ""

    if n >= 100:
        words += ones[n // 100] + hundred
        n %= 100  # Reduce n by removing the hundreds place

        if n > 0:
            words += "and"

    if n >= 20:
        # Append the word for the tens place
        words += tens[n // 10 * 10]
        n %= 10  # Reduce n by removing the tens place

    # Handle the teens (11 to 19)
    if 10 < n < 20:
        words += teens[n]

    elif n == 10 or n < 10:
        words += ones[n]

    return words

# Testing the function
print(num_to_words(342))  # "threehundredandfortytwo"
print(num_to_words(115))  # "onehundredandfifteen"
print(num_to_words(105))  # "onehundredandfive"