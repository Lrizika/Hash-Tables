#!/usr/bin/env python

# '''
# Linked List hash table key/value pair
# '''

from collections import namedtuple


class LinkedPair:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None

	def set_pair(self, key, value):
		if self.key == key:
			self.value = value
		elif self.next is not None:
			self.next.set_pair(key, value)
		else:
			self.add_item(key, value)

	def add_item(self, key, value):
		if self.next is None:
			self.next = LinkedPair(key, value)
		else:
			self.next.add_item(key, value)

	def remove_key_return(self, key):
		if self.key == key:
			self = self.next
			return self
		elif self.next is not None:
			self.next = self.next.remove_key_return(key)
			return self
		else:
			raise KeyError(key)

	def get_pair_by_key(self, key):
		if self.key == key:
			return self
		else:
			return self.next.get_pair_by_key(key)

	def __iter__(self):
		cur = self
		while cur is not None:
			yield cur.key, cur.value
			cur = cur.next

	def __str__(self):
		return '{' + ', '.join([f'{k}: {v}' for k, v in self]) + '}'

	def __repr__(self):
		return f'<{self.__class__.__name__}: {str(self)}>'


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

	def __setitem__(self, key, value):
		hashed = self._hash_mod(key)
		if self.storage[hashed] is None:
			self.storage[hashed] = LinkedPair(key, value)
		else:
			self.storage[hashed].set_pair(key, value)

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
		hashed = self._hash_mod(key)
		if self.storage[hashed] is not None:
			self.storage[hashed] = self.storage[hashed].remove_key_return(key)
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
		hashed = self._hash_mod(key)
		if self.storage[hashed] is not None:
			return self.storage[hashed].get_pair_by_key(key).value
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
		self.storage = [None] * new_capacity
		for pair in old_storage:
			if pair is not None:
				for key, value in pair:
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
