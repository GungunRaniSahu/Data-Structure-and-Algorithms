#Huffman Coding Implementation
import heapq
from collections import Counter

def build_huffman_tree(freq_map):
    heap = [[freq, char] for char, freq in freq_map.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        heapq.heappush(heap, [left[0] + right[0], [left, right]])
    return heap[0]

def generate_codes(tree, prefix="", codes={}):
    if isinstance(tree[1], str):
        codes[tree[1]] = prefix
    else:
        generate_codes(tree[1][0], prefix + "0", codes)
        generate_codes(tree[1][1], prefix + "1", codes)
    return codes

def huffman_encode(text):
    freq_map = Counter(text)
    tree = build_huffman_tree(freq_map)
    codes = generate_codes(tree)
    return ''.join(codes[char] for char in text), codes

text = "hello"
encoded_text, codes = huffman_encode(text)

print("Original Text:", text)
print("Huffman Codes:", codes)
print("Encoded Text:", encoded_text)
