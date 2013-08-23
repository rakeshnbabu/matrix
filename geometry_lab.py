from mat import Mat
import math
from matutil import rowdict2mat
from vec import Vec

## Task 1
def identity(labels = {'x','y','u'}):
    '''
    In case you have never seen this notation for a parameter before,
    the way it works is that identity() now defaults to having labels 
    equal to {'x','y','u'}.  So you should write your procedure as if 
    it were defined 'def identity(labels):'.  However, if you want the labels of 
    your identity matrix to be {'x','y','u'}, you can just call 
    identity().  Additionally, if you want {'r','g','b'}, or another set, to be the
    labels of your matrix, you can call identity({'r','g','b'}).  
    '''
    return Mat((labels,labels), {(l,l):1 for l in labels})

## Task 2
def translation(x,y):
    '''
    Input:  An x and y value by which to translate an image.
    Output:  Corresponding 3x3 translation matrix.
    '''
    labels = {'x','y','u'}
    retMat = Mat((labels,labels),{(l,l):1 for l in labels})
    retMat[('x','u')] = x
    retMat[('y','u')] = y
    return retMat
    

## Task 3
def scale(a, b):
    '''
    Input:  Scaling parameters for the x and y direction.
    Output:  Corresponding 3x3 scaling matrix.
    '''
    labels = {'x','y','u'}
    retMat = Mat((labels,labels),{(l,l):1 for l in labels})
    retMat[('x','x')] = a
    retMat[('y','y')] = b
    return retMat

## Task 4
def rotation(angle):
    '''
    Input:  An angle in radians to rotate an image.
    Output:  Corresponding 3x3 rotation matrix.
    Note that the math module is imported.
    '''
    labels = {'x','y','u'}
    retMat = Mat((labels,labels),{(l,l):1 for l in labels})
    retMat[('x','x')] = math.cos(angle)
    retMat[('y','y')] = math.cos(angle)
    retMat[('x','y')] = -math.sin(angle)
    retMat[('y','x')] = math.sin(angle)
    return retMat

## Task 5
def rotate_about(x,y,angle):
    '''
    Input:  An x and y coordinate to rotate about, and an angle
    in radians to rotate about.
    Output:  Corresponding 3x3 rotation matrix.
    It might be helpful to use procedures you already wrote.
    '''
    return translation(x,y)*rotation(angle)*translation(-x,-y)

## Task 6
def reflect_y():
    '''
    Input:  None.
    Output:  3x3 Y-reflection matrix.
    '''
    labels = {'x','y','u'}
    retMat = Mat((labels,labels),{(l,l):1 for l in labels})
    retMat[('x','x')] = -1
    return retMat

## Task 7
def reflect_x():
    '''
    Inpute:  None.
    Output:  3x3 X-reflection matrix.
    '''
    labels = {'x','y','u'}
    retMat = Mat((labels,labels),{(l,l):1 for l in labels})
    retMat[('y','y')] = -1
    return retMat
    
## Task 8    
def scale_color(scale_r,scale_g,scale_b):
    '''
    Input:  3 scaling parameters for the colors of the image.
    Output:  Corresponding 3x3 color scaling matrix.
    '''
    labels = {'r','g','b'}
    return Mat((labels,labels),{('r','r'):scale_r, ('g','g'):scale_g,('b','b'):scale_b})

## Task 9
def grayscale():
    '''
    Input: None
    Output: 3x3 greyscale matrix.
    '''
    labels = {'r','g','b'}
    row = Vec(labels,{'r':77/256, 'g':151/256, 'b':28/256})
    return(rowdict2mat({'r':row,'g':row,'b':row}))

## Task 10
def reflect_about(p1,p2):
    '''
    Input: 2 points that define a line to reflect about.
    Output:  Corresponding 3x3 reflect about matrix.
    '''
    return translate(-p1,-p2)*rotate(math.atan2(p2/p1))*reflect_x*rotate(-math.arctan(p2/p1))*translate(p1,p2)
