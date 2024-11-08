# Library Management System

This project is developed as part of the COL106 course assignment, which aims to digitize the IIT Delhi library's collection by creating a searchable and efficient data structure system. This system allows users to retrieve distinct words from each book, count their occurrences, and perform keyword-based searches to find relevant books.

## Project Overview

The Library Management System involves processing a large collection of books by analyzing the text, identifying unique words, and storing these words in a hash table. The project supports different hashing techniques (chaining, linear probing, and double hashing) to handle collisions. It also incorporates dynamic resizing for efficient space utilization.

### Background

The IIT Delhi library houses a vast collection of rare books and periodicals, which require digital transformation for improved accessibility. This project not only digitizes the books but also optimizes the system for fast data retrieval by including a compressed dictionary for each book, containing only the words in that specific book. Users can search for books by keywords, providing a powerful tool for digital information management.

### Key Components

- **Hash Table Classes**: Implements `HashSet` and `HashMap` with custom collision handling methods:
  - **Chaining**: Uses linked lists to manage collisions.
  - **Linear Probing**: Handles collisions by sequentially finding the next available slot.
  - **Double Hashing**: Uses a secondary hash function to calculate the probe step.

- **Digital Library Class**: Contains methods to manage book collections, find distinct words, count unique words, search by keywords, and print book details.

- **Hashing Techniques**:
  - **MuskLibrary**: Uses merge sort for lexicographical sorting to find distinct words.
  - **JGBLibrary**: Uses hash tables to optimize storage and retrieval using Jobs (Chaining), Gates (Linear Probing), and Bezos (Double Hashing) methods.

- **Dynamic Resizing**: Resizes the hash tables when the load factor exceeds a certain threshold, ensuring efficient use of memory.

## Project Structure

- `dynamic_hash_table.py`: Implements the dynamic resizing for hash tables.
- `hash_table.py`: Implements the base HashTable class, along with HashSet and HashMap for handling key-value pairs.
- `library.py`: Defines the `DigitalLibrary` class with two child classes, `MuskLibrary` and `JGBLibrary`, each with distinct approaches to handling text data.
- `main.py`: A testing script to verify the functionality of different modules.
- `prime_generator.py`: A helper module for generating prime numbers for resizing (not modifiable).

## Requirements

- **Python**: The project is built from scratch without using Python's built-in `set` or `dictionary` libraries. 
- **Time Complexity**:
  - Insertion: Amortized O(1) for hash tables.
  - Searching: Expected O(1) for hash tables.
  - Sorting (MuskLibrary): O(W log W) for `W` words in a book.

## Usage

To run and test the project:
1. Clone this repository.
2. Navigate to the main directory.
3. Run `main.py` to test functionalities.

## Author

This project is completed by Gurnoor Singh as part of the COL106 course at IIT Delhi.
"""

