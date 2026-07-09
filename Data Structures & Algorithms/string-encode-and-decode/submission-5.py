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
            cur_word = []

            # Get the cur word length by iterating until we hit a '#' char
            word_len_start_i = i
            while s[i] != '#':
                i += 1
            cur_word_len = int(s[word_len_start_i:i])

            # Use the extracted word length to add each string to the res list
            for char_idx in range(cur_word_len):
                i += 1
                cur_word.append(s[i])
            # Move pointer to point to the next number which represents the len of the next word
            i += 1
            res.append("".join(cur_word))
        return res

