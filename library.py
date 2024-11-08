import hash_table as ht
import dynamic_hash_table

def merge_sort(arr, key=lambda x: x):
    """
    Sorts a list of elements using the merge sort algorithm.
    Supports sorting by a key function for complex objects like tuples.
    
    Args:
        arr (list): List of elements to be sorted
        key (function): Function to extract comparison key (default: identity function)
    
    Returns:
        list: Sorted list of elements
    """
    # Base case: if list has 1 or fewer elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Find the middle point to divide array into two halves
    mid = len(arr) // 2
    
    # Recursively sort the two halves
    left = merge_sort(arr[:mid], key=key)
    right = merge_sort(arr[mid:], key=key)
    
    # Merge the sorted halves
    return merge(left, right, key=key)

def merge(left, right, key=lambda x: x):
    """
    Merges two sorted lists into a single sorted list.
    Uses the key function for comparisons.
    
    Args:
        left (list): First sorted list
        right (list): Second sorted list
        key (function): Function to extract comparison key
    
    Returns:
        list: Merged sorted list
    """
    result = []
    left_idx, right_idx = 0, 0
    
    # Compare elements from both lists and merge them in sorted order
    while left_idx < len(left) and right_idx < len(right):
        # Apply key function and convert to lowercase if string
        left_key = key(left[left_idx])
        right_key = key(right[right_idx])
        
        # # Convert to lowercase if strings for case-insensitive comparison
        # if isinstance(left_key, str) and isinstance(right_key, str):
        #     left_key = left_key.lower()
        #     right_key = right_key.lower()
            
        if left_key <= right_key:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    
    # Add remaining elements from left list, if any
    result.extend(left[left_idx:])
    
    # Add remaining elements from right list, if any
    result.extend(right[right_idx:])
    
    return result


class DigitalLibrary:
    # DO NOT CHANGE FUNCTIONS IN THIS BASE CLASS
    def __init__(self):
        pass
    
    def distinct_words(self, book_title):
        pass
    
    def count_distinct_words(self, book_title):
        pass
    
    def search_keyword(self, keyword):
        pass
    
    def print_books(self):
        pass
    
class MuskLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, book_titles, texts):
        self.book_library = []
        
        # Create the book library with pairs of titles and texts
        for i in range(len(book_titles)):
            text_copy = []
            for word in texts[i]:
                text_copy.append(word)
            pair = [book_titles[i], text_copy]
            self.book_library.append(pair)

        # Sort each text list in lexicographical order
        for book in self.book_library:
            book[1] = merge_sort(book[1])

        for book in self.book_library:
            # we have to append to a new list
            temp = []
            for i in range(len(book[1])):
                if(i == len(book[1])-1):
                    temp.append(book[1][i])
                    break
                if(book[1][i] != book[1][i+1]):
                    temp.append(book[1][i])
            book[1] = temp
        # Sort the books by title
        self.book_library = merge_sort(self.book_library, key=lambda x: x[0])
    
    def distinct_words(self, book_title):
        ans = []
        index = self.binary_search(book_title)
        if index != -1:
            words_list = self.book_library[index][1]
            for i in range(len(words_list)):
                ans.append(words_list[i])
        return ans 

    
    def count_distinct_words(self, book_title):
        index = self.binary_search(book_title)
        if index != -1:
            return len(self.book_library[index][1])  # Return the count of distinct words
        return None  # Return None if the book is not found
    
    def search_keyword(self, keyword):
        ans = []
        for i in self.book_library:
            index = self.binary_search_word(i[1],  keyword)
            if(index != -1):
                ans.append(i[0])
        return ans
        pass
    
    def print_books(self):
        for book in self.book_library:
            title = book[0]
            text = book[1] # Assuming this contains the sorted words

            # Create a list to hold distinct words
            distinct_words = []

            # Iterate through the sorted list of words
            for i in range (0,len(text)):
                distinct_words.append(text[i])

            # Format the output for Musk's method (sorted)
            musk_format = " | ".join(distinct_words)

            print(f"{title}: {musk_format}")

    def binary_search(self, book_title):
        left, right = 0, len(self.book_library) - 1
        
        while left <= right:
            mid = left + (right - left) // 2  # Avoids potential overflow

            # Compare mid book title with the target book title
            if self.book_library[mid][0] == book_title:
                return mid  # Book found at index mid
            elif self.book_library[mid][0] < book_title:
                left = mid + 1  # Move right
            else:
                right = mid - 1  # Move left
        
        return -1  # Book not found
    
    def binary_search_word(self, list , keyword):
        left, right = 0, len(list) - 1  # as last is the count 
        
        while left <= right:
            mid = left + (right - left) // 2  # Avoids potential overflow

            # Compare mid book title with the target book title
            if list[mid] == keyword:
                return mid  # Book found at index mid
            elif list[mid] < keyword:
                left = mid + 1  # Move right
            else:
                right = mid - 1  # Move left
        
        return -1  # Book not found
    
class JGBLibrary(DigitalLibrary):
    def __init__(self, name, params):
        super().__init__()
        self.books = dynamic_hash_table.DynamicHashMap(
            "Chain" if name == "Jobs" else 
            "Linear" if name == "Gates" else 
            "Double", params
        )
        self.helper_searchkey = []

    def add_book(self, book_title, text):
        words_set = dynamic_hash_table.DynamicHashSet(self.books.collision_type, self.books.params)
        for word in text:
            words_set.insert(word)
        self.books.insert((book_title, words_set))
        self.helper_searchkey.append(book_title)

    def distinct_words(self, book_title):
        words_set = self.books.find(book_title)
        if self.books.collision_type != "Chain":
            if words_set is None:
                return []
            return [word for word in words_set.table if word]
        else:
            if words_set is None:
                return []
            else:
                ans = []
                for lists in words_set.table:
                    if lists is not None:
                        for i in lists:
                            ans.append(i)
                return ans

    def count_distinct_words(self, book_title):
        words_set = self.books.find(book_title)
        if words_set:
            return words_set.total_elements
        else:
            return 0

    def search_keyword(self, keyword):
        results = []
        for entry in self.helper_searchkey:
            words_set = self.books.find(entry)
            if words_set.find(keyword):
                results.append(entry)
        return results

    def print_books(self):
        for slot in self.books.table:
            if slot:  # if slot is not None
                if self.books.collision_type == "Chain":
                    for book_entry in slot:
                        if isinstance(book_entry, tuple) and len(book_entry) == 2:
                            book_title, words_set = book_entry
                            words = []
                            # Process each word slot in the hash table
                            for word_slot in words_set.table:
                                if word_slot is None:
                                    words.append("<EMPTY>")
                                elif isinstance(word_slot, list):
                                    # Handle chained words
                                    if not word_slot:  # if empty list
                                        words.append("<EMPTY>")
                                    else:
                                        # Convert chain to format: word1 ; word2 ; word3
                                        words.append(" ; ".join(word_slot))
                                else:
                                    words.append(word_slot)
                            
                            # Print book title and words
                            print(f"{book_title}: ", end="")
                            print(" | ".join(words))
                else:  # Linear or Double hashing
                    if isinstance(slot, tuple) and len(slot) == 2:
                        book_title, words_set = slot
                        words = []
                        for word in words_set.table:
                            if word is None:
                                words.append("<EMPTY>")
                            else:
                                words.append(word)
                        formatted_words = " | ".join(words)  # Keep all words including <EMPTY>
                        print(f"{book_title}: {formatted_words}")
                    
