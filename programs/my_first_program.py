from nada_dsl import *

def nada_main():
    # Define parties
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")

    # Define inputs for party1
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Define inputs for party2
    my_int3 = SecretInteger(Input(name="my_int3", party=party2))
    my_int4 = SecretInteger(Input(name="my_int4", party=party2))

    # Perform arithmetic operations
    addition_result = my_int1 + my_int2 + my_int3 + my_int4

    # Provide output
    return [Output(addition_result, "addition_result", party1)]

# Run the NADA program
nada_main()
