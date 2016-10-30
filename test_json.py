import json

def output_to_json(text_to_transfer):
    """
    Function to handle strings to json.
    """

    # with open("text.json", "r") as file:
    #     print(file.readlines())
    with open("text.json", "w") as file:
        json.dump({'text_to_webpage':text_to_transfer}, file, indent=4)
    file.close()

    with open("text.json") as file:
        result = json.load(file)
    file.close()
    # print (type(result))
    # print (result.keys())
    # print (result)
