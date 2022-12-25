def sum(num):
    try:
        return int(num) + 5
    except (ValueError, TypeError) as err:
        return err