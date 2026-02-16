def adjust_brightness(pixels, amount):
    # Adds the amount to every pixel in the list
    return [p + amount for p in pixels]

def clip_values(pixels):
    # Ensures no pixel is below 0 or above 255
    new_pixels = []
    for p in pixels:
        if p < 0:
            new_pixels.append(0)
        elif p > 255:
            new_pixels.append(255)
        else:
            new_pixels.append(p)
    return new_pixels

def image_pipeline(data, filters):
    """
    data: a list of numbers
    filters: a list of functions
    """
    for filter_func in filters:
        # We take the data, run it through the current filter, 
        # and SAVE the result back into 'data' for the next loop.
        data = filter_func(data)
    
    return data

raw_pixels = [50, 100, 240, 10]

# 2. To make 'adjust_brightness' work in the loop, we need a 
# version that only takes one argument (the pixels). 
# We can use a lambda or a small wrapper:
def brighten(p): return adjust_brightness(p, 30)

# 3. Define our list of filters in the order we want them applied
my_filters = [brighten, clip_values]

# 4. Run the pipeline!
final_image = image_pipeline(raw_pixels, my_filters)

print(f"Original Pixels: {raw_pixels}")
print(f"Processed Pixels: {final_image}")