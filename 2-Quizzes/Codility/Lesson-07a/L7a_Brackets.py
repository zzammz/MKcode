# ==========
def L7a_Brackets (p_str):
    #print ("\n----- start: p_str={}".format(p_str))
    len_str = len(p_str)
    if len_str == 0:
        return 1
    stack_list = []
    for ictr in range (0, len_str):
        current_ch = p_str[ictr]
        if current_ch in "([{":
            stack_list.append(current_ch)
            #print ("100: current_ch={}".format(current_ch))
            continue
        if current_ch in ")]}":
            pop_ch = ""
            if len(stack_list) > 0:
                pop_ch = stack_list.pop()
            else:
                return 0
            if current_ch == ")" and pop_ch == "(":
                continue
            if current_ch == "]" and pop_ch == "[":
                continue
            if current_ch == "}" and pop_ch == "{":
                continue
            #print ("here: pop_ch={}  current_ch={}".format(pop_ch, current_ch))  #return 0
            return 0
        else:
            continue
    if len(stack_list) > 0:
        return 0
    if len(stack_list) == 0:
        return 1;

    return 0



def TEST_L7a_Brackets():

    str_1 = ""
    print ("str={}  brackets={}".format(str_1, L7a_Brackets(str_1)))

    str_1 = "()"
    print ("str={}  brackets={}".format(str_1, L7a_Brackets(str_1)))

    str_1 = "[()]"
    print ("str={}  brackets={}".format(str_1, L7a_Brackets(str_1)))

    str_1 = "[[]]"
    print ("str={}  brackets={}".format(str_1, L7a_Brackets(str_1)))

    str_1 = "{[()()]}"
    print ("str={}  brackets={}".format(str_1, L7a_Brackets(str_1)))

    str_1 = "([)()]"
    print ("str={}  brackets={}".format(str_1, L7a_Brackets(str_1)))

    str_1 = "]]"
    print ("str={}  brackets={}".format(str_1, L7a_Brackets(str_1)))

    str_1 = "[["
    print ("str={}  brackets={}".format(str_1, L7a_Brackets(str_1)))
    return


# =========== main
TEST_L7a_Brackets()


