import pprint

def find(text):
    elements = {
        "{": [],
        "(": [],
        "[": []
    }
    position = 0
    for value in text:
        print(position, value)        
        match value:
            # open
            case "{":
                elements["{"].append( (value, position) )
            case "(":
                elements["("].append( (value, position) )
            case "[":
                elements["["].append( (value, position) )

            # close
            case "}":
                elements["{"].pop()
            case ")":
                elements["("].pop()
            case "]":
                elements["["].pop()
        position += 1

    return elements


test = "jkjkd[jjd dkdkd][()"
pprint.pprint(find(test))

    