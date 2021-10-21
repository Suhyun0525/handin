def order_array(input_array):
    """function that rearranges the numbers in an array in smaller to larger order.\
    Input: An array of number (numbers)
    Output: The array of number rearranged in order (numbers) """
    
    for i in range(len(input_array)):
        m_index = i
        for j in range(i, len(input_array)):
            if input_array[j] < input_array[m_index]:
                m_index = j
        input_array[i], input_array[m_index] = input_array[m_index], input_array[i]
        
    return print(input_array)