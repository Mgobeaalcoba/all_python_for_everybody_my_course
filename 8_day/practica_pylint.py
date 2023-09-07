"""
Module with a sum function for everybody
"""

def run() -> None:
    """
    Initial function
    Return: None
    """
    suma : int = sumar(5,7)
    print(suma)


def sumar(numero1: int, numero2: int) -> int:
    """
    Function what receive two numbers and return the sum of boths
    Return: int
    """
    return numero1 + numero2


if __name__ == '__main__':
    run()


"""
Resultao final de revisión con Pylint: 

C:\Users\mgobea\Documents\develop\python_total\8_day(main -> origin)
(venv) λ pylint practica_pylint.py -r y


Report
======
7 statements analysed.

Statistics by type
------------------

+---------+-------+-----------+-----------+------------+---------+
|type     |number |old number |difference |%documented |%badname |
+=========+=======+===========+===========+============+=========+
|module   |1      |1          |=          |100.00      |0.00     |
+---------+-------+-----------+-----------+------------+---------+
|class    |0      |NC         |NC         |0           |0        |
+---------+-------+-----------+-----------+------------+---------+
|method   |0      |NC         |NC         |0           |0        |
+---------+-------+-----------+-----------+------------+---------+
|function |2      |2          |=          |100.00      |0.00     |
+---------+-------+-----------+-----------+------------+---------+



25 lines have been analyzed

Raw metrics
-----------

+----------+-------+------+---------+-----------+
|type      |number |%     |previous |difference |
+==========+=======+======+=========+===========+
|code      |9      |36.00 |9        |=          |
+----------+-------+------+---------+-----------+
|docstring |11     |44.00 |8        |+3.00      |
+----------+-------+------+---------+-----------+
|comment   |0      |0.00  |NC       |NC         |
+----------+-------+------+---------+-----------+
|empty     |5      |20.00 |4        |+1.00      |
+----------+-------+------+---------+-----------+



Duplication
-----------

+-------------------------+------+---------+-----------+
|                         |now   |previous |difference |
+=========================+======+=========+===========+
|nb duplicated lines      |0     |0        |0          |
+-------------------------+------+---------+-----------+
|percent duplicated lines |0.000 |0.000    |=          |
+-------------------------+------+---------+-----------+



Messages by category
--------------------

+-----------+-------+---------+-----------+
|type       |number |previous |difference |
+===========+=======+=========+===========+
|convention |0      |2        |2          |
+-----------+-------+---------+-----------+
|refactor   |0      |0        |0          |
+-----------+-------+---------+-----------+
|warning    |0      |0        |0          |
+-----------+-------+---------+-----------+
|error      |0      |0        |0          |
+-----------+-------+---------+-----------+



Messages
--------

+-----------+------------+
|message id |occurrences |
+===========+============+




-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 7.14/10, +2.86)
"""