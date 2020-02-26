class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        different_transformations = set()
        for word in words:
            morse_code = ""
            for char in word:
                i = ord(char) - ord('a')
                morse_code += code[i]
            different_transformations.add(morse_code)
        return len(different_transformations)