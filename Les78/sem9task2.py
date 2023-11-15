expression = input()
def check(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
ops = {'-': 0, '+': 1, '/': 2, '*': 3}
res = 0
def Calc(expr_s):
    expr = list(expr_s.split())
    num_stack = []
    if check(expr[0]) != True or check(expr[1]) != True:
        res = 'False'
    else:
        for i in range(len(expr)):
            if check(expr[i]) == True:
                num_stack.append(expr[i])
            elif expr[i] == '+' and len(num_stack) >= 2 :
                num_stack.append(str(float(num_stack.pop(-2)) + float(num_stack.pop(-1))))
            elif expr[i] == '-' and len(num_stack) >= 2:
                num_stack.append(str(float(num_stack.pop(-2)) - float(num_stack.pop(-1))))
            elif expr[i] == '*' and len(num_stack) >= 2:
                num_stack.append(str(float(num_stack.pop(-2)) * float(num_stack.pop(-1))))
            elif expr[i] == '/' and len(num_stack) >= 2 and num_stack[-1] != 0 :
                num_stack.append(str(float(num_stack.pop(-2)) / float(num_stack.pop(-1))))
            else:
                res = 'False'
                break
        res = float(num_stack[-1])
    if len(num_stack) != 1:
        res = 'False'
    return res


print(Calc(expression))
