import heapq
import os
import time
import matplotlib.pyplot as plt
import numpy as np

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def calc_freq(text):
    frequency = {}
    for char in text:
        if not char in frequency:
            frequency[char] = 0
        frequency[char] += 1
    return frequency

def build_heap(frequency):
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)
    return heap

def merge_nodes(heap):
    while(len(heap)>1):
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2

        heapq.heappush(heap, merged)

def build_codes(root, binary_string, codes):
    if(root is None):
        return

    if(root.char is not None):
        codes[root.char] = binary_string
        return

    build_codes(root.left, binary_string + "0", codes)
    build_codes(root.right, binary_string + "1", codes)

def huffman_encoding(text):
    frequency = calc_freq(text)
    heap = build_heap(frequency)
    merge_nodes(heap)

    root = heapq.heappop(heap)
    codes = {}
    build_codes(root, "", codes)

    encoded_text = ""
    for char in text:
        encoded_text += codes[char]

    return encoded_text, root

def decode(encoded_text, root):
    current_node = root
    decoded_text = ""

    for bit in encoded_text:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if(current_node.char is not None):
            decoded_text += current_node.char
            current_node = root

    return decoded_text

def test_time(text):
    # Measure encoding time
    start_time = time.time()
    encoded_text, root = huffman_encoding(text)
    end_time = time.time()
    encode_time = end_time - start_time

    # Measure decoding time
    start_time = time.time()
    decode(encoded_text, root)
    end_time = time.time()
    decode_time = end_time - start_time

    return encode_time, decode_time

# Generate random strings of different lengths
data_lengths = np.linspace(10**4, 10**5, num=50, dtype=int)
encode_times = []
decode_times = []

for length in data_lengths:
    text = ''.join(np.random.choice(['a', 'b', 'c', 'd', 'e'], size=length))
    
    encode_time, decode_time = test_time(text)
    
    encode_times.append(encode_time)
    decode_times.append(decode_time)

plt.figure(figsize=(10, 6))
plt.plot(data_lengths, encode_times, marker='o', label='Encoding')
plt.plot(data_lengths, decode_times, marker='o', label='Decoding')
plt.title('Time Consumption of Huffman Coding and Decoding for Different Data Lengths')
plt.xlabel('Data Sample Length')
plt.ylabel('Time Taken (seconds)')
plt.grid(True)
plt.legend()
plt.show()