def isPalindrome(self, x: int) -> bool:
    # one liner but harder to read
    # return float(x) >= 0 if str(x) == str(x)[::-1] else False
    if str(x) == str(x)[::-1]:
        if float(x) < 0:
            return False
        else:
            return True
    else:
        return False