in_expr = list(input())
op_stack = []
out_expr = []
ops = {'-': 0, '+': 1, '/': 2, '*': 3}
for x in in_expr[::-1]:
    if x in ops.keys():
        while len(op_stack) != 0 and op_stack[-1] != ')' and ops[x] <= ops[op_stack[-1]]:
            out_expr.append(op_stack.pop())
        op_stack.append(x)
    elif x == ')':
        op_stack.append(x)
    elif x == '(':
        while op_stack[-1] != ')':
            out_expr.append(op_stack.pop())
        op_stack.pop()
    else:
        out_expr.append(x)
while len(op_stack) != 0:
        out_expr.append(op_stack.pop())
print(*out_expr[::-1])
