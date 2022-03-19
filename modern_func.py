import sqlite3 as sql


def modern_func(text_func):
    con = sql.connect('data_base.db')
    cur = con.cursor()
    input_text_funcs = cur.execute('''SELECT input_func, output_func FROM MathGrammar''').fetchall()
    con.close()
    for x, y in input_text_funcs:
        text_func = text_func.replace(x, y)

    con.close()
    return text_func.strip()


if __name__ == '__main__':
    pass
