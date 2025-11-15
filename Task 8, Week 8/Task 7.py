import svgwrite
from svgwrite import cm
import math

def drawsquare(dwg):
    left = float(input("- Left edge position: "))
    top = float(input("- Top edge position: "))
    side = float(input("- Side length: "))
    fill_color = input("- Fill color: ")
    stroke_color = input("- Stroke color: ")

    square = dwg.rect(lefttop = (left, top), size = (side, side), color1 = fill_color, color2 = stroke_color)
    dwg.add(square)

def drawHexagon(dwg):
    print("Insert hexagon details:")
    center_x = float(input("Middle point X: "))
    center_y = float(input("Middle point Y: "))
    apothem = float(input("Apothem length: "))
    fill_color = input("Insert fill: ")
    stroke_color = input("Insert stroke: ")

    circums = apothem / math.cos(math.radians(30))
    points = []
    for i in range(6):
        angle_degree = 30 + i * 60
        angle_radiant = math.radians(angle_degree)
        x = center_x + circums * math.cos(angle_radiant)
        y = center_y + circums * math.sin(angle_radiant)
        points.append(round(x), round(y))
        hexagon = dwg.polygon(points,fill_color, stroke_color)
        dwg.add(hexagon)

def drawcircle(dwg):
    center1 = float(input("- Left edge position: "))
    center2 = float(input("- Top edge position: "))
    radious = float(input("- Side length: "))
    fill_color = input("- Fill color: ")
    stroke_color = input("- Stroke color: ")

    circles = dwg.circle(center = (center1, center2), r = radious, color1 = fill_color, color2 = stroke_color)
    dwg.add(circles)

def savedraw(dwg):
    filename = input("File: ")
    print("Are you sure")
    save = input("y/n: ")
    if save.lower() == "y":
        dwg.saveas(filename, pretty = True, ident = 2)
    else:
        print("Cancel")

def main():
    dwg = svgwrite.Drawing(size=('800px', '600px'))
    while True:
        choices = int(input("Your choices: "))
        if choices == 1:
            drawsquare(dwg)
        elif choices == 2:
            drawcircle(dwg)
        elif choices == 3:
            savedraw(dwg)
        elif choices == 4:
            drawHexagon(dwg)
        elif choices == 0:
            break
if __name__ == "__main__":
    main()