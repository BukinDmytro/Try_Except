
###
try:
    print("david")
    print(error)
    print("laid")
except:
    print("4")


###
def checker(var_1):
    if type(var_1) != str:
        raise TypeError(f"Sorry, we can't work with {type(var_1)}, we need class 'str'")
    else:
        print(var_1)
first = "1"
checker(first)


###

class BuildingError(Exception):
    def __str__(self):
        return "With so low amount of material, the house cannot be built"

def check_material(amount_of_material , limit_value):
    if amount_of_material > limit_value:
        return "Enough material"
    else:
        raise BuildingError()

print(check_material(299,300))


