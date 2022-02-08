import imageDisplay

current_parameters = []

def imagesort(parameter_input):

    from uploadJSON import data_array
    from uploadJSON import parameter_length
    from uploadJSON import data_length

    print(data_array)
    print(parameter_length)
    print(data_length)

    global current_parameters

    current_parameters = parameter_input

    diff_index = parameter_length+2
    score_index = parameter_length+3

    # Scoring Sort
    for i in range(parameter_length):
        for j in range(data_length):
            # Set Score to Null if User Did Not Utilize Parameter
            if(parameter_input[i]==''):
                data_array[j][diff_index] = "null"
                continue
            # Calculate Difference
            input = float(parameter_input[i])
            current = float(data_array[j][i+1])
            diff = abs(input-current)
            data_array[j][diff_index]=diff
        # Sort by Differences
        data_array = sorted(data_array,key=lambda x:x[diff_index])
        added_value = 0
        # Add Scores to Final Column of Data Array
        # Determined by Difference
        for j in range(data_length):
            if(j>0):
                if(data_array[j-1][diff_index]!=data_array[j][diff_index]):
                    added_value = j
            data_array[j][score_index]+=added_value
    # Redefine Data Array
    data_array=sorted(data_array,key=lambda x:x[diff_index])
    imageDisplay.image_display(data_array)