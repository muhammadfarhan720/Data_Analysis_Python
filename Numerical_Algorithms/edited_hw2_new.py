"""
@author: << Muhammad Farhan Azmine >>
"""

# Here are some test values that you can use for Questions 1-2
year1 = 2023   # NOT a leap year
year2 = 2000   # is a leap year
year3 = 2112   # is a leap year
year4 = 2800   # is a Gregorian leap year but NOT a Milankovic leap year
year5 = 2900   # NOT a Gregorian leap year but is a Milankovic leap year

# Here are some test values that you can use for Question 3
roman1 = "MCXIV"   # is a valid Roman numeral
roman2 = "ASDF"    # NOT a valid Roman numeral (fails rule 1)
roman3 = "CCCC"    # NOT a valid Roman numeral (fails rule 2)
roman4 = "MLC"     # NOT a valid Roman numeral (fails rule 3a)
roman5 = "CIL"     # NOT a valid Roman numeral (fails rule 3b)
roman6 = "LLL"     # NOT a valid Roman numeral (fails rule 4)


####################################
# QUESTION 1: GREGORIAN LEAP YEARS
####################################

test_year_greg = year3            # Update this value to test a different year
is_gregorian_leap = False         # You can choose to start this variable as True
                                  # if your implementation requires it

##############################################################################
# Here is where you will write Python code to determine if a year is a 
# Gregorian leap year.  Your code should set the is_gregorian_leap variable to
# True or False depending on the value in test_year.
if(0<test_year_greg<100):

  if((test_year_greg%4)==0 ):
   is_gregorian_leap=True
  else:
   is_gregorian_leap=False
elif(100<=(test_year_greg)<400):
  if(((test_year_greg%4)==0) & ((test_year_greg%100)!=0)):
   is_gregorian_leap=True
  else:
   is_gregorian_leap=False
elif(test_year_greg>=400):
  if(((test_year_greg%4)==0) & ((test_year_greg%100)==0) & ((test_year_greg%400)==0)):
   is_gregorian_leap=True
  elif(((test_year_greg%4)==0) & ((test_year_greg%100)!=0)):
   is_gregorian_leap=True
  else:
   is_gregorian_leap=False







##############################################################################

print("Is", test_year_greg, "a Gregorian leap year?", is_gregorian_leap)




####################################
# QUESTION 2: MILANKOVIC LEAP YEARS
####################################

test_year_milan = year4               # Update this value to test a different year
is_milankovic_leap = False        # You can choose to start this variable as True
                                  # if your implementation requires it

##############################################################################
# Here is where you will write Python code to determine if a year is a 
# Milankovic leap year.  Your code should set the is_gregorian_leap variable to
# True or False depending on the value in test_year.

if(0<test_year_milan<100):
    if(test_year_milan%4==0):
        is_milankovic_leap=True
    else:
        is_milankovic_leap=False

elif(100<=test_year_milan<900):
    if(((test_year_milan%4)==0) & ((test_year_milan%100)!=0)):
        is_milankovic_leap=True
    else:
        is_milankovic_leap=False
elif(test_year_milan>=900):
    if(((test_year_milan % 4) == 0)& ((test_year_milan % 100)==0)& ((test_year_milan%900)==200) ):
        is_milankovic_leap=True
    elif(((test_year_milan % 4) == 0)& ((test_year_milan % 100)==0)& ((test_year_milan%900)==600)):
        is_milankovic_leap=True
    elif(((test_year_milan % 4)==0)&((test_year_milan % 100)!=0)):
        is_milankovic_leap=True
    else:
        is_milankovic_leap=False














##############################################################################

print("Is", test_year_milan, "a Milankovic leap year?", is_milankovic_leap)




####################################
# QUESTION 3: ROMAN NUMERAL
####################################

test_numeral ="IIV" # Update this value to test a different numeral
is_valid_roman = False         # You can choose to start this variable as True
                               # if your implementation requires it

##############################################################################
# Here is where you will write Python code to determine if a Roman numeral 
# represents a valid string.  Your code should set the is_valid_roman variable
# to True or False depending on the value in test_numeral.

all_chars_not_correct=False

for char in test_numeral:
    if char in "IVXLCDM":
        all_chars_not_correct=False

    else:
        all_chars_not_correct = True
        break

##print(all_chars_not_correct)
#repetition_count=test_numeral.count("M")
wrong_char_repeat=False
#print(repetition_count)
#wrong_char_repeat=True
if (all_chars_not_correct==False):
    for char in "VLD":
        repetition_count= test_numeral.count(char)
        if(repetition_count>1):
            wrong_char_repeat=True
            break
        else:
            wrong_char_repeat=False

##print(wrong_char_repeat)

list_repeat_number=[]
list_repeat_chars=[]
not_excessive_right_char=True
# if no_wrong_char_repeat:
#     for char in "IXCM":
#         repetition_count_right_char=test_numeral.count(char)
#         if (1<repetition_count_right_char<4):
#             list_repeat_number.append(repetition_count_right_char)
#             list_repeat_chars.append(char)
#         elif (repetition_count_right_char>=4):
#             not_excessive_right_char=False
#
#
# print(list_repeat_number)
# print(list_repeat_chars)
# print(not_excessive_right_char)


