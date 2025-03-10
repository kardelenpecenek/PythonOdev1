#Lütfen length_of_longestargümanı olarak bir dizi dize alan isimli bir fonksiyon yazınız.
#  Fonksiyon en uzun dizenin uzunluğunu döndürür.
def length_of_longest(lst):
    # Use the max function to find the longest string based on length
    return len(max(lst, key=len))

# Example usage:
my_list = ["first", "second", "fourth", "eleventh"]
result = length_of_longest(my_list)
print(result)  # 8

my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
result = length_of_longest(my_list)
print(result)# 7