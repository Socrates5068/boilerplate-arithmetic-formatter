def arithmetic_arranger(*problems):
    x = []

    # Control the quantity of problems
    if len(problems[0]) >= 6:
        return "Error: Too many problems."

    # Separate the list
    for i in range(len(problems[0])):
        x.append(problems[0][i].split())

    # Control the input operator
    for i in range(len(x)):
        if x[i][1] != '+' and x[i][1] != '-':
            return "Error: Operator must be '+' or '-'."

    # Control if number isdigit()
    for i in range(len(x)):
        if x[i][0].isdigit() != True or x[i][2].isdigit() != True:
            return "Error: Numbers must only contain digits."

    # Control the length of operands
    for i in range(len(x)):
        if len(x[i][0]) > 4 or len(x[i][2]) > 4:
            return ("Error: Numbers cannot be more than four digits.")

    # Control the second argument
    if len(problems) == 2:

        # Print the first operand
        a = ""
        for i in range(len(x)):
            if i < (len(x) - 1):
                a = a + "  "
                if (len(x[i][2]) - len(x[i][0])) > 0:
                    for j in range(len(x[i][2]) - len(x[i][0])):
                        a = a + " "
                a = a + x[i][0] + "    "
            else:
                a = a + "  "
                if (len(x[i][2]) - len(x[i][0])) > 0:
                    for j in range(len(x[i][2]) - len(x[i][0])):
                        a = a + " "
                a = a + x[i][0] + "\n"

        # Print the second operand
        b = ""
        for i in range(len(x)):
            if i < len(x) - 1:
                b = b + x[i][1] + " "
                if (len(x[i][0]) - len(x[i][2])) > 0:
                    for j in range(len(x[i][0]) - len(x[i][2])):
                        b = b + " "
                b = b + x[i][2] + "    "
            else:
                b = b + x[i][1] + " "
                if (len(x[i][0]) - len(x[i][2])) > 0:
                    for j in range(len(x[i][0]) - len(x[i][2])):
                        b = b + " "
                b = b + x[i][2] + "\n"

        # Print the line
        z = []
        c= ""
        for i in range(len(x)):
            if i < len(x) - 1:
                if len(x[i][0]) > len(x[i][2]):
                    con = 0
                    for i in range(len(x[i][0]) + 2):
                        c = c + "-"
                        # print("-", end="")
                        con += 1
                else:
                    con = 0
                    for i in range(len(x[i][2]) + 2):
                        c = c + "-"
                        # print("-", end="")
                        con += 1
                c = c + "    "
                # print("", end="    ")
                z.append(con)
            else:
                if len(x[i][0]) > len(x[i][2]):
                    con = 0
                    for i in range(len(x[i][0]) + 2):
                        c = c + "-"
                        # print("-", end="")
                        con += 1
                    c = c + "\n"
                    # print("")
                else:
                    con = 0
                    for i in range(len(x[i][2]) + 2):
                        c = c + "-"
                        # print("-", end="")
                        con += 1
                    c = c + "\n"
                    # print("")
                z.append(con)

        # Print the result
        d = ""
        for i in range(len(z)):
            if i < len(z) - 1:
                if x[i][1] == '+':
                    if z[i] - 1 == len(str(int(x[i][0]) + int(x[i][2]))):
                        result = int(x[i][0]) + int(x[i][2])
                        d = d + " " + str(result) + "    "
                    else:
                        result = int(x[i][0]) + int(x[i][2])
                        d = d + "  " + str(result) + "    "
                else:
                    if x[i][2] > x[i][0]:
                        result = int(x[i][2]) - int(x[i][0])
                        for j in range(z[i] - (len(str(result)) + 1)):
                            d = d + " "
                        d = d + "-" + str(result) + "    "
                    else:
                        result = int(x[i][0]) - int(x[i][2])
                        for j in range(z[i] - len(str(result))):
                            d = d + " "
                        d = d + str(result) + "    "
            else:
                if x[i][1] == '+':
                    if z[i] - 1 == len(str(int(x[i][0]) + int(x[i][2]))):
                        result = int(x[i][0]) + int(x[i][2])
                        d = d + " " + str(result) 
                    else:
                        result = int(x[i][0]) + int(x[i][2])
                        d = d + "  " + str(result)
                else:
                    if x[i][2] > x[i][0]:
                        result = int(x[i][2]) - int(x[i][0])
                        for j in range(z[i] - (len(str(result)) + 1)):
                            d = d + " "
                        d = d + "-" + str(result)
                    else:
                        result = int(x[i][0]) - int(x[i][2])
                        for j in range(z[i] - len(str(result))):
                            d = d + " "

        return (a + b + c + d)
    else:

        # Print the first operand
        a = ""
        for i in range(len(x)):
            if i < (len(x) - 1):
                a = a + "  "
                if (len(x[i][2]) - len(x[i][0])) > 0:
                    for j in range(len(x[i][2]) - len(x[i][0])):
                        a = a + " "
                a = a + x[i][0] + "    "
            else:
                a = a + "  "
                if (len(x[i][2]) - len(x[i][0])) > 0:
                    for j in range(len(x[i][2]) - len(x[i][0])):
                        a = a + " "
                a = a + x[i][0] + '\n'

        # Print the second operand
        b = ""
        for i in range(len(x)):
            if i < len(x) - 1:
                b = b + x[i][1] + " "
                if (len(x[i][0]) - len(x[i][2])) > 0:
                    for j in range(len(x[i][0]) - len(x[i][2])):
                        b = b + " "
                b = b + x[i][2] + "    "
            else:
                b = b + x[i][1] + " "
                if (len(x[i][0]) - len(x[i][2])) > 0:
                    for j in range(len(x[i][0]) - len(x[i][2])):
                        b = b + " "
                b = b + x[i][2] + '\n'

        # Print the line
        c = ""
        for i in range(len(x)):
            if i < len(x) - 1:
                if len(x[i][0]) > len(x[i][2]):
                    for i in range(len(x[i][0]) + 2):
                        c = c + "-"
                else:
                    for i in range(len(x[i][2]) + 2):
                        c = c + "-"
                c = c + "    "
            else:
                if len(x[i][0]) > len(x[i][2]):
                    for i in range(len(x[i][0]) + 2):
                        c = c + "-"
                else:
                    for i in range(len(x[i][2]) + 2):
                        c = c + "-"
    
        return (a + b + c)
