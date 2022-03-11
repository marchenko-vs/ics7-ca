import sys
import interpolation as inpln


def main():
    main_table = inpln.get_table()
    inpln.print_all_tables(main_table)

    return_code, n_x, n_y, n_z, x, y, z = inpln.get_data(len(main_table))

    if return_code == inpln.EXIT_FAILURE:
        sys.exit(inpln.EXIT_FAILURE)

    result = inpln.triple_interpolation(main_table, n_x, n_y, n_z, x, y, z)

    print("Interpolation table")

    for i in range(1, 4):
        table_interpolation = [[0] * 3 for i in range(3)]

        for j in range(1, 4):
            for k in range(1, 4):
                table_interpolation[j - 1][k - 1] = inpln.triple_interpolation(
                    main_table, k, j, i, x, y, z)

        print(f'N_Z = {i}')
        inpln.print_table(table_interpolation, None)

    print("Interpolation result = {:.3f}".format(result))


if __name__ == '__main__':
    main()
