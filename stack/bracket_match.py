from link_stack import *
def match(test_string:str):
    match_hash = {")":"(","]":"[","}":"{"}
    temp_stack = LinkStack()
    for i in test_string:
        if i in ["(","[","{"]:
            temp_stack.push(i)
        if i in [")","]","}"]:
            if match_hash[i] == temp_stack.show_top:
                temp_stack.pop()
            else:
                temp_stack.push(i)
        # else:
        #     temp_stack.push(i)
    return temp_stack.is_null

if __name__ == "__main__":
    test_string = "([]){}"
    print(match(test_string))