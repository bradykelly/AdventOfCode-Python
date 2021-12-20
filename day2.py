from input_tool import InputTool

tool = InputTool()
input = tool.clean_split(tool.input_for_day(2, 2019), ",")

input[1] = "12"
input[2] = "2"

op_code_pos = 0
while op_code_pos < len(input):
    op_code = int(input[op_code_pos])
    if op_code == 99:
        break
    pos_1 = int(input[op_code_pos + 1])
    pos_2 = int(input[op_code_pos + 2])
    pos_3 = int(input[op_code_pos + 3])
    if op_code == 1:
        input[pos_3] = str(int(input[pos_1]) + int(input[pos_2]))
    elif op_code == 2:
        input[pos_3] = str(int(input[pos_1]) * int(input[pos_2]))
    op_code_pos += 4

print(input[0])

