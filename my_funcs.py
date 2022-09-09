import os, re

def natural_sort(mylist): 
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(mylist, key=alphanum_key)

def my_natsort(your_list):
    def convert(text):
        res = int(text) if text.isdigit() else text.lower()
        return res

    def alphanum_key(key):
        splitted = re.split('([0-9]+)', key)
        res = [convert(c) for c in splitted]
        return res

    sorted_list = sorted(your_list, key=alphanum_key)
    return sorted_list

def to_rgb(hex_color: str):
    """
    Takes a hex color value as an arguement, and returns
    the RGB equivelant of it.

    RETURN VALUE:
    tuple of ints

    NOTE:
    do not include octothorpe in the beginning
    """
    # rgb = (int(hex_color[i:i+2], 16) for i in (0, 2 ,4))

    hex_nums = hex_color.lstrip("#")

    r = int(hex_nums[0:2], 16)
    g = int(hex_nums[2:4], 16)
    b = int(hex_nums[4:6], 16)
    
    return (r, g, b)





list_1 = [['image_', 10, '.png'], ['image_', 2, '.png'],
          ['image_', 5, '.png'], ['image_', 4, '.png'],
          ['image_', 3, '.png'], ['image_', 12, '.png'],
          ['image_', 11, '.png'], ['image_', 1, '.png'],]
list_1.sort()
# print(*list_1, sep='\n')



if __name__ == '__main__':
    color = to_rgb('00404a')
    print(color)
    