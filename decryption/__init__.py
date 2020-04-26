def decryptPassword(s):
    # Write your code here
    num = []
    for i in range(len(s)):
        if s[i].isdigit():
            num.append(s[i])
        elif s[i].isalpha():
            new_string = s[i::].split('*')
            break
    result = ''
    for n in new_string:
        aux = n[:-2] + n[-1] + n[-2]
        for i in range(len(aux)):
            if aux[i].isdigit():
                r = num.pop()
                result += aux[:i] + r + aux[i+1::]
        result += aux
    return result




if __name__ == '__main__':
    s = '51Pa*0Lp*0e'
    print(decryptPassword(s))
