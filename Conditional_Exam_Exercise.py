#CONDITIONAL TEST

#filesystem must have a maximum of 4096 bytes
#if it has 4097 bytes, it will use 4096*2=8192 bytes
#create function that determines how many bits to allocate depending on the file size

def calculate_storage(filesize):
    block_size=4096 #length of the block
    full_blocks=filesize//block_size #this give us the number of blocks, ex,: 0,1,2...
    rest_of_block=filesize%block_size #use % on block size (4096), because and any value that is modulo of 4096 will be 1, except 4096
    if rest_of_block>0: #if whatever value the module is 1, It's because you need another block of 4096
        return block_size*(full_blocks+1) #ex, filesize = 4097, the full block be: 1 (because division floor), the module be 1, 1>0, so blocksize*(1+1)=8192 
    return block_size*full_blocks #ex, 4096, the full block be 1, BUT the module be 0, so 4096*1=4096


# Test the function
print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192