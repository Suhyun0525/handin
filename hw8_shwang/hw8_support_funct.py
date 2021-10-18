def order_array(input_array):
    
    for i in range(len(input_array)):
        m_index = i
        for j in range(i, len(input_array)):
            if input_array[j] < input_array[m_index]:
                m_index = j
        input_array[i], input_array[m_index] = input_array[m_index], input_array[i]
        
    return print(input_array)
       