# Color study

For the past two weeks, I've been working on recreating multiple color models. Everything is done purely mathematically and in blender (python for HSV gradient calculator).

## Models
I've recreated the RGB model (top), HSV model (middle) and HSL model (bottom).

![all](/Images/all.png)

## Sliders
All of these models support slider adjustements. That means you can choose you only want Red [100-255], Green [0-0], Blue [0-255], Hue [100-150], Saturation [100-100], Value [0-100] or whatever else you'd like to display.

![slider](/Images/slider.png)

![sliders](/Images/sliders.png)

## Cutouts
Since everything is calculated by maths, you can also make cutouts of these models (using booleans), and they will still properly display the color.

![cutouts](/Images/cutouts.png)

# HSV
![hsv_models](/Images/hsv_models.png)

# HSL
![hsl_models](/Images/hsl_models.png)

# Grayscale
I've been trying to recreate the Windows grayscale (for reasons). How to activate it - go to: Settings -> Ease of Access -> Color filters -> Grayscale. I've looked through many grayscale formulas, but wasn't able to figure out the precise Windows formula.

I can't take a screenshot of the Windows filter applied, so you have to check yourself. I've gotten close to the formula, but never got it 100% right.

From left to right: 

1 Blender grayscale node

2 Simple grayscale: (R + G + B) / 3

3 - 5 Weighted grayscale (R * wr + G * wg + B * wb), based on 3 different formulas, sorry, but I can't find them anymore. These were also the closest

6 - 8 Some gamma correction applied. I've seen the weighted formulas with gamma correction, but I believe that the correction is applied to photos or similar, not on computer generated math colors.

9 Average grayscale: (min(R, G, B) + max(R, G, B)) / 2

![grayscale](/Images/grayscale.png)

I also tried to calculate the Windows grayscale formula by taking 3 colors, their grayscale values and using an equation of 3 variables. This produced negative weights, so Windows doesn't just use a linear transformation.

I've also worked on a custom tool [github_link](https://github.com/Mahrkeenerh/python_filter), that will display the value of color. When applied on the RGB cube, the result it provided was closest to the Average grayscale cube, which is an interesting find.

![rgb_value](/Images/rgb_value.png)

# CIE XYZ model
I've read through this interesting study (it's also copied here, if the link stopped working): https://graphics.stanford.edu/courses/cs148-10-summer/docs/2010--kerr--cie_xyz.pdf

And so I've decided to recreate the CIE XYZ model too. This proved a rather hard task, because of the 3 imaginary light sources, but I've come to some result, which I don't really know how to interpret properly, read or whatever. So if anyone wants to continue on this, feel free to.

![cie_all](/Images/cie_all.png)

This model is calculated as a summation of 3 light sources (imaginary). Then it's recalculated to some other color space from left to right: sRGB, Adobe RGB, ProPhoto RGB.

I've expected all the sources to have linear gradients of energy. This displays how much of their source is added to the final dot. But instead, they are curving in the middle, and they straighten towards the ends.

I've checked my math multiple times, and can't figure out if I've made a mistake or not. The funny thing is, that the edge points are accurate (when I selected 0.5 value, they streched from the middle of one edge to the other, and were curvy in between).

![cie_05](/Images/cie_05.png)
![cie_05](/Images/cie_03.png)

# ERROR

How I calculated the source strenghts (this is a problem of weight distribution between 3 points in space. There are some formulas on how to calculate that, but I didn't really want to do it that way (but maybe it would have been better)):

First I needed to find the strength ratio for just two points (X, Y).
While rewriting this to be readable, I may have found the culprit of my error, and why it's all curvy and stuff. However I can't be bothered to come up with another formula, so it will stay as it is now.

![paper_1](/Images/paper_1.jpg)

Now I needed to calculate the strengths once more, between the top point, and my origin Z.

![paper_2](/Images/paper_2.jpg)

I've normalized these values, multiplied them with some stuff and came out with (hopefully) the strengths of X, Y, Z.

![cie_nodes](/Images/cie_nodes.png)

Finally, I've multiplied the strengths with Transformation Matrix values found at: http://brucelindbloom.com/index.html?Eqn_RGB_XYZ_Matrix.html

# HSV gradient calculator
This tool was made to make it easier to create gradients between two colors. It works in the HSV color space.

It takes the two points (their hex codes), and makes a line between them. Then splits this line into x points, and returns their properties (HSV, RGB, hex).

It's also possible to calculate a single point on this line, by setting one of the properties (h, s, v). It will then calculate the rest.

![calculator](/Images/calculator.png)
