"""Check a string has brackets are in correct sequence."""
def is_match_brackets(string):
    """
    Check a string has brackets are in correct sequence.
    Args:
        string: input string
    Return:
        1: string is in correct sequence.
        0: not in correct sequence.
    """
    stack = []    # Use stack method
    map_pair_brackets = {
        ")":"(",
        "]":"[",
        "}":"{",
        ">":"<"
    }

    for char in string:
        # if character is open bracket -> push to stack
        if char in map_pair_brackets.values():
            stack.append(char)
        # if character is close bracket:
        elif char in map_pair_brackets:
            # if top of stack is corresponding open bracket
            if stack[-1] == map_pair_brackets[char]:
                stack.pop()
            else:
                return 0
        else:
            pass

    return 1 if not stack else 0

if __name__ == "__main__":
    result_all_tests = []    # Store value of all test cases
    number_test_cases = int(input("Number of test cases: "))

    while number_test_cases:
        input_string = input()
        validate_result = is_match_brackets(input_string)
        result_all_tests.append(validate_result)
        number_test_cases -= 1

    print(*result_all_tests)
