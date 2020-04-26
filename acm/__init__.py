def acmTeam(topic):
    maximal = 0

    for i in range(len(topic)):
        aux = topic[i]
        for j in range(i + 1, len(topic)):
            top = topic[j]
            aux_2 = sum([1 if aux[i] == '1' or top[i] == '1' else 0 for i in range(len(topic[0]))])
            if maximal < aux_2:
                num_top = 0
                maximal = aux_2
            if maximal == aux_2:
                num_top += 1

    return maximal, num_top


if __name__ == '__main__':
    topic = ['10101', '11100', '11010', '00101']
    print(acmTeam(topic))
