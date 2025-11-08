def base_conversion(base_to, input):
    """A python function to easyly convert a decimal number to a given base like 2, 4, 8 except base 16 and above [for now]."""
    temp = input // base_to
    output = ""
    # a = []
    
    
    while (temp != 0):
        mod = input % base_to
        temp = input // base_to
        output = output + str(mod)
        # a.insert(0, str(mod))
        input = temp
        print({temp, mod, input, output})
        
        
    return print("Conversion result is ", output[::-1], temp)

#Run base_conversion function
base_conversion(2, 8)
base_conversion(8, 100)
# base_conversion(16, 1244)
base_conversion(10, 888)