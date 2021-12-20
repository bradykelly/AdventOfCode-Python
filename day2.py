from input_tool import InputTool

tool = InputTool()
input = tool.clean_split(tool.input_for_day(2, 2019), ",")

def compute(in_strings: list, noun: int, verb: int) -> int:
    input = [int(x) for x in in_strings]
    input[1] = noun
    input[2] = verb
    for i in range(0, len(input), 4):
        if input[i] == 99:
            break
        elif input[i] == 1:
            input[input[i+3]] = input[input[i+1]] + input[input[i+2]]
        elif input[i] == 2:
            input[input[i+3]] = input[input[i+1]] * input[input[i+2]]
    return input[0]

def Part1():
    print(compute(input, 12, 2))
    
Part1()


