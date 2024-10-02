# Hard-coded FIRST sets
first_sets = {
    'E': {'(', 'i', 'n'},
    'E\'': {'+', 'e'},
    'T': {'(', 'i', 'n'},
    'T\'': {'*', 'e'},
    'F': {'(', 'i', 'n'},
}

# Hard-coded FOLLOW sets
follow_sets = {
    'E': {')', '$'},
    'E\'': {')', '$'},
    'T': {'+', ')', '$'},
    'T\'': {'+', ')', '$'},
    'F': {'+', ')', '$', '*'}
}

# Hard-coded LL(1) Parsing Table
parsing_table = {
    'E': {
        '(': ['T', 'E\''],
        'i': ['T', 'E\''],
        'n': ['T', 'E\''],
    },
    'E\'': {
        '+': ['+', 'T', 'E\''],
        ')': ['e'],
        '$': ['e'],
    },
    'T': {
        '(': ['F', 'T\''],
        'i': ['F', 'T\''],
        'n': ['F', 'T\''],
    },
    'T\'': {
        '*': ['*', 'F', 'T\''],
        '+': ['e'],
        ')': ['e'],
        '$': ['e'],
    },
    'F': {
        '(': ['(', 'E', ')'],
        'i': ['i'],
        'n': ['n'],
    }
}

# Function to display the tables in a 2D structure
def display_tables_2d():
    # Display FIRST sets
    print("FIRST Sets (2D Structure):")
    first_table = [["Non-terminal", "FIRST"]]
    for non_terminal, first_set in first_sets.items():
        first_table.append([non_terminal, ', '.join(first_set)])

    for row in first_table:
        print(f"{row[0]:<10} | {row[1]}")

    print("\nFOLLOW Sets (2D Structure):")
    follow_table = [["Non-terminal", "FOLLOW"]]
    for non_terminal, follow_set in follow_sets.items():
        follow_table.append([non_terminal, ', '.join(follow_set)])

    for row in follow_table:
        print(f"{row[0]:<10} | {row[1]}")

    print("\nParsing Table (2D Structure):")
    parsing_table_rows = [["Non-terminal", "Terminal", "Production"]]
    for lhs, productions in parsing_table.items():
        for terminal, production in productions.items():
            parsing_table_rows.append([lhs, terminal, ' '.join(production)])

    for row in parsing_table_rows:
        print(f"{row[0]:<10} | {row[1]:<10} | {row[2]}")

# Example usage
if __name__ == "__main__":
    display_tables_2d()
