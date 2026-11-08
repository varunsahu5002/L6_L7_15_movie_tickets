def _to_int(token):
    """Convert a token to int safely; return None if it isn't a plain ASCII integer."""
    token = token.strip()
    if not token or not token.isascii() or not token.isdigit():
        return None
    try:
        return int(token)
    except ValueError:  # e.g. absurdly long digit strings
        return None


def parse_seat(seat):
    """'H12' -> ('H', 12). Returns None for invalid input."""
    if not isinstance(seat, str):
        return None
    seat = seat.strip()
    if len(seat) < 2 or not (seat[0].isascii() and seat[0].isalpha()):
        return None
    number = _to_int(seat[1:])
    if number is None or number < 1:
        return None
    return seat[0].upper(), number


def total_price(prices_csv):
    """'150,250,400' -> total incl. 18% GST. Returns None for invalid input."""
    if not isinstance(prices_csv, str):
        return None
    prices = [_to_int(p) for p in prices_csv.split(',')]
    if not prices or any(p is None for p in prices):
        return None
    return round(sum(prices) * 1.18, 2)


def average_rating(ratings):
    """'4 5 3' -> 4.0. Ratings must be integers 1-5. Returns None for invalid input."""
    if not isinstance(ratings, str):
        return None
    values = [_to_int(r) for r in ratings.split()]
    if not values or any(v is None or not 1 <= v <= 5 for v in values):
        return None
    return round(sum(values) / len(values), 1)


def main():
    print("==== Running parse_seat ====")
    user_input = input("Enter a seat number (e.g. H12): ")
    result = parse_seat(user_input)
    print("Row and Seat:", result if result is not None else "Invalid seat")

    print("\n==== Running total_price ====")
    user_input = input("Enter ticket prices as CSV (e.g. 150,250,400): ")
    result = total_price(user_input)
    print("Total with GST:", result if result is not None else "Invalid prices")

    print("\n==== Running average_rating ====")
    user_input = input("Enter ratings separated by spaces (e.g. 4 5 3): ")
    result = average_rating(user_input)
    print("Average Rating:", result if result is not None else "Invalid ratings")


if __name__ == "__main__":
    main()
