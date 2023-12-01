# exhaustive vs dynamic programming
from itertools import combinations

# exhaustive programming
def exhaustive_best(limit, stock_values):
    # best combo and their values of the best combos
    best_stock_combo = None
    best_value = 0

    # trying all the combos
    for subset_size in range(1, len(stock_values) + 1):
        for stock_combo in combinations(stock_values, subset_size):
            # getting the total value of whichever the current combo is
            current_value = sum(stock[1] for stock in stock_combo)

            # sees if the combo is valid and if the value is higher
            if current_value <= limit and current_value > best_value:
                best_stock_combo = stock_combo
                best_value = current_value

    return best_value, best_stock_combo

# dynamic programming
def dynamic_best(limit, stock_values):
    # table for results
    dp_table = [[0] * (limit + 1) for _ in range(len(stock_values) + 1)]

    # dp for the table
    for stock_index in range(1, len(stock_values) + 1):
        for current_limit in range(limit + 1):
            # checks current stock be put in
            if stock_values[stock_index-1][1] <= current_limit:
                # checks to see whether or not it goes in or not
                dp_table[stock_index][current_limit] = max(
                    dp_table[stock_index-1][current_limit],
                    dp_table[stock_index-1][current_limit-stock_values[stock_index-1][1]] + stock_values[stock_index-1][1]
                )
            else:
                # if too high price, skip over it
                dp_table[stock_index][current_limit] = dp_table[stock_index-1][current_limit]

    # selected stocks
    selected_stocks = []
    remaining_limit = limit
    for stock_index in range(len(stock_values), 0, -1):
        if dp_table[stock_index][remaining_limit] != dp_table[stock_index-1][remaining_limit]:
            # current stock goes in the results
            selected_stocks.append(stock_values[stock_index-1])
            remaining_limit -= stock_values[stock_index-1][1]

    return dp_table[len(stock_values)][limit], selected_stocks

# gets the 10 sample inputs from the input.txt file
def read_input(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    N = int(lines[0].split('=')[1].strip())
    stock_values = [list(map(int, line.split(','))) for line in lines[1:N+1]]
    amount = int(lines[N+1].split('=')[1].strip())

    return N, stock_values, amount

# puts the output of it into the output.txt file
def write_output(file, result):
    with open(file, 'w') as f:
        f.write(f"Maximum Value: {result[0]}\n")
        f.write(f"Selected Stocks: {result[1]}\n")

# main
def main():
    input_file = 'input.txt'
    output_file = 'output.txt'

    # reads the input.txt
    N, stock_values, amount = read_input(input_file)

    # exhaustive
    result_A = exhaustive_best(amount, stock_values)
    write_output(output_file, result_A)

    # dynamic
    result_B = dynamic_best(amount, stock_values)
    write_output(output_file, result_B)

if __name__ == "__main__":
    main()
