class Trie:

    def __init__(self):
        self.children = {}

        

    def insert(self, word: str) -> None:
        curr = self.children

        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        
        curr["#"] = True
        
    def search(self, word: str) -> bool:
        curr = self.children

        for char in word:
            if char not in curr:
                return False
            curr = curr[char]
        
        if "#" in curr:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.children

        for char in prefix:
            if char not in curr:
                return False
            curr = curr[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)