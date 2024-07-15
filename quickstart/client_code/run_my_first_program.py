from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")

    secret_num1 = SecretInteger(Input(name="secret_num1", party=party1))
    secret_num2 = SecretInteger(Input(name="secret_num2", party=party1))

    comparison_result = secret_num1 > secret_num2

    return [Output(comparison_result, "comparison_output", party=party1)]
