# ########################################
# Capstone Project
# Submitted: M.N.Abdul-Cader
# Date: 6th November 2018
#
# ########################################
# Project details
# ################
# The implementation of the two data Lists
# from data.py have been created as Hashmaps
# with LinkedList index storage
# The implementation although without syntax
# errors. Does not successfully retrieve data.
# In order to test the working of the rest of program
# an example list was created and hard coded
# as if this was retrieved from the hashmap.
# This is for test purposes only.
# ##########################################

#from trie import Trie
from data import *
from welcome import *
from hashmap import HashMap
from linkedlist import LinkedList


#Printing the Welcome Message

print_welcome()

#Write code to insert food types into a data structure here. The data is in data.py
# populate types into a hash_map

from linkedlist import LinkedList
from data import *

# A Class to store the types data list as a HashMap
class TypeHashMap:
    def __init__(self,size): #,value):
        self.array_size = size
        self.array = [LinkedList() for item in range(self.array_size)]


    def hash(self,key):
        key_bytes = key.encode()
        print("key bytes is {0} for value key {1}".format(key_bytes,key))

        hash_code = sum(key_bytes)
        return hash_code

    def compressor(self, hash_code):
        return hash_code % self.array_size

    def assign(self, value):
        # array index from hashcode calculated from key
        # will be first letter of value
        key = value[0]

        array_index = self.compressor(self.hash(key))

        list_at_array = self.array[array_index]
        payload = Node(value)

        for item in list_at_array:
            if item == key:
                list_at_array.insert_beginning(value)

        list_at_array.insert(payload)

    def retrieve(self,key):
        # array index from hashcode
        array_index = self.compressor(self.hash(key)) # array_index is an integer

        # make current node the head node
        payload = self.array[array_index]
        #current_node = self.head_node
        list_at_index = self.array[array_index]
        display_list = []
        for item in list_at_index:
            if item[0] == key:
                display_list += str(payload.value)
                return
            else:
                return
        return display_list

#Write code to insert restaurant data into a data structure here. The data is in data.py
class RestaurantHashMaps:
        def __init__(self,size):
            self.array_size = size
            self.array = [LinkedList() for item in range(self.array_size)]


        def hash(self,key):
            key_bytes = key.encode()
            print("key bytes is {0} for value key {1}".format(key_bytes,key))

            hash_code = sum(key_bytes)
            return hash_code

        def compressor(self, hash_code):
            return hash_code % self.array_size

        def assign(self, value):
            # array index from hashcode calculated from key
            # will be first letter of value
            key = value[0]

            array_index = self.compressor(self.hash(key))

            list_at_array = self.array[array_index]
            payload = Node(value)

            for item in list_at_array:
                if item == key:
                    list_at_array.insert_beginning(value)

            list_at_array.insert(payload)

        def retrieve(self,key):
            # array index from hashcode
            array_index = self.compressor(self.hash(key)) # array_index is an integer

            # make current node the head node
            payload = self.array[array_index]
            #current_node = self.head_node
            list_at_index = self.array[array_index]
            display_list = []
            for item in list_at_index:
                if item[0] == key:
                    display_list += str(payload.value)
                    return
                else:
                    return
            return display_list



#Write code for user interaction here
while True:
    ''' Test workaround to continue development
        The data hashmaps do not return expected list of food_types
        HardCoded values used for user_input 'i':
        and list_food_type = ['indian' , 'italian']
    '''
    user_input = str(input("\nWhat type of food would you like to eat?\nType the beginning of that food type and press enter to see if it's here.\n")).lower()
    #user_input = 'i'

    #Search for user_input in food types data structure here
    #Search with first letter of user_input
    # Continue until there is only one selection from user_input
    list_food_type =[]
    while list_food_type != 1:
        first_letter = user_input[0]

        # Instantiate a food_type hash map
        types_hash_map = TypeHashMap(len(types))

        # Retrieve the list of all items with first letter per user input
        # This does not work as expected, no list is retrieved.
        #list_food_type =types_hash_map.retrieve(first_letter)
        ''' Test workaround to continue development
            HardCoded values for user_input 'i':
                list_food_type = ['indian' , 'italian']
        '''
        list_food_type = ['indian' , 'italian']


        # Compare to user input and Reduce this list of food_type
        # to only items that match other letters in user_input.
        # Display a final list which matches user input
        matched_food_type =[]
        #possible_item = ""
        user_input_length = 0
        for i in range(len(list_food_type)):
            current_item = list_food_type[i]
            if user_input == current_item[0:(len(user_input))]:
                matched_food_type.append(current_item)

            # Check if more than one item in matched food list
            if len(matched_food_type) != 1:
                print("\nWith those beginning letters your choices are {}".format(matched_food_type))
                break
        break
    # Only one  matched

    one_food_choice = str(input("\nThe only option with those beginning letters is {}. Do you want to look at {} restaurants? Enter 'y' for 'yes' or 'n' for 'no' ").format(matched_food_type)).lower()
    if one_food_choice == 'n':
        # go back to request user input
        break

    elif one_food_choice == 'y' :
        # search for restaurant

        # Display restaurant page at a time

        search_again_choice = str(input("\nDo you want to find other restaurants?\n Enter 'y' for 'yes and 'n' for 'no'")).lower()

        if search_again_choice == 'y':
            break
        elif search_again_choice == 'n':
            quit()
        else:
            # 'y' or 'n' not entered
            print("Wrong entry - please enter 'y' or 'n'")
            break
        break