consecutive_overflow = False
prechar=None
count=1

if ((wrong_char_repeat==False) & (all_chars_not_correct==False)):
    for char in test_numeral:
        if char==prechar:
           count += 1
           if count>3:
               consecutive_overflow=True
               break

        else:count=1

        prechar=char

patterns=["IV", "IX", "XL", "XC", "CD", "CM"]

list_roman_digits=["I","V","X","L","C","D","M","T"]

Descending_broke=False

prev_char_new="T"

test_numeral_new=test_numeral


###print(consecutive_overflow)
previous_char_pattern_small=False

if ((consecutive_overflow==False) & (wrong_char_repeat==False) & (all_chars_not_correct==False)):

   for pattern in patterns:
       test_numeral_new=test_numeral_new.replace(pattern,"")
       ##print(test_numeral_new)

   if((len(test_numeral)>2) & (test_numeral_new!="")&(test_numeral.find(pattern)>0)):
       for pattern in patterns:

           if(list_roman_digits.index(test_numeral[test_numeral.find(pattern)-2])<list_roman_digits.index(test_numeral[test_numeral.find(pattern)])):
               ##(test_numeral[test_numeral.find(pattern)])
               previous_char_pattern_small=True
               break
   if((previous_char_pattern_small==False)&(len(test_numeral_new)>1)):

       for char_new in test_numeral_new:

           if(list_roman_digits.index(char_new)>list_roman_digits.index(prev_char_new)):
               Descending_broke=True
               break


           prev_char_new=char_new

##print(Descending_broke)


count=0


roman_numeral_strings = ["II", "III","XX","XXX", "CC", "CCC", "MM", "MMM"]

repeat_str_overflow = False

if((Descending_broke == False) & (consecutive_overflow==False)& (wrong_char_repeat==False) & (all_chars_not_correct==False)&(previous_char_pattern_small==False)):
    for repeats in roman_numeral_strings:
        if (repeats in test_numeral):
            repeat_str_count=test_numeral.count(repeats)
            if(repeat_str_count>1):
                repeat_str_overflow=True
                break


##print(repeat_str_overflow)


larger_after_consecutive=False


if((repeat_str_overflow == False) & (Descending_broke == False) & (consecutive_overflow==False) & (wrong_char_repeat==False) & (all_chars_not_correct==False)&(previous_char_pattern_small==False)):
   for repeats in roman_numeral_strings:
       if(repeats in test_numeral):

           prev_char_numeral=test_numeral[test_numeral.find(repeats)]
           ##print(repeats)
           if(len(test_numeral)>(test_numeral.find(repeats)+len(repeats))):
               next_char = test_numeral[test_numeral.find(repeats)+len(repeats)]

               if(list_roman_digits.index(next_char)>list_roman_digits.index(prev_char_numeral)):
                   larger_after_consecutive=True
                   break




##print(larger_after_consecutive)


repeatable_char_overflow=False

if ((repeat_str_overflow == False) & (Descending_broke == False) & (consecutive_overflow==False) & (wrong_char_repeat==False) & (all_chars_not_correct==False) &(larger_after_consecutive==False)&(previous_char_pattern_small==False)):
    for char in "IXCM":
        repetition_count= test_numeral.count(char)
        if(repetition_count>3):
            repeatable_char_overflow=True
            break
        else:
            repeatable_char_overflow=False

##print(repeatable_char_overflow)
#
# for i in range(len(list_repeat_number)):
#     char_to_check = list_repeat_chars[i]
#     repeat_count = list_repeat_number[i]
#
#     if char_to_check in test_numeral:
#
#         consecutive_pattern = char_to_check * repeat_count
#         #print(consecutive_pattern)
#
#         if consecutive_pattern not in test_numeral:
#             consecutive = False
#             break
#
# if consecutive:
#     print("All characters are used consecutively.")
# else:
#     print("At least one character is not used consecutively.")
#
# print(consecutive)

if((repeat_str_overflow == False) & (Descending_broke == False) & (consecutive_overflow==False) & (wrong_char_repeat==False) & (all_chars_not_correct==False) &(larger_after_consecutive==False)&(previous_char_pattern_small==False)&(repeatable_char_overflow==False)&(test_numeral!="")):
    is_valid_roman=True
#
# print(f"repeat_str_overflow: {repeat_str_overflow}")
# print(f"Descending_broke: {Descending_broke}")
# print(f"consecutive_overflow: {consecutive_overflow}")
# print(f"wrong_char_repeat: {wrong_char_repeat}")
# print(f"all_chars_not_correct: {all_chars_not_correct}")
# print(f"larger_after_consecutive: {larger_after_consecutive}")
# print(f"previous_char_pattern_small: {previous_char_pattern_small}")
# print(f"repeatable_char_overflow: {repeatable_char_overflow}")


##############################################################################

print("Is", test_numeral, "a valid Roman numeral?", is_valid_roman)