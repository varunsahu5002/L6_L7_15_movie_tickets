from hypothesis import given, strategies as st
from movie_tickets import parse_seat, total_price, average_rating


@given(st.text() | st.none())
def test_parse_seat_no_crash(s):
    try:
        parse_seat(s)
    except Exception as e:
        assert False, f"parse_seat crashed with: {e!r}"


@given(st.text() | st.none())
def test_total_price_no_crash(s):
    try:
        total_price(s)
    except Exception as e:
        assert False, f"total_price crashed with: {e!r}"


@given(st.text() | st.none())
def test_average_rating_no_crash(s):
    try:
        average_rating(s)
    except Exception as e:
        assert False, f"average_rating crashed with: {e!r}"


# ---- extra property checks (correct behaviour on valid input) ----

@given(st.sampled_from("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"),
       st.integers(min_value=1, max_value=10**6))
def test_parse_seat_valid_roundtrip(row, num):
    assert parse_seat(f"{row}{num}") == (row.upper(), num)


@given(st.lists(st.integers(min_value=0, max_value=10**5), min_size=1))
def test_total_price_valid(prices):
    csv = ",".join(map(str, prices))
    assert total_price(csv) == round(sum(prices) * 1.18, 2)


@given(st.lists(st.integers(min_value=1, max_value=5), min_size=1))
def test_average_rating_in_range(ratings):
    result = average_rating(" ".join(map(str, ratings)))
    assert 1 <= result <= 5
