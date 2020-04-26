def merge_the_tools(string, k):
    # your code goes here

    for i in range(0, len(string), k):
        aux = list(string[i: i + k])
        acum = []
        for j in aux:
            if j in acum:
                acum.append('')
            else:
                acum.append(j)
        else:
            acum = ''.join(acum)
            print(acum)


if __name__ == '__main__':
    # string, k = input(), int(input())
    with open('data.txt', 'r') as file:
        string, k = file.readlines()
    k = int(k)

    merge_the_tools(string, k)
