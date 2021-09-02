# Python calculator for color intervals
# Samuel Buban
# Pixel Federation
# 18.8.2021


from colorsys import hsv_to_rgb, rgb_to_hsv


first, second = [0] * 3, [0] * 3


def SubtractVectors(base, subtractee):

    return [base[i] - subtractee[i] for i in range(len(base))]


def AddVectors(one, two):

    return [one[i] + two[i] for i in range(len(one))]


def MultiplyVectorByNumber(vector, number):

    return [vector[i] * number for i in range(len(vector))]


def SetPoints(one: list, two: list):

    global first, second

    first = one
    second = two


def CalculatePoint(hue=0, saturation=0, value=0):

    global first, second

    vec = SubtractVectors(second, first)

    if hue == first[0] or saturation == first[1] or value == first[2]:
        return first
    
    if hue == second[0] or saturation == second[1] or value == second[2]:
        return second

    if hue != -1:
        length = vec[0]
        distance = hue - first[0]
        coef = float(distance) / float(length)

        saturation = vec[1] * coef + first[1]
        value = vec[2] * coef + first[2]

    elif saturation != -1:
        length = vec[1]
        distance = saturation - first[1]
        coef = float(distance) / float(length)

        hue = vec[0] * coef + first[0]
        value = vec[2] * coef + first[2]

    elif value != -1:
        length = vec[2]
        distance = value - first[2]
        coef = float(distance) / float(length)

        hue = vec[0] * coef + first[0]
        saturation = vec[1] * coef + first[1]

    return [round(hue), round(saturation), round(value)]


def CalculateInterval(splits: int):

    global first, second

    vec = SubtractVectors(second, first)
    coef = 1 / float(splits - 1)
    coef_vec = MultiplyVectorByNumber(vec, coef)
    out = []

    for i in range(splits):
        out.append(AddVectors(first, MultiplyVectorByNumber(coef_vec, i)))

    return [[round(i[0]), round(i[1]), round(i[2])] for i in out]


def HSV_to_RGB(hsv):

    return [round(i * 255) for i in hsv_to_rgb(float(hsv[0])/360, float(hsv[1])/100, float(hsv[2])/100)]

def RGB_to_HEX(rgb):

    return "".join(["0" + hex(i).split("0x")[1] if len(hex(i).split("0x")[1]) == 1 else hex(i).split("0x")[1] for i in rgb])

def RGB_to_HSV(rgb):

    hsl_dec = rgb_to_hsv(float(rgb[0])/255, float(rgb[1])/255, float(rgb[2])/255)

    return [round(hsl_dec[0] * 360), round(hsl_dec[1] * 100), round(hsl_dec[2] * 100)]

def HEX_to_RGB(hex):

    return [int(hex[0:2], 16), int(hex[2:4], 16), int(hex[4:6], 16)]
