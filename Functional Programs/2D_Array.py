def read_2d_array(data_type, rows, cols):
    array = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if data_type == 'int':
                row.append(int(input(f"Enter integer for position ({i+1}, {j+1}): ")))
            elif data_type == 'float':
                row.append(float(input(f"Enter float for position ({i+1}, {j+1}): ")))
            elif data_type == 'bool':
                row.append(input(f"Enter boolean for position ({i+1}, {j+1}) (True/False): ").strip().lower() == 'true')
        array.append(row)
    return array

def print_2d_array(array):
    for row in array:
        print(row)


def main():
    rows = int(input("Enter the number of rows (M): "))
    cols = int(input("Enter the number of columns (N): "))
    data_type = input("Enter the data type (int, float, bool): ").strip().lower()
    
    if data_type == 'int':
        array = read_2d_array('int', rows, cols)
        print_2d_array(array)
    elif data_type == 'float':
        array = read_2d_array('float', rows, cols)
        print_2d_array(array)
    elif data_type == 'bool':
        array = read_2d_array('bool', rows, cols)
        print_2d_array(array)

if __name__ == "__main__":
    main()
