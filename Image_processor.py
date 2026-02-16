def adjust_brightness(pixels, amount):
    # Add the amount to every pixel in the list
    return [p + amount for p in pixels]

def clip_values(pixels):
    #Filter values in (0-255)
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
        # Take the data, run it through the current filter, 
        # Save the result back into 'data' for the next loop.
        data = filter_func(data)
    
    return data

raw_pixels = [50, 100, 240, 10]

# Make 'adjust_brightness' work in the loop
def brighten(p): return adjust_brightness(p, 30)

#List of filters in the order 
my_filters = [brighten, clip_values]

#Run the pipeline
final_image = image_pipeline(raw_pixels, my_filters)

print(f"Original Pixels: {raw_pixels}")
print(f"Processed Pixels: {final_image}")
