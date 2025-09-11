def count(rows):
    stars = [
        (row_num, col_num)
        for row_num, row in enumerate(rows)
        for col_num, char in enumerate(row)
        if char == '+'
        ]

    recs = [
        (top_left, bottom_right)
        for top_left in stars
        for bottom_right in stars
        if top_left[0] < bottom_right[0]
        and top_left[1] < bottom_right[1]
        and is_rect(
            (top_left, bottom_right), rows
            )
        ]

    return len(recs)


def is_rect(diagonals, rows):
    ul, dr = diagonals
    ul_x, ul_y = ul[0], ul[1]
    dr_x, dr_y = dr[0], dr[1]

    return(
        #rows[ul_x][dr_y] == '+'
        #and
        #rows[dr_x][ul_y] == '+'
        all(
            char in "-+"
            for row_num in (ul_x, dr_x)
            for char in rows[row_num][ul_y:dr_y]
            )
        and all(
            rows[row_num][col_num] in "|+"
            for row_num in range(ul_x, dr_x)
            for col_num in (ul_y, dr_y)
            )
        )
