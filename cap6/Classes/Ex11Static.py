class StringUtil:

    @staticmethod
    def is_palindrome(s, case_insentive=True):
        # we allow only letters and numbers
        #print([c for c in s if c.isalnum()])
        s = ''.join(c for c in s if c.isalnum())
        print(s)
        if case_insentive:
            s = s.lower()
        for c in range(len(s) // 2):
            if s[c] != s[-c - 1]:
                return False
        return True

    @staticmethod
    def get_unique_words(sentence):
        return set(sentence.split())


print(StringUtil.is_palindrome('Radar', case_insentive=False))
print(StringUtil.is_palindrome('A nut for a jar of tuna'))
print(StringUtil.is_palindrome('Never Odd, Or Even!'))
print(StringUtil.is_palindrome('In Girum Imus Nocte Et Consumimur Igni'))
print(StringUtil.get_unique_words('I love palingromes. I really really love them!'))