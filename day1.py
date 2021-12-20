from input_tool import InputTool

def fuel_for_mass(mass):
    return mass // 3 - 2

tool = InputTool()

def part1()->int:
    total_fuel = 0
    lines = tool.input_lines_for_day(1)
    for(i, line) in enumerate(lines):
        fuel = fuel_for_mass(int(line))
        total_fuel +=fuel

    print(total_fuel)

def part2()->int:
    total_fuel = 0
    lines = tool.input_lines_for_day(1)
    for(i, line) in enumerate(lines):
        fuel = fuel_for_mass(int(line))
        total_fuel += fuel
        while fuel > 0:
            fuel = fuel_for_mass(fuel)
            if fuel > 0:
                total_fuel += fuel
    print(total_fuel)

part2()

