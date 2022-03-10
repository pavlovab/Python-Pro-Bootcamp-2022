# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


import pandas

alphabet_dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")

def genereate_phonetic():
    word = input("Enter a word: ").upper()
    alphabet_dict = {row.letter:row.code for (index, row) in alphabet_dataframe.iterrows()}

    try:
        phonetic_list = [alphabet_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        genereate_phonetic()
    else:
        print(phonetic_list)

genereate_phonetic()