class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        # Your code here
        self.capacity = capacity
        self.count = 0
        self.contents = [None] * self.capacity

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        # Number of keys stored / capacity
        return self.count / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        http://www.goodmath.org/blog/2013/10/20/basic-data-structures-hash-tables/
        """
        # Your code here
        hash = 5381
        for elem in key:
            hash = (hash * 33) + ord(elem)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here

        # load factor
        lf = self.get_load_factor()

        # if load factor greater than 0.7, double in size
        if lf > 0.7:
            new_size = self.capacity * 2
            self.resize(new_size)

        # if lf < 0.2:
        #     new_size = self.capacity / 2

        #     # if at minimum, resize with min capacity
        #     if new_size <= MIN_CAPACITY:
        #         self.resize(MIN_CAPACITY)

        #     # otherwise, resize like normal
        #     else:
        #         self.resize(new_size)

        index = self.hash_index(key)
        new = HashTableEntry(key, value)
        contents = self.contents[index]

        # if nothing in table at index
        if contents is None:
            # enter new at index
            self.contents[index] = new
            # print(f"head node: {self.head}")

            # Increase count
            self.count += 1

        # breakpoint()

        # if there is already value for key
        else:
            # handle collisions -> check if head node has a next
            # special case - if key matches input key, then update
            # value and don't set a next
            if contents.key == key:
                contents.value = new.value

            else:

                if contents.next is None:
                    # breakpoint()
                    # if head node but no next, make head node's next the new
                    # node
                    contents.next = new
                    self.count += 1

                # otherwise, there is a next, so make a new next
                else:

                    cur = self.contents[index].next
                    cur.next = new
                    self.count += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)

        # if nothing there, return warning
        if not self.contents[index]:
            return "Warning: Key Not Found!"

        # otherwise, check for a next
        else:
            # if there is no next, then delete value
            if not self.contents[index].next:
                self.contents[index].value = None
                # update counter
                self.count -= 1

            # if there is a next, delete value and update node info
            else:
                cur = self.contents[index]
                cur.value = None
                self.contents[index] = cur.next
                self.count -= 1

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)

        # if key not found, return None
        if self.contents[index] is None:
            return None

        # otherwise, there is an index for key, so return value
        else:
            # need to see if key matches
            if self.contents[index].key == key:
                return self.contents[index].value

            # if key doesn't match, check for a next
            else:
                if self.contents[index].next is None:
                    return None

                # if there's a next, return its value
                else:
                    return self.contents[index].next.value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here

        # reset capacity
        self.capacity = new_capacity

        # extract current state of contents
        contents = self.contents

        # redefine self.contents to scale of capacity
        self.contents = [None] * self.capacity

        # iterate through contents -> count to get actual num of nodes
        for i in range(len(contents)):
            cur = contents[i]
            # account for nexts
            # if no next, put cur
            if cur.next:  # > AttributeError: 'NoneType' object has no attribute 'next'
                self.put(cur.next.key, cur.next.value)
                self.put(cur.key, cur.value)
            # otherwise, put next, then self
            else:
                self.put(cur.key, cur.value)


if __name__ == "__main__":

    # ht = HashTable(8)

    # ht.put("key-0", "val-0")
    # ht.put("key-1", "val-1")
    # ht.put("key-2", "val-2")
    # ht.put("key-3", "val-3")
    # ht.put("key-4", "val-4")
    # ht.put("key-5", "val-5")
    # ht.put("key-6", "val-6")
    # ht.put("key-7", "val-7")
    # ht.put("key-8", "val-8")
    # ht.put("key-9", "val-9")

    # return_value = ht.get("key-0")
    # print("key-0 val:", return_value) #> val-0
    # return_value = ht.get("key-1")
    # print("key-1 val:", return_value) #> val-1
    # return_value = ht.get("key-2")
    # print("key-2 val:", return_value) #> val-2
    # return_value = ht.get("key-3")
    # print("key-3 val:", return_value) #> val-3
    # return_value = ht.get("key-4")
    # print("key-4 val:", return_value) #> val-4
    # return_value = ht.get("key-5")
    # print("key-5 val:", return_value) #> val-5
    # return_value = ht.get("key-6")
    # print("key-6 val:", return_value) #> val-6
    # return_value = ht.get("key-7")
    # print("key-7 val:", return_value) #> val-7

    # return_value = ht.get("key-8")
    # print("key-8 val:", return_value) #> val-8
    # return_value = ht.get("key-9")
    # print("key-9 val:", return_value) #> val-9

    # ht = HashTable(0x10000)

    # ht.put("key-0", "val-0")
    # ht.put("key-1", "val-1")
    # ht.put("key-2", "val-2")

    # # breakpoint()

    # ht.put("key-0", "new-val-0")
    # ht.put("key-1", "new-val-1")
    # ht.put("key-2", "new-val-2")

    # return_value = ht.get("key-0")
    # print("key-0 val:", return_value) #> "new-val-0"
    # return_value = ht.get("key-1")
    # print("key-1 val:", return_value) #> "new-val-1"
    # return_value = ht.get("key-2")
    # print("key-2 val:", return_value) #> "new-val-2"

    # ht = HashTable(8)

    # ht.put("key-0", "val-0")
    # ht.put("key-1", "val-1")
    # ht.put("key-2", "val-2")
    # ht.put("key-3", "val-3")
    # ht.put("key-4", "val-4")
    # ht.put("key-5", "val-5")
    # ht.put("key-6", "val-6")
    # ht.put("key-7", "val-7")
    # ht.put("key-8", "val-8")
    # ht.put("key-9", "val-9")

    # ht.put("key-0", "new-val-0")
    # ht.put("key-1", "new-val-1")
    # ht.put("key-2", "new-val-2")
    # ht.put("key-3", "new-val-3")
    # ht.put("key-4", "new-val-4")
    # ht.put("key-5", "new-val-5")
    # ht.put("key-6", "new-val-6")
    # ht.put("key-7", "new-val-7")
    # ht.put("key-8", "new-val-8")
    # ht.put("key-9", "new-val-9")

    # return_value = ht.get("key-0")
    # print("key-0 val:", return_value) #> "new-val-0"
    # return_value = ht.get("key-1")
    # print("key-1 val:", return_value) #> "new-val-1"
    # return_value = ht.get("key-2")
    # print("key-2 val:", return_value) #> "new-val-2"
    # return_value = ht.get("key-3")
    # print("key-3 val:", return_value) #> "new-val-3"
    # return_value = ht.get("key-4")
    # print("key-4 val:", return_value) #> "new-val-4"
    # return_value = ht.get("key-5")
    # print("key-5 val:", return_value) #> "new-val-5"
    # return_value = ht.get("key-6")
    # print("key-6 val:", return_value) #> "new-val-6"
    # return_value = ht.get("key-7")
    # print("key-7 val:", return_value) #> "new-val-7"
    # return_value = ht.get("key-8")
    # print("key-8 val:", return_value) #> "new-val-8"
    # return_value = ht.get("key-9")
    # print("key-9 val:", return_value) #> "new-val-9"

    # print("---" * 10)
    # print(ht.resize(20))

    # ht = HashTable(8)

    # ht.put("key-0", "val-0")
    # ht.put("key-1", "val-1")
    # ht.put("key-2", "val-2")
    # ht.put("key-3", "val-3")
    # ht.put("key-4", "val-4")
    # ht.put("key-5", "val-5")
    # ht.put("key-6", "val-6")
    # ht.put("key-7", "val-7")
    # ht.put("key-8", "val-8")
    # ht.put("key-9", "val-9")

    # ht.resize(1024)
    # print("new_capacity:", ht.get_num_slots()) #> 1024

    # return_value = ht.get("key-0")
    # print("key-0 val:", return_value) #> "new-val-0"
    # return_value = ht.get("key-1")
    # print("key-1 val:", return_value) #> "new-val-1"
    # return_value = ht.get("key-2")
    # print("key-2 val:", return_value) #> "new-val-2"
    # return_value = ht.get("key-3")
    # print("key-3 val:", return_value) #> "new-val-3"
    # return_value = ht.get("key-4")
    # print("key-4 val:", return_value) #> "new-val-4"
    # return_value = ht.get("key-5")
    # print("key-5 val:", return_value) #> "new-val-5"
    # return_value = ht.get("key-6")
    # print("key-6 val:", return_value) #> "new-val-6"
    # return_value = ht.get("key-7")
    # print("key-7 val:", return_value) #> "new-val-7"
    # return_value = ht.get("key-8")
    # print("key-8 val:", return_value) #> "new-val-8"
    # return_value = ht.get("key-9")
    # print("key-9 val:", return_value) #> "new-val-9"

    ht = HashTable(8)

    ht.put("key-0", "val-0")
    ht.put("key-1", "val-1")
    ht.put("key-2", "val-2")
    ht.put("key-3", "val-3")
    ht.put("key-4", "val-4")
    ht.put("key-5", "val-5")
    ht.put("key-6", "val-6")
    # ht.put("key-7", "val-7")
    # ht.put("key-8", "val-8")
    # ht.put("key-9", "val-9")
