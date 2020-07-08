import random

def init_random_array(number_of_element):
    hidden_array = [0]
    for i in range(number_of_element-1):
        rand = random.randint(i,i*number_of_element)
        hidden_array.append(rand)
        while hidden_array[i+1] < hidden_array[i]:
            rand = random.randint(i,i*number_of_element)
            hidden_array[i+1] = rand
    return hidden_array
