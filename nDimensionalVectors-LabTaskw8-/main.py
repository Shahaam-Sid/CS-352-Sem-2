from vectornd import NdVector

try:
    v1 = NdVector(3)
    v2 = NdVector(3)

    v1[0], v1[1], v1[2] = 1, 2, 3
    v2[0], v2[1], v2[2] = 4, 5, 6

    print("v1 =", v1)
    print("v2 =", v2)

    print("len(v1) =", len(v1))

    print("v1[0] =", v1[0])
    print("v1[-1] =", v1[-1])

    print("v1 + v2 =", v1 + v2)

    print("v2 - v1 =", v2 - v1)

    print("v1 * 2 =", v1 * 2)

    print("3 * v1 =", 3 * v1)

    print("|v1| =", abs(v1))
    
except TypeError as e:
    print("Error: ", e)
except IndexError as e:
    print("Error: ", e)
except ValueError as e:
    print("Error", e)
except Exception:
    print("Error: An Error has Occured")