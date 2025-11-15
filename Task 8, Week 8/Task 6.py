import svgwrite
from svgwrite import cm

def Square(dwg):
    left = float(input("- Left edge position: "))
    top = float(input("- Top edge position: "))
    side = float(input("- Side length: "))
    fill_color = input("- Fill color: ")
    stroke_color = input("- Stroke color: ")

    square = dwg.rect(lt = (left, top), size = (side, side), color = fill_color, color2 = stroke_color)
    dwg.add(square)

def Circle(dwg):
    center1 = float(input("- Left edge position: "))
    center2 = float(input("- Top edge position: "))
    radious = float(input("- Side length: "))
    fill_color = input("- Fill color: ")
    stroke_color = input("- Stroke color: ")

    circle = dwg.circle(center = (center1, center2), ra = radious, color1 = fill_color, color2 = stroke_color)
    dwg.add(circle)

def savedrawing(dwg):
    filename = input("file: ")
    print("Are you sure")
    Continue = input("y/n: ")
    if Continue.lower() == "y":
        dwg.saveas(filename, pretty = True, ident = 2)
    else:
        print("Cancel")

def main():
    dwg = svgwrite.Drawing(size=('800px', '600px'))
    while True:
        choices = int(input("Choices: "))
        if choices == 1:
            Square(dwg)
        elif choices == 2:
            Circle(dwg)
        elif choices == 3:
            savedrawing(dwg)
        elif choices == 0:
            break
if __name__ == "__main__":
    main()