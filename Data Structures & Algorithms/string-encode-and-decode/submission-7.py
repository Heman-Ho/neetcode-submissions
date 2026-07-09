class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        new_string = []
        for string in strs:
            new_string.append(str(len(string)))
            new_string.append("#")
            new_string.append(string)
            
        return "".join(new_string)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s): 
            # Get the cur word length by iterating until we hit a '#' char
            word_len_start_i = i
            while s[i] != '#':
                i += 1
            cur_word_len = int(s[word_len_start_i:i])

            # Move the pointer to point to the start of the desired string (instead of the trailing '#')
            i += 1

            # Use the extracted word length to add the string to the res list
            res.append(s[i:i+cur_word_len])

            # Move pointer to point to the next number which represents the len of the next word
            i += cur_word_len
            
        return res

