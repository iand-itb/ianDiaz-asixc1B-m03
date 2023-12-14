'''
Ian Diaz
8/11/23
ASIXc M03 UF1 A3
Descripció: Detecta si 3 números han estat introduïts en ordre creixent.
'''

nums = input("Introdueix tres números separats per espais: \t").split(" ")
try:

    if int(nums[0])<int(nums[1])<int(nums[2]):
        print("Els números " + str(nums) + " son en ordre ascendent.")
    else:
        print("Els números " + str(nums) + " NO son en ordre ascendent.")

except ValueError:
    print("Introdueix només números.")