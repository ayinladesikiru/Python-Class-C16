language = input("Enter preferred language: ")
match language:
    case "java":
        print("you are a hardcore programmer")
    case "javascript":
        print("you are a full stack developer")
    case "python":
        print("you are an amazing programmer")
    case _:
        print("if you are learning programming for the first time, learn python")

