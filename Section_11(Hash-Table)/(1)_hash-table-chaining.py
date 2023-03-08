# Hash Table
# ===========
# A hash table is a data structure that implements an associative array (for example a dictionary).
# In an associative array, data is stored as a collection of key-value pairs, where
# * Key: Unique integer that is used for indexing the values,
# * Value: Data that are associated with keys.
# The position of the data within the array is determined by applying a hashing algorithm to the key -
# a process called Hashing. The hashing algorithm is called a hash function.
#
# Let k be a key and h(x) be a hash function.
# Here, h(k) will give us a new index to store the element linked with k.
#
# Hash tables enable very efficient searching. In the best case, data can be retrieved from a hash table
# in constant time, so you will find them wherever high performance searching is a requirement. Maintaining
# (adding, updating and deleting) data in a hash table is also very efficient.
#
# Implement Hashing using Chaining method
# Chains are represented using LinkedList
#
# Source: Hash Tables by isaaccomputerscience.org
# URL: https://isaaccomputerscience.org/concepts/dsa_datastruct_hash_table?examBoard=all&stage=all

from linkedlist import LinkedList
class HashChain:
    def __init__(self):
        self.hashtable_size = 10
        self.hashtable = [0] * self.hashtable_size
        for i in range(self.hashtable_size):
            self.hashtable[i] = LinkedList()

    def hashcode(self, key):
        return key % self.hashtable_size

    def insert(self, element):
        i = self.hashcode(element)
        self.hashtable[i].insertsorted(element)

    def search(self, key):
        i = self.hashcode(key)
        return self.hashtable[i].search(key) != -1

    def display(self):
        for i in range(self.hashtable_size):
            print('[', i, ']', end=' ')
            self.hashtable[i].display()
        print()

H = HashChain()
H.insert(54)
H.insert(78)
H.insert(64)
H.insert(92)
H.insert(34)
H.insert(86)
H.insert(28)
H.display()
print('Search Result: ', H.search(54))