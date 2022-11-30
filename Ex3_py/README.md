https://www.codingame.com/ide/puzzle/longest-palindrome

<img width="1106" alt="Screen Shot 2022-11-29 at 17 55 57" src="https://user-images.githubusercontent.com/74509202/204611988-4779e51f-8251-4da4-bc5b-868eb6da3092.png">


def longest(s: str) -> str:
    res = ""
    resLen = 0

    for i in range(len(s)):
        # run in difference of 1 step
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l: r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1

        # run step by step
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l: r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1
    return res, resLen


if __name__ == '__main__':
    a = '23zabaz5'
    print(longest(a))
