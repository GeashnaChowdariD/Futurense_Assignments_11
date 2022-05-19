import matplotlib.pyplot as plt

import numpy as np

# xpoints = np.array([1, 8])
# ypoints = np.array([3,10])
#
# plt.plot(xpoints, ypoints)
# plt.show()

# xpoints = np.array([1, 8])
# ypoints = np.array([3,10])
#
# plt.plot(xpoints, ypoints, 'o')
# plt.show()

#
# xpoints = np.array([1, 2, 6, 8])
# ypoints = np.array([3, 8, 1, 10])
#
# plt.plot(xpoints, ypoints)
# plt.show()


# ypoints = np.array([3, 8, 1, 10, 5, 7])
#
# plt.plot(ypoints)
# plt.show()    #The x-points in the example above is [0, 1, 2, 3, 4, 5]


# xpoints = np.array([1, 8])
# ypoints = np.array([3,10])
#
# plt.plot(xpoints, ypoints, marker='>')
# plt.show()

# xpoints = np.array([1, 8])
# ypoints = np.array([3,10])
#
# plt.plot(xpoints, ypoints, 'D--k')
# plt.show()

# x = np.linspace(0, 14, 100)
# print(x)

# def sinplot(flip = 2):
#     x = np.linspace(0, 14, 100)
#     for i in range(1, 5):
#         plt.plot(x, np.sin(x + i * .5)*(7 - i) * flip)

# sinplot()
# # plt.show()


# import seaborn as  sb
# sb.set()
# sinplot()
# plt.show()

# ypoints = np.array([3, 8, 1, 10])
#
# plt.plot(ypoints, marker = 'o', ms = 20)
# plt.show()

# ypoints = np.array([3, 8, 1, 10])
#
# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
# plt.show()

# ypoints = np.array([3, 8, 1, 10])
#
# plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
# plt.show()

# ypoints = np.array([3, 8, 1, 10])
#
# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'g')
# plt.show()

# plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
# plt.show()
#
# ypoints = np.array([3, 8, 1, 10])
#
# plt.plot(ypoints, linestyle = 'dotted')
# plt.show()

# x1 = np.array([0, 1, 2, 3])
# y1 = np.array([3, 8, 1, 10])
# x2 = np.array([0, 1, 2, 3])
# y2 = np.array([6, 2, 7, 11])
#
# plt.plot(x1, y1, x2, y2)
# plt.show()


# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
#
# plt.plot(x, y)
#
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
#
# plt.show()


# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
#
# plt.plot(x, y)
#
# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
#
# plt.show()

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
#
# font1 = {'family':'serif','color':'blue','size':20}
# font2 = {'family':'serif','color':'darkred','size':15}
#
# plt.title("Sports Watch Data", fontdict = font1)
# plt.xlabel("Average Pulse", fontdict = font2)
# plt.ylabel("Calorie Burnage", fontdict = font2)
#
# plt.plot(x, y)
# plt.show()


# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
#
# plt.title("Sports Watch Data", loc = 'left')
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
#
# plt.plot(x, y)
# plt.show()

####################### Adding Grid ##################

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
#
# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
#
# plt.plot(x, y)
#
# #plt.grid()
# plt.grid(axis = 'x')
#
# plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
#
# plt.show()

#############################  Subplot ####################

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
#
# plt.subplot(2, 3, 1)
# plt.plot(x,y)
#
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
#
# plt.subplot(2, 3, 2)
# plt.plot(x,y)
#
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
#
# plt.subplot(2, 3, 3)
# plt.plot(x,y)
#
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
#
# plt.subplot(2, 3, 4)
# plt.plot(x,y)
#
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
#
# plt.subplot(2, 3, 5)
# plt.plot(x,y)
#
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
#
# plt.subplot(2, 3, 6)
# plt.plot(x,y)
#
# plt.show()


#################### Scatter ######################


# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
#
# plt.scatter(x, y, c=colors, cmap='autumn')
#
# plt.colorbar()
#
# plt.show()


# x = np.random.randint(100, size=(100))
# y = np.random.randint(100, size=(100))
# colors = np.random.randint(100, size=(100))
# sizes = 10 * np.random.randint(100, size=(100))
#
# plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')
#
# plt.colorbar()
#
# plt.show()

# import seaborn as sb
# sb.axes_style()
#
# from matplotlib import pyplot as plt
# import seaborn as sb
# current_palette = sb.color_palette()
# current_palette = sb.color_palette("Greens")
# sb.palplot(current_palette)
# plt.show()

# def sinplot(flip = 2):
#     x = np.linspace(0, 14, 100)
#     for i in range(1, 20):
#         plt.plot(x, np.sin(x + i * .5)*(7 - i) * flip)
# #
# # # import seaborn as  sb
# # # sb.set_style("white")
# # # sb.set_palette(("flare"))
# # # sinplot()
# # # plt.show()
# #
# # import seaborn as  sb
# # sb.set_style("white")
# # sb.set_palette(("Greens"))
# # sinplot()
# # plt.show()
#
# import seaborn as  sb
# sb.set_style("white")
# sb.set_palette(("dark"))
# sinplot()
# plt.show()

# from matplotlib import pyplot as plt
# import seaborn as sns
# sns.set_style("darkgrid", {"grid.color": ".6", "grid.linestyle": ":"})
# sns.lineplot(x=["A", "B", "C"], y=[1, 3, 2]) #sns.barplot(x=["A", "B", "C"], y=[1, 3, 2])
# plt.show()

# a = 'My sr'
# b = 2
# c = id(a) + id(b)
# print(type(c))
#
# def MyFunction(*args, **kwargs):
#     print(args)
#     print(kwargs)
# MyFunction(1, 2, 3, a=1, b=2, c=3)

# def MyFunction(a, *args, b=1, **kwargs):
#     print(a, args, b, kwargs)
#
# MyFunction(c=1)

# def MyFunction(a):
#     return a**2
# print(MyFunction(3))
# print(MyFunction(a=3))


# def IsThisRecursion(start, answer):
#     if start>=10:
#         return answer
#     else:
#         start += 1
#         answer *= start
#         return Recursion(start, answer)
# print(IsThisRecursion(1,0))


# def IsThisRecursion(start, answer):
#     if start>=10:
#         return answer
#     else:
#         start += 1
#         answer *= start
#         return IsThisRecursion(start, answer)
# print(IsThisRecursion(1,0))
#
# def IsThisRecursion(start, answer):
#     if start>=10:
#         return answer
#     else:
#         start += 1
#         answer += start
#         return IsThisRecursion(start, answer)
# print(IsThisRecursion(1,0))

# print((True!=False)*2*"A")

# a = 1
# b = 1
# print(id(a))
# print(id(b))
# print(a is b)
# print((a == b) and (a is b))
# a = (3+5j)
# b = (3+5j)
# c = a
# d = b
#
# print((a== b) or (c is b ) and not (d is a))

import string
print(string.ascii_letters)

print(0.1 + 0.2 == 0.3)
print(round(0.1+0.2, 2) == round(0.3, 2))

