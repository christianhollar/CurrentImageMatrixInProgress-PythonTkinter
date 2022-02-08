import json
import inputWindow

parameter_names = []
parameter_length = 0
data_array = []
data_length = 0
data = []

def uploadjson():
    from findJSON import filename

    global parameter_names
    global parameter_length
    global data_array
    global data_length
    global data

    # 1. Load JSON File

    f = open(filename)

    try:
        data = json.load(f)
    except:
        print("Failure to load json file.")

    # 2. Get Number of Images
    data_length = len(data)
    # 3. Get Number of Parameters
    dct = data[0]['params']
    parameter_length = len(dct)

    # Create Paramater Name Reference Variable For Titles
    for key in dct.keys():
        parameter_names.append(key)

    data_array = []

    # Create Data Matrix
    # Column 1: Image Index (1 - Number of Images)
    # Column 2 + Parameter Length: Corresponding Parameter Values
    # Column 2 + Parameter Length + 1: Temporary Score Placeholder
    # Column 2 + Parameter_Length + 2: Total Score Placeholder

    for i in range(data_length):
        arr = []
        arr.append(i)
        for j in range(parameter_length):
            arr.append(data[i]['params'][parameter_names[j]])
        arr.append(data[i]['filename'])
        arr.append(0)
        arr.append(0)
        data_array.append(arr)

    inputWindow.input_window()