import mmh3


class BloomFilter():

	def __init__(self, size, hash_count):
		super().__init__()
		self.byte_array = bytearray(size) 
		self.size = size
		self.hash_count = hash_count

	def __len__(self):
		return self.size

	def __iter__(self):
		return iter(self.byte_array)

	def add(self, item):
		for seed in range(self.hash_count):
			index = mmh3.hash(item, seed) % self.size
			self.byte_array[index] = 1

		return self

	def __contains__(self, item):
		for seed in range(self.hash_count):
			index = mmh3.hash(item, seed) % self.size
			if self.byte_array[index] == 0:
				return False
		return True

	def __str__(self):
		return str(self.byte_array)

def main():
	bloom = BloomFilter(100, 3)
	animals = ['dog', 'cat', 'giraffe', 'fly', 'mosquito', 'horse', 'eagle', 'bird', 'bison', 'boar', 'butterfly', 'ant', 'anaconda', 'bear', 'chicken', 'dolphin', 'donkey', 'crow', 'crocodile']
	for animal in animals:
		print(bloom.add(animal))

	for animal in animals:
		if animal in bloom:
			print(f'{animal} is in bloom filter as expected!')
		else:
			print("some is wrong")

if __name__ == "__main__":
	main()