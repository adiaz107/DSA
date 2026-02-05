
class HashMap:

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.table = [[] for i in range(self.capacity)]
        self.size = 0

    # Our hash function takes the sum of a key's ASCII characters, then mods it by the backing table size
    def hash(self, key):
        h = 0
        for character in key:
            h += ord(character)

        return h % self.capacity

    def get(self, key):
        index = self.hash(key)
        index_chain = self.table[index]

        for curr_key, curr_value in index_chain:
            if key == curr_key:
                return curr_value

        raise Exception(f'Key {key} is not located in the hash map!')

    def put(self, key, value):
        if (self.size + 1) / self.capacity > .6:
            self.resize()

        index = self.hash(key)

        self.table[index].append((key, value))
        self.size += 1

    def delete(self, key):
        index = self.hash(key)
        index_chain = self.table[index]

        for curr_key, curr_value in index_chain:
            if key == curr_key:
                index_chain.remove((curr_key, curr_value))
                self.size -= 1
                return

        raise Exception(f'Key {key} is not located in the hash map!')

    def resize(self):
        # Create a new table, twice the size of old one
        new_capacity = (2 * self.capacity) + 1
        new_table = [[] for i in range(new_capacity)]

        # Get all the pairs from our old backing table
        old_pairs = []
        for chain in self.table:
            for pair in chain:
                old_pairs.append(pair)

        # Make the new table the map's backing table, and add the old pairs back
        self.table = new_table
        self.capacity = new_capacity
        for key, value in old_pairs:
            self.put(key, value)