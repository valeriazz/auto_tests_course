def test_substring(full_string, substring):
    assert substring in full_string, \
        f"expected '{substring}' to be substring of '{full_string}'"


full_string = input()
substring = input()

test_substring(full_string, substring)
