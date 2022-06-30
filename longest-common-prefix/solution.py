def longestCommonPrefix(self, strs) -> str:
    # get current first word
    prefix = strs[0]

    for word in strs:
        # see if there is a whole word match
        while not word.startswith(prefix):
            # if there isn't a match, subtract letter from each world until match
            prefix = prefix[:-1]
    return prefix
