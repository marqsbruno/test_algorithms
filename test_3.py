""" Create an algorithm that generates the following random ID pattern: XXXX-AAAA-BBBB-CCCC
Where XXXX, AAAA, BBBB and CCCC patterns are random alphanumeric
The default is a string: "XXXX-AAAA-BBBB-CCCC"
The result must be stored in a variable. For example:
$id = generarId()
id is ~ abc1-bb12-234a-bcc2 """

from random import choice
from string import ascii_letters, digits


def generate_id():
    generate_1 = ''.join([choice(ascii_letters + digits) for i in range(4)])
    generate_2 = ''.join([choice(ascii_letters + digits) for i in range(4)])
    generate_3 = ''.join([choice(ascii_letters + digits) for i in range(4)])
    generate_4 = ''.join([choice(ascii_letters + digits) for i in range(4)])

    id_string = f"{generate_1}-{generate_2}-{generate_3}-{generate_4}"

    return id_string


print(generate_id())
