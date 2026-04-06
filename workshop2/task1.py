def unique_substring_len(s):
    if not s:
        return 0
    
    left = 0
    max_len = 0
    symb_set = set() # Множество символов в подстроке от left до right (set реализован на хеш-таблице, поэтому можно использовать его)
    
    for symb in s:
        # сдвиг левой границы (если повторяется символ, удаляем начало строки до этого элемента включительно)
        while symb in symb_set:
            symb_set.remove(s[left])
            left += 1

        symb_set.add(symb)
        max_len = max(max_len, len(symb_set)) 
        
    
    return max_len

print(unique_substring_len("ABCDEBCFGH"))
print(unique_substring_len("abcabcbb"))
print(unique_substring_len("bbbbb"))
print(unique_substring_len("pwwkew"))
