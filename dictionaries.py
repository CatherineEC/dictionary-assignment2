# First Task: Merge two dict:
def merge_dictionaries (dict1, dict2):
    merged_dict= dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

#Example
dict1 = {"a":1, "b":2, "c":3}
dict2 = {"b":10,"d": 4}
print (merge_dictionaries(dict1,dict2))

# Second Task: Word in a sentence:
def word_count (sentence):
    words= sentence.split (" ")
    count_dict= { }
    for i in range (len(words)):
        count_dict [ words[i]] = count_dict.get (words[i], 0) + 1
    return count_dict

#Example
sentence = 'apple orange banana apple orange apple'
print (word_count(sentence))

# Third Task: Employee's dictionary 
company_employees = {
"Engineering": {
"Alice": {"age": 30, "role": "Software Engineer"},
"Bob": {"age": 28, "role": "DevOps Engineer"}
},
"HR": {
"Charlie": {"age": 35, "role": "HR Manager"}
}
}

#a)Print 
print(company_employees)

#b) Add a new employee "David" in "Engineering" with role "Data Scientist" and age 27
company_employees['Engineering'] ['David'] = {'age': 27, 'role': 'Data Scientist'} 

#c)Count the total number of employees in the company
def count_total_employee(company_employees):
    total = sum(len(department) for department in company_employees .values() )
    return total

print ("Total number of employees: ", count_total_employee(company_employees))

# Fourth Task: 
def reverse_dict (input_dict):
    result = {}
    for key, value in input_dict.items():
        if value not in result:
            result [value]= []
        result [value] .append(key)
    return result 

#Example
input_dict = {"Alice": 10, "Bob": 20, "Charlie": 10, "David": 30}
print (reverse_dict(input_dict))
