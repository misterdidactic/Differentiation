import re

def derive(f):
    print("expression:", f)
    # remove all spaces
    f = "".join(f.split(" "))
    # create a list of addition/subtraction operators to be re-inserted at the end
    operators = re.findall(r"[+-]", f)
    # split the polynomial into a list of its component parts/"segments"
    f = re.split(r"[+-]", f)
    # create empty string to hold the derivative/result
    derived = ""

    # iterate over list of segments
    for segment in f:
        # if it's an exponent
        if "^" in segment:
            # separate the base from the exponent
            base, exp = segment.split("^")
            # if the base isn't just "x" then multiply the number part by the exponent
            if len(base) > 1:
                derived += str(int(exp)*int(base[:-1])) + base[-1:]
            else:
                # otherwise just concat the exponent and base i.e. x^2 -> 2x
                derived += exp+base
            # if the exponent is greater than 2 then reduce it by 1
            if int(exp) > 2:
                derived += "^{}".format(int(exp) - 1)
            # if the polynomial is not yet finished, add the next operator to the derived string
            if len(operators) > 0:
                derived += " {} ".format(operators[0])
                # remove that operator from the list
                operators = operators[1:]
        # if this segment is not an exponent
        else:
            # if it contains an "x"
            if "x" in segment:
                # if it *only* contains an x, reduce it to 1
                if segment == "x":
                    base = "1"
                # if it's 2x or 501x, reduce it to 2 or 501
                else:
                    base = segment[:-1]
                # add to the derived string
                derived += base
                # if the polynomial is not yet finished, add the next operator to the derived string
                if len(operators) > 0:
                    derived += " {} ".format(operators[0])
                    # remove that operator from the list
                    operators = operators[1:]

    # in case the derived string ends with an operator and no operand
    # remove the last operator
    derived = derived.strip()
    if derived.endswith("+") or derived.endswith("-"):
        derived = derived[:-1]
        derived = derived.strip()

    print("derived:", derived)
    return derived

if __name__ == "__main__":
    f = "x^2 + 2x + 3"
    f = derive(f)
    f = "x^3 - 1"
    f = derive(f)
    f = "6x^9 + 12x^2 - 4"
    f = derive(f)
    f = "2x^6 + x^5 + x + 2"
    f = derive(f)
