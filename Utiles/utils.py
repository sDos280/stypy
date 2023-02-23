iota_counter = 0


# https://www.youtube.com/watch?v=8QP2fDBIxjM&list=PLpM-Dvs8t0VbMZA7wW9aR3EtBqe2kinu4&ab_channel=TsodingDaily
def iota(reset: bool = False) -> int:
    if not reset:
        global iota_counter
        result = iota_counter
        iota_counter += 1
        return result
    else:
        iota_counter = 0
        return 0
