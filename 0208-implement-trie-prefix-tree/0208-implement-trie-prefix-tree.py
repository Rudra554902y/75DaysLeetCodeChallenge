class Trie:

    def __init__(self):
        self.root={}

    def insert(self, word: str) -> None:
        curr=self.root
        for letter in word:
            if letter not in curr:
                curr[letter]={}
            curr=curr[letter]
        curr['*']=''

    def search(self, word: str) -> bool:
        curr=self.root
        for letter in word:
            if letter not in curr:
                return False
            curr=curr[letter]
        return "*" in curr

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for letter in prefix:
            if letter not in curr:
                return False
            curr=curr[letter]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)