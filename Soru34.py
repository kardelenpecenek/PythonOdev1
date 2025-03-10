#Lütfen string argümanı alan isimli bir fonksiyon yazınız .
#  Fonksiyon, orijinaliyle aynı olan ancak tüm sesli harfleri kaldırılmış yeni bir dize döndürür.
#Dizenin yalnızca küçük harfli İngiliz alfabesindeki a...z karakterlerini içereceğini varsayabilirsiniz.
def no_vowels(s):
    # Define the vowels to be removed
    vowels = "aeiou"
    # Use a list comprehension to filter out vowels and join the result into a string
    return ''.join([char for char in s if char not in vowels])

# Example usage:
my_string = "bu sn xmpl"
print(no_vowels(my_string))# "bu sn xmpl"