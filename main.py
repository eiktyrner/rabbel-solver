M = 4
N = 4

class TrieNode:
    def __init__(self, text = ''):
        self.text = text
        self.children = dict()
        self.is_word = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()
    
    def __child_words_for(self, node, words):
        if node.is_word:
            words.append(node.text)
        for letter in node.children:
            self.__child_words_for(node.children[letter], words)

    def insert(self, word):
        current = self.root
        for i, char in enumerate(word):
            if char not in current.children:
                prefix = word[0:i+1]
                current.children[char] = TrieNode(prefix)
            current = current.children[char]
        current.is_word = True

   #TODO: Optimera, ord maste vara 3 langa, klipp vid 9 bokstaver
    def find(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return None
            current = current.children[char]
        if current.is_word:
            return current
    
    def starts_with(self, prefix):
        words = list()
        current = self.root
        for char in prefix:
            if char not in current.children:
                return list()
            current = current.children[char]
        self.__child_words_for(current, words)
        return words

def build_dict():
    trie = PrefixTree()
    with open("saol.txt") as my_dict:
        for line in my_dict:
            text = ''.join(letter for letter in line if letter.isalnum())
            trie.insert(text)
    return trie

def isWord(trie, Str):
    if (len(Str) < 3):
        return
    text = Str.lower()
    if (trie.find(text)):
        return Str

def findWordsUtil(words, trie, grid, visited, i, j, Str):
    visited[i][j] = True
    Str = Str + grid[i][j]

    if(isWord(trie, Str)):
        words.add(Str)
    
    row = i - 1
    while row <= i + 1 and row < M:
        col = j - 1
        while col <= j + 1 and col < N:
            if (row >= 0 and col >= 0 and not visited[row][col]):       
                findWordsUtil(words, trie, grid, visited, row, col, Str)
            col +=1
        row+=1

    Str = "" + Str[-1]
    visited[i][j] = False

def findWords(grid):
    trie = build_dict()
    visited = [[False for i in range(N)] for j in range(M)]
    Str = ''
    words = set()
    
    for i in range(M):
        for j in range(N):
            findWordsUtil(words, trie, grid, visited, i, j, Str)
    print (len(words))
    print (words,'\n')

# Read a matrix of letters
if __name__ == "__main__":
    grid = [['H','L','K','R'],
            ['U','V','A','A'],
            ['A','O','A','S'],
            ['A','O','E','G']]

    findWords(grid)
