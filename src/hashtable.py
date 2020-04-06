#!/usr/bin/env python

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
		self.storage = [(None, None)] * capacity

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

	def __setitem__(self, key, value):
		bucket = self._hash_mod(key)
		if self.storage[bucket][0] not in (key, None):
			raise KeyError(f'Collision: Key {self.storage[bucket][0]} and {key} both have bucket {bucket}.')
		self.storage[bucket] = (key, value)

	def insert(self, key, value):
		'''
		Store the value with the given key.

		# Part 1: Hash collisions should be handled with an error warning. (Think about and
		# investigate the impact this will have on the tests)

		# Part 2: Change this so that hash collisions are handled with Linked List Chaining.

		Fill this in.
		'''
		try:
			self[key] = value
		except KeyError as e:
			print(e)

	def __delitem__(self, key):
		bucket = self._hash_mod(key)
		if self.storage[bucket][0] == key:
			self.storage[bucket] = (None, None)
		else:
			raise KeyError(key)

	def remove(self, key):
		'''
		Remove the value stored with the given key.

		Print a warning if the key is not found.

		Fill this in.
		'''
		try:
			del self[key]
		except KeyError as e:
			print(e)

	def __getitem__(self, key):
		bucket = self._hash_mod(key)
		if self.storage[bucket][0] == key:
			return self.storage[bucket][1]
		else:
			raise KeyError(key)

	def retrieve(self, key):
		'''
		Retrieve the value stored with the given key.

		Returns None if the key is not found.

		Fill this in.
		'''
		try:
			return self[key]
		except KeyError:
			return None

	def resize(self, new_capacity=None):
		'''
		Doubles the capacity of the hash table and
		rehash all key/value pairs.

		Fill this in.
		'''
		if new_capacity is None:
			new_capacity = self.capacity * 2
		old_storage = self.storage[:]
		self.storage = [(None, None)] * new_capacity
		for key, value in old_storage:
			self[key] = value


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
