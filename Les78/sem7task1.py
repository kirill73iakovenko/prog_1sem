import tkinter as tk
class Vector():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x + other, self.y + other, self.z + other)
    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x * other, self.y * other, self.z * other)

def Center_Mass(l, res):
    x_sum = 0
    y_sum = 0
    z_sum = 0
    for i in range(len(l)):
        x_sum += l[i].x
        y_sum += l[i].y
        z_sum += l[i].z
    x_sum = x_sum / len(l)
    y_sum = y_sum / len(l)
    z_sum = z_sum / len(l)
    text = str(round(x_sum, 2)) + ' ' + str(round(y_sum, 2)) + ' ' + str(round(z_sum, 2))
    res.set(text)



class Point():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Triangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def Sides(self):
        side1 = Vector(self.a.x - self.b.x, self.a.y - self.b.y, self.a.z - self.b.z)
        side2 = Vector(self.b.x - self.c.x, self.b.y - self.c.y, self.b.z - self.c.z)
        side3 = Vector(self.a.x - self.c.x, self.a.y - self.c.y, self.a.z - self.c.z)
        length1 = abs(side1)
        length2 = abs(side2)
        length3 = abs(side3)
        return length1, length2, length3
    def Perimetr(self):
        length1, length2, length3 = self.Sides()
        per = length1 + length2 + length3
        return per
    def Square(self):
        length1, length2, length3 = self.Sides()
        per = self.Perimetr()
        per2 = per/2
        sqr = (per2 * (per2 - length1) * (per2 - length2) * (per2 - length3))**(1/2)
        return sqr


def Max_Square(l, res):
    triangles = []
    sqr_triangles = []
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            for k in range(j+1, len(l)):
                triangles.append(Triangle(l[i], l[j], l[k]))
    for i in range(len(triangles)):
        sqr_triangles.append(triangles[i].Square())
    result = max(sqr_triangles)
    res.set(result)


def save_v(s, l):
    l1 = list(s.split())
    l2 = []
    for i in range(len(l1)):
        if l1[i] == ',' or l1[i] == '.':
            continue
        else:
            l2.append(float(l1[i]))
    p = Point(l2[0], l2[1], l2[2])
    l.append(p)
def Clean(l):
    l.clear()
    return l

def main():
    Points = []
    root = tk.Tk()
    root.geometry('500x300')
    data = tk.StringVar()
    CCM = tk.StringVar()
    Squar = tk.StringVar()
    tk.Entry(root, textvariable=data).grid(row=1, column=1)
    tk.Button(root, text='Add a point', command=lambda: save_v(data.get(), Points)).grid(row=1, column=2)
    tk.Button(root, text='Find the center of mass', command=lambda:  Center_Mass(Points, CCM)).grid(row=2, column=1)
    tk.Button(root, text='Remove all points', command=lambda: Clean(Points)).grid(row=2,column=2)
    tk.Label(root, text='Сoordinates of the center of mass').grid(row=3, column=1)
    tk.Label(root, textvariable=CCM).grid(row=3, column=2)
    tk.Button(root, text ='Max Square', command=lambda: Max_Square(Points, Squar)).grid(row=4, column=2)
    tk.Label(root, textvariable=Squar).grid(row=4, column=1)
    root.mainloop()

if __name__ == '__main__':
    main()
