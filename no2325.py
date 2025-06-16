class Solution:
	def decodeMessage(self, key: str, message: str) -> str:
		# Create a mapping from characters in the key to letters
		char_map = {}
		current_char = 'a'
		
		for char in key:
			if char != ' ' and char not in char_map:
				char_map[char] = current_char
				current_char = chr(ord(current_char) + 1)
		
		# Decode the message using the mapping
		decoded_message = ''.join(char_map.get(char, ' ') for char in message)
		
		return decoded_message

key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
solution = Solution()
decoded_message = solution.decodeMessage(key, message)
print(decoded_message)  # Output: "this is a secret"