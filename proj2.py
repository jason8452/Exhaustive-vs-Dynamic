def exhaustive_best(limit, stock_values):
    # sorting the values of each stock in order of value
    stock_values.sort(key=lambda x: x[1], reverse=True)
    selected_stocks = []  # stores the select stocks (for later when outputting)
    total_value = 0  # stores the values of the selected stocks (also for outputting)
    # goes through all the stocks and checks for if they're in the limit and not outside the boundaries
    for stock in stock_values:
        if stock[1] <= limit:
            selected_stocks.append(stock)
            limit -= stock[1]
            total_value += stock[1]
    return total_value, selected_stocks

def dynamic_best(limit, stock_values):
    #  to store results
    dp = [[0] * (limit + 1) for _ in range(len(stock_values) + 1)]
    # dynamic programming to find max value
    for index in range(1, len(stock_values) + 1):
        for current_limit in range(limit + 1):
            if stock_values[index - 1][1] <= current_limit:
                dp[index][current_limit] = max(
                    dp[index - 1][current_limit],
                    dp[index - 1][current_limit - stock_values[index - 1][1]] + stock_values[index - 1][1]
                )
            else:
                dp[index][current_limit] = dp[index - 1][current_limit]
    selected_stocks = []  # stores the stocks that are chosen
    remaining_limit = limit  # checks what the remaining limit is
    # finding selected stocks
    for index in range(len(stock_values), 0, -1):
        if dp[index][remaining_limit] != dp[index - 1][remaining_limit]:
            selected_stocks.append(stock_values[index - 1])
            remaining_limit -= stock_values[index - 1][1]
    return dp[len(stock_values)][limit], selected_stocks  # returns max val and stocks that were selected (to go to the output of course)

def write_output(file, result):
    # Append the output to a file
    with open(file, 'append') as f:
        f.write(f"Max stock: {result[0]} ") # shows the max stock
        f.write(f"Stocks selected: {result[1]}\n\n") # shows the slected stocks

def main():
    # method did not work trying to pull the sample inputs from input.txt so I did it through the directory
    output_file = r'C:\Users\jayle\Exhaustive-vs-Dynamic\output.txt'
    # Sample Input 1
    N = 4
    Stocks_and_values = [[1, 2], [4, 3], [5, 6], [6, 7]]
    Amount = 12
    # running exhaustive
    part_A = exhaustive_best(Amount, Stocks_and_values)
    write_output(output_file, part_A)
    # running dynamic
    part_B = dynamic_best(Amount, Stocks_and_values)
    write_output(output_file, part_B)

    # Sample Input 2
    N = 4
    Stocks_and_values = [[3, 2], [4, 3], [5, 3], [6, 7]]
    Amount = 10
    # running exhaustive
    part_A = exhaustive_best(Amount, Stocks_and_values)
    write_output(output_file, part_A)
    # running dynamic
    part_B = dynamic_best(Amount, Stocks_and_values)
    write_output(output_file, part_B)

    # Sample Input 3
    N = 3
    Stocks_and_values = [[2, 4], [3, 5], [1, 2]]
    Amount = 8
    # running exhaustive
    part_A = exhaustive_best(Amount, Stocks_and_values)
    write_output(output_file, part_A)
    # running dynamic
    part_B = dynamic_best(Amount, Stocks_and_values)
    write_output(output_file, part_B)

    # Sample Input 4
    N = 5
    Stocks_and_values = [[2, 3], [4, 6], [1, 2], [3, 5], [5, 7]]
    Amount = 15
    # running exhaustive
    part_A = exhaustive_best(Amount, Stocks_and_values)
    write_output(output_file, part_A)
    # running dynamic
    part_B = dynamic_best(Amount, Stocks_and_values)
    write_output(output_file, part_B)

    # Sample Input 5
    N = 2
    Stocks_and_values = [[1, 2], [1, 1]]
    Amount = 3
    # running exhaustive
    part_A = exhaustive_best(Amount, Stocks_and_values)
    write_output(output_file, part_A)
    # running dynamic
    part_B = dynamic_best(Amount, Stocks_and_values)
    write_output(output_file, part_B)

    # Sample Input 6
    N = 3
    Stocks_and_values = [[5, 8], [2, 3], [3, 4]]
    Amount = 10
    # running exhaustive
    part_A = exhaustive_best(Amount, Stocks_and_values)
    write_output(output_file, part_A)
    # running dynamic
    part_B = dynamic_best(Amount, Stocks_and_values)
    write_output(output_file, part_B)

    # Sample Input 7
    N = 4
    Stocks_and_values = [[1, 1], [2, 2], [3, 3], [4, 4]]
    Amount = 8
    # running exhaustive
    part_A = exhaustive_best(Amount, Stocks_and_values)
    write_output(output_file, part_A)
    # running dynamic
    part_B = dynamic_best(Amount, Stocks_and_values)
    write_output(output_file, part_B)

    # Sample Input 8
    N = 5
    Stocks_and_values = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
    Amount = 15
    # running exhaustive
    part_A = exhaustive_best(Amount, Stocks_and_values)
    write_output(output_file, part_A)
    # running dynamic
    part_B = dynamic_best(Amount, Stocks_and_values)
    write_output(output_file, part_B)

    # Sample Input 9
    N = 3
    Stocks_and_values = [[3, 5], [1, 2], [2, 3]]
    Amount = 7
    # running exhaustive
    part_A = exhaustive_best(Amount, Stocks_and_values)
    write_output(output_file, part_A)
    # running dynamic
    part_B = dynamic_best(Amount, Stocks_and_values)
    write_output(output_file, part_B)

    # Sample Input 10
    N = 2
    Stocks_and_values = [[4, 7], [2, 3]]
    Amount = 8
    # running exhaustive
    part_A = exhaustive_best(Amount, Stocks_and_values)
    write_output(output_file, part_A)
    # running dynamic
    part_B = dynamic_best(Amount, Stocks_and_values)
    write_output(output_file, part_B)
