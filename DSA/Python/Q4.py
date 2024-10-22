def compress(chars):
   #write your code here
   write = 0
    read = 0
    
    while read < len(chars):
        current_char = chars[read]
        count = 0
        
        while read < len(chars) and chars[read] == current_char:
            read += 1
            count += 1
            
        chars[write] = current_char
        write += 1
        
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1
                
    return write
   
if __name__ == "__main__":
    chars = ['a', 'a', 'b', 'b', 'c', 'c', 'c']
    newSize = compress(chars)
    print("New length:", newSize)
    print(chars[:newSize])
