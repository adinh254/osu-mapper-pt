
def isKthBitSet(n, k): # k starts at 0
    if n & (1 << (k)):
        return True
    else:
        return False


with open('../files/REDALiCE - Pekorap Tropical House Remix (Yuuma) [Universal Daikaiten Peko Peko no Mai].osu', 'r', encoding="utf8") as file:

    for line in file:
        if "HitObjects" in line:
            break

    circle_count = 0
    slider_count = 0
    for line in file:
        line_data = line.split(',')
        num = int(line_data[3])
        if isKthBitSet(num, 0):
            circle_count += 1
        elif isKthBitSet(num, 1):
            slider_count += 1
    print(circle_count, slider_count)


