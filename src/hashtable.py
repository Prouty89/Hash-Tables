# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity
    # Index capacity will not grow too large


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # Compute index of key using hash function
        index = self._hash_mod(key)
        # If the index is empty, create a new node and add it
        if self.storage[index] is None:
            self.storage[index] = LinkedPair(key, value)
        else:
            current = self.storage[index]
            while current is not None:
                if current.key == key:
                    current.value = value
                    break
                    # A collision occurred, there is a LL of at least one node at this index
                    # iterate to the end of the list and add a new node there.
                else:
                    if current.next is None:
                        current.next = LinkedPair(key, value)
                    else:
                        current = current.next



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        # Compute hash for the key to determine index
        current = self.storage[index]
        # Key not found, return NONE
        if current == None:
            return 'No key found.'
        # If there is only one LinkedPair
        elif current.next is None and current.key == key:
            self.storage[index] = None
        # Otherwise, find the key and remove
        else:
            prevNode = None
            nextNode = current.next
            while current is not None:
                if current.key == key:
                    if prevNode is None:
                        self.storage[index] = nextNode
                    else:
                        if nextNode:
                            prevNode.next = nextNode
                        else:
                            prevNode.next = None
                    break
                else:
                    if current.next is None:
                        return 'No key found'
                    else:
                        prevNode = current
                        current = current.next
                        nextNode = current.next


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # Compute the index of provided key using the hash function
        index = self._hash_mod(key)
        # Go to the bucket for that index
        current = self.storage[index]
        # Return the value of the retrieved node or return NONE
        while current is not None:
            if current.key == key:
                return current.value
            else:
                current = current.next
        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # New buckets to maintain time complexity when hash gets full.
        # Element at [0] remains because we're relying on the KEY in the old array(?)
        self.capacity *= 2
        # Temp var NEW STORAGE
        new_storage = [None] * self.capacity
        # Iterate over the elements on the old storage and insert them into the new_storage
        for i in range(len(self.storage)):
            current = self.storage[i]

            while current is not None:
                index = self._hash_mod(current.key)
                if new_storage[index] is None:
                    new_storage[index] = LinkedPair(current.key, current.value)
                else:
                    new_storage[index].next = LinkedPair(
                        current.key, current.value)
                current = current.next

        self.storage = new_storage



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
