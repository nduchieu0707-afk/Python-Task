def askDimension(PPrompt: str) -> float:
   Feed = input(PPrompt)
   return float(Feed)

Width = askDimension("Insert width: ")
Height = askDimension("Insert height: ")

def calcRectangleArea(PWidth: float, PHeight: float) -> float:
   Area = PWidth * PHeight
   return Area

Area = calcRectangleArea(Width, Height)
print("")
print(f"Area is {Area}²")
print("end")