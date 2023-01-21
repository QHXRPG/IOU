import numpy as np
def box_IOU(a,b):
    a = np.array(a)
    b = np.array(b)
    xa1,ya1,xa2,ya2 = a[0],a[1],a[2],a[3]
    xb1,yb1,xb2,yb2 = b[0],b[1],b[2],b[3]
    X1,Y1,X2,Y2 = max(xa1,xb1), max(ya1,yb1), min(xa2,xb2), min(ya2,yb2)
    I = max((X2 - X1),0) * max((Y2 - Y1),0)
    U = (xa2 - xa1) * (ya2 - ya1) + (xb2 - xb1) * (yb2 - yb1) - I
    IOU = I/U
    return IOU
