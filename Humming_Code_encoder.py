def hammingEncoder(x):
    # check for valid input
    input_check = list(x)

    if all(char in "01" for char in input_check) and input_check != []:
        new_list = list(x)
        stringlength = len(new_list)
        exp = 0
        powern = 0

        while powern < stringlength:
            powern = 2 ** exp
            exp += 1
            stringlength += 1
            new_list.insert(powern - 1, "*")
        new_list.pop()
        # print("Original list: ", new_list)
        # print()
        steps = 1
        parity_bits = []
        while steps <= len(new_list):
            templist = []
            for i in range(steps - 1, len(new_list), 2 * steps):
                templist.extend(new_list[i: i + steps])
            steps *= 2
            # print("Before parity: ", templist)
            parity_val = 0
            for j in range(1, len(templist)):
                if templist[j] == "1":
                    parity_val += 1

            if parity_val % 2 == 0:
                templist[0] = "0"
                parity_bits.append(templist[0])
            else:
                templist[0] = "1"
                parity_bits.append(templist[0])
        n = 0
        result = ""
        # print(" parity bits", parity_bits)
        for m in range(0, len(new_list)):
            if new_list[m] == "*":
                result += parity_bits[n]
                n += 1
            else:
                result += new_list[m]
        return result

    else:
        return 'Error: Input must be binary!'




print(hammingEncoder("1001"))
