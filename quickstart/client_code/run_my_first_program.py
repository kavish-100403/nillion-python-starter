from nada_dsl import *

def nada_main():
    party2 = Party(name="Party2")

    secret_num1 = SecretInteger(Input(name="secret_num1", party=party2))
    secret_num2 = SecretInteger(Input(name="secret_num2", party=party2))

    sum_result = secret_num1 + secret_num2

    return [Output(sum_result, "sum_output", party2)]
