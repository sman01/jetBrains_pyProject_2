def what_to_do(instructions):
    if instructions.startswith("Simon says"):
        x = "I " + instructions[len("Simon says "):]
        return x.strip()
    elif instructions.endswith("Simon says"):
        x = "I " + instructions[:len(" Simon says")+1]
        return x.strip()
    else:
        return "I won't do it!"

