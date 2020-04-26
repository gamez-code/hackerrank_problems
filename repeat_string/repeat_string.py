def repeatedString(s, n):
    rn = n % len(s)
    tn = n // len(s)

    acum = s.count('a') * tn
    if 'a' in s[:rn]:
        acum += s[:rn].count('a')
    return acum


if __name__ == '__main__':
    s = "bcbccacaacbbacabcabccacbccbababbbbabcccbbcbcaccababccbcbcaabbbaabbcaabbbbbbabcbcbbcaccbccaabacbbacbc"
    n = 649606239668
    print(repeatedString(s, n) == 162401559918)
