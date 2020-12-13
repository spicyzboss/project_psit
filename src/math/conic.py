"""CONIC SECTION"""
from time import sleep as delay
import math
#Import แค่ฟังคชัน conic
def distance_ptop():
    """DISTANCE BETWEEN POINT AND POINT"""
    delay(0.5)
    print("Welcome to Distance between Point and Point topic!")
    delay(0.5)
    print()
    print("Input the first point(Input example \"(x,y)\": ", end="")
    point1_ptop = input()
    print("Input the second point(Input example \"(x,y)\": ", end="")
    point2_ptop = input()
    point1_ptop = point1_ptop.replace("(", "").replace(")", "")
    point2_ptop = point2_ptop.replace("(", "").replace(")", "")
    try :
        list_point1 = point1_ptop.split(",")
        list_point2 = point2_ptop.split(",")
        x_result_ptop = (float(list_point1[0])-float(list_point2[0]))**2
        y_result_ptop = (float(list_point1[1])-float(list_point2[1]))**2
        ans_ptop = math.sqrt(x_result_ptop+y_result_ptop)
        print()
        print("Distance between (%s) and (%s) is %.2f"%(point1_ptop, point2_ptop, ans_ptop))
    except:
        print()
        print("Please input in the same format as example.")
    
#_____________________________________END POINT TO POINT______________________________________
def line_made(num):
    """PRINT LINE"""
    if num >= 0:
        printnum =  "+"+str(num)
    elif num < 0: 
        printnum = str(num)
    return printnum
def distance_ptol():
    """DISTANCE BETWEEN POINT AND LINE"""
    delay(0.5)
    print("Welcome to Distance between Point and Line topic!")
    delay(0.5)
    print()
    print("Input the point(Input example \"(x,y)\": ", end="")
    point_ptol = input()
    print("From \"Ax + By + C = 0\": ")
    print("\t• Input \"A\": ", end="")
    a_ptol = float(input())
    print("\t• Input \"B\": ", end="")
    b_ptol = float(input())
    print("\t• Input \"C\": ", end="")
    c_ptol = float(input())
    point_ptol = point_ptol.replace("(", "").replace(")", "")
    try :
        list_point = point_ptol.split(",")
        top_ptol = abs(a_ptol*float(list_point[0])+b_ptol*float(list_point[1])+c_ptol)
        bottom_ptol = math.sqrt(a_ptol**2+b_ptol**2)
        ans_ptol = top_ptol/bottom_ptol
        print()
        print("Distance between (%s) and line %sx%sy%s = 0  is %.2f"%(point_ptol, a_ptol, line_made(b_ptol), line_made(c_ptol), ans_ptol))
    except:
        print()
        print("Please input in the same format as example.")
    
#_____________________________________END POINT TO LINE______________________________________

def distance_parallel():
    """DISTANCE BETWEEN PARALLEL LINE"""
    delay(0.5)
    print("Welcome to Distance between Parallel Line topic!")
    delay(0.5)
    print()
    print("From \"Ax + By + C1 = 0\" and \"Ax + By + C2 = 0\": ")
    print("\t• Input \"A\": ", end="")
    a_parallel = float(input())
    print("\t• Input \"B\": ", end="")
    b_parallel = float(input())
    print("\t• Input \"C1\": ", end="")
    c1_parallel = float(input())
    print("\t• Input \"C2\": ", end="")
    c2_parallel = float(input())
    
    try :
        
        top_parallel = abs(c1_parallel-c2_parallel)
        bottom_parallel = math.sqrt(a_parallel**2+b_parallel**2)
        ans_parallel = top_parallel/bottom_parallel
        print()
        print("Distance between line %sx%sy%s and line %sx%sy%s = 0  is %.2f"\
            %(a_parallel, line_made(b_parallel), line_made(c1_parallel), a_parallel, line_made(b_parallel), line_made(c2_parallel), ans_parallel))
    except:
        print()
        print("Please input in the correct form")
    

#_____________________________________END PARALLEL LINE______________________________________
    
def half_2p():
    """HALF POINT BETWEEN 2 POINTS"""
    delay(0.5)
    print("Welcome to Half Point between 2 points topic!")
    delay(0.5)
    print()
    print("Input the first point(Input example \"(x,y)\": ", end="")
    point1_half_2p = input()
    print("Input the second point(Input example \"(x,y)\": ", end="")
    point2_half_2p = input()
    point1_half_2p = point1_half_2p.replace("(", "").replace(")", "")
    point2_half_2p = point2_half_2p.replace("(", "").replace(")", "")
    try :
        list_point1 = point1_half_2p.split(",")
        list_point2 = point2_half_2p.split(",")
        x_result_half_2p = (float(list_point1[0])+float(list_point2[0]))/2
        y_result_half_2p = (float(list_point1[1])+float(list_point2[1]))/2
        print()
        print("Half Point between (%s) and (%s) is (%.2f,%.2f)"%(point1_half_2p, point2_half_2p, x_result_half_2p, y_result_half_2p))
    except:
        print()
        print("Please input in the same format as example.")
    
#_____________________________________END HALF POINT TO POINT______________________________________

def circle_equation():
    """FIND RADIAUS AND CENTER POINT OF CIRCLE"""
    delay(0.5)
    print("Welcome to Circle Conic topic!")
    print("This Topic will find Center Point and Radius for you")
    delay(0.5)
    print()
    print("What form of Equation do you have? (\"^\" mean Exponential)")
    print()
    print("1) (x-A)^2 + (y-B)^2 = C\t2) x^2 + y^2 +Ax + By + C = 0")
    print("Answer the number(1 or 2): ", end="")
    circle_equa_type = int(input())
    if circle_equa_type == 1:
        print()
        print("From \"(x-A)^2 + (y-B)^2 = C\"")
        print("\t• Input \"A\": ", end="")
        a_circle_1 = float(input())
        print("\t• Input \"B\": ", end="")
        b_circle_1 = float(input())
        print("\t• Input \"C\"(>=0): ", end="")
        c_circle_1 = float(input())
        try:
            radius_circle_1 = math.sqrt(c_circle_1)
            print()
            print("The Center Point of this circle equation is (%.2f,%.2f)"%(a_circle_1, b_circle_1))
            print()
            print("The Radius of this circle equation is %.2f"%(radius_circle_1))
        except:
            print("Your Equation can't make circle!")
    elif circle_equa_type == 2:
        print()
        print("From \"x^2 + y^2 +Ax + By + C = 0\"")
        print("\t• Input \"A\": ", end="")
        a_circle_2 = float(input())
        print("\t• Input \"B\": ", end="")
        b_circle_2 = float(input())
        print("\t• Input \"C\"(>=0): ", end="")
        c_circle_2 = float(input())
        try:
            center_circle2_a, center_circle2_b = (-1*a_circle_2)/2, (-1*b_circle_2)  
            radius_circle_2 = (1/2)*math.sqrt((a_circle_2**2)+(b_circle_2**2)-(4*c_circle_2))
            print()
            print("The Center Point of this circle equation is (%.2f,%.2f)"%(center_circle2_a, center_circle2_b))
            print()
            print("The Radius of this circle equation is %.2f"%(radius_circle_2))
        except:
            print("Your Equation can't make circle!")
        
#_____________________________________END CIRCLE CONIC______________________________________

def parabola_equation():
    """FIND TYPE ,FOCUS POINT,DIRECTRIX EQUATION, LATUS LECTUM LENGTH"""
    delay(0.5)
    print("Welcome to Parabola Conic topic!")
    print("This Topic will find Type of graph, Focus Point, Directrix equation and Latus Lectum Length for you")
    delay(0.5)
    print()
    print("What form of Equation do you have? (\"^\" mean Exponential)")
    print()
    print("1) (y-B)^2 = C(x-A)\t2) (x-A)^2 = C(y-B)")
    print("Answer the number(1 or 2): ", end="")
    parabola_equa_type = int(input())
    if parabola_equa_type == 1:
        print()
        print("From \"(y-B)^2 = C(x-A)\"")
        print("\t• Input \"A\": ", end="")
        a_parabola_1 = float(input())
        print("\t• Input \"B\": ", end="")
        b_parabola_1 = float(input())
        print("\t• Input \"C\"(>0 or <0): ", end="")
        c_parabola_1 = float(input())
        try:
            if c_parabola_1 > 0:
                graph_type_parabola_1 = "Right-Parabola"
                focus_point_1_x = a_parabola_1+(c_parabola_1/4)
                dirix_eqation = -1*(c_parabola_1/4)
                latus_lectum_1 = abs(c_parabola_1)
            elif c_parabola_1 < 0:
                graph_type_parabola_1 = "Left-Parabola"
                focus_point_1_x = a_parabola_1+(c_parabola_1/4)
                dirix_eqation = -1*(c_parabola_1/4)
                latus_lectum_1 = abs(c_parabola_1)
            print()
            print("The Graph Type of this parabola equation is %s"%(graph_type_parabola_1))
            print()
            print("The Focus point of this parabola equation is (%.2f,%.2f)"%(focus_point_1_x, b_parabola_1))
            print()
            print("The Directrix Equation of this parabola equation is x = %.2f "%(dirix_eqation))
            print()
            print("The Latus Lectrum Length of this parabola equation is %.2f"%(latus_lectum_1))

        except:
            print("Your Equation can't make parabola!")
    elif parabola_equa_type == 2:
        print()
        print("From \"(x-A)^2 = C(y-B)\"")
        print("\t• Input \"A\": ", end="")
        a_parabola_2 = float(input())
        print("\t• Input \"B\": ", end="")
        b_parabola_2 = float(input())
        print("\t• Input \"C\"(>0 or <0): ", end="")
        c_parabola_2 = float(input())
        try:
            if c_parabola_2 > 0:
                graph_type_parabola_2 = "Up-Parabola"
                focus_point_2_y = b_parabola_2+(c_parabola_2/4)
                dirix_eqation = -1*(c_parabola_2/4)
                latus_lectum_2 = abs(c_parabola_2)
            elif c_parabola_2 < 0:
                graph_type_parabola_2 = "Down-Parabola"
                focus_point_2_y = b_parabola_2+(c_parabola_2/4)
                dirix_eqation = -1*(c_parabola_2/4)
                latus_lectum_2 = abs(c_parabola_2)
            print()
            print("The Graph Type of this parabola equation is %s"%(graph_type_parabola_2))
            print()
            print("The Focus point of this parabola equation is (%.2f,%.2f)"%(a_parabola_2, focus_point_2_y))
            print()
            print("The Directrix Equation of this parabola equation is x = %.2f "%(dirix_eqation))
            print()
            print("The Latus Lectrum Length of this parabola equation is %.2f"%(latus_lectum_2))
        except:
            print("Your Equation can't make parabola!")
    
#_____________________________________END PARABOLA_____________________________________

def ellipse_equation():
    """FIND MAJOR AXIS, FOCUS POINT, VERTEX POINT, MAJOR AXIS LENGTH\
        , MINOR AXIS LENGTH, LATUS LECTUM LENGTH"""
    delay(0.5)
    print("Welcome to Ellipse Conic topic!")
    print("This Topic will find Major Axis, Vertex, Focus Point, Point end of minor, Length of Major/Minor Axis and Length of Latus Lectum for you")
    delay(0.5)
    print()
    print("What form of Equation do you have? (\"^\" mean Exponential, \"/\" mean Divided)")
    print()
    print("1) (x-A)^2/C+(y-B)^2/D = 1 (Horizonal)\t\t2) (x-A)^2/D+(y-B)^2/C = 1 (Vertical)")
    print("Answer the number(1 or 2): ", end="")
    ellipse_equa_type = int(input())
    if ellipse_equa_type == 1:
        print()
        print("From \"((x-A)^2/C+(y-B)^2)/D (Horizonal)\"")
        print("\t• Input \"A\": ", end="")
        a_ellipse_1 = float(input())
        print("\t• Input \"B\": ", end="")
        b_ellipse_1 = float(input())
        print("\t• Input \"C\"(>0 or <0): ", end="")
        c_ellipse_1 = float(input())
        print("\t• Input \"D\"(>0 or <0 , D<=C): ", end="")
        d_ellipse_1 = float(input())
        try:
            c_cal_1 = math.sqrt(c_ellipse_1-d_ellipse_1)
            vertex_ellispe_1_h1 = a_ellipse_1-math.sqrt(c_ellipse_1)
            vertex_ellispe_1_h2 = a_ellipse_1+math.sqrt(c_ellipse_1)
            focus_ellispe_1_h1 = a_ellipse_1-c_cal_1
            focus_ellispe_1_h2 = a_ellipse_1+c_cal_1
            pointminor_ellispe_1_k1 = b_ellipse_1-math.sqrt(d_ellipse_1)
            pointminor_ellispe_1_k2 = b_ellipse_1+math.sqrt(d_ellipse_1)
            major_lenght = 2*math.sqrt(c_ellipse_1)
            minor_lenght = 2*math.sqrt(d_ellipse_1)
            latus_lectum_e1 = (2*d_ellipse_1)/math.sqrt(c_ellipse_1)
            print()
            print("The Major Axis of this ellipse equation is X")
            print()
            print("The Vertex of this ellipse equation is (%.2f,%.2f) and (%.2f,%.2f)"%(vertex_ellispe_1_h1,b_ellipse_1,vertex_ellispe_1_h2,b_ellipse_1))
            print()
            print("The Focus Point of this ellipse equation is (%.2f,%.2f) and (%.2f,%.2f)"%(focus_ellispe_1_h1,b_ellipse_1,focus_ellispe_1_h2,b_ellipse_1))
            print()
            print("The Point end of Minor Axis of this ellipse equation is (%.2f,%.2f) and (%.2f,%.2f)"%(a_ellipse_1,pointminor_ellispe_1_k1,a_ellipse_1,pointminor_ellispe_1_k2))
            print()
            print("The Major Axis Length of this ellipse equation is %.2f"%(major_lenght))
            print()
            print("The Minor Axis Length of this ellipse equation is %.2f"%(minor_lenght))
            print()
            print("The Latus Lectrum Length of this ellipse equation is %.2f"%(latus_lectum_e1))
        except:
            print("Your Equation can't make ellipse!")
    elif ellipse_equa_type == 2:
        print()
        print("From \"((x-A)^2/D+(y-B)^2)/C (Vertical)\"")
        print("\t• Input \"A\": ", end="")
        a_ellipse_2 = float(input())
        print("\t• Input \"B\": ", end="")
        b_ellipse_2 = float(input())
        print("\t• Input \"C\"(>0 or <0): ", end="")
        c_ellipse_2 = float(input())
        print("\t• Input \"D\"(>0 or <0 , D<=C): ", end="")
        d_ellipse_2 = float(input())
        try:
            c_cal_2 = math.sqrt(c_ellipse_2-d_ellipse_2)
            vertex_ellispe_2_k1 = b_ellipse_2-math.sqrt(c_ellipse_2)
            vertex_ellispe_2_k2 = b_ellipse_2+math.sqrt(c_ellipse_2)
            focus_ellispe_2_k1 = b_ellipse_2-c_cal_2
            focus_ellispe_2_k2 = b_ellipse_2+c_cal_2
            pointminor_ellispe_2_h1 = a_ellipse_2-math.sqrt(d_ellipse_2)
            pointminor_ellispe_2_h2 = a_ellipse_2+math.sqrt(d_ellipse_2)
            major_lenght = 2*math.sqrt(c_ellipse_2)
            minor_lenght = 2*math.sqrt(d_ellipse_2)
            latus_lectum_e2 = (2*d_ellipse_2)/math.sqrt(c_ellipse_2)
            print()
            print("The Major Axis of this ellipse equation is Y")
            print()
            print("The Vertex of this ellipse equation is (%.2f,%.2f) and (%.2f,%.2f)"%(a_ellipse_2, vertex_ellispe_2_k1, a_ellipse_2, vertex_ellispe_2_k2))
            print()
            print("The Focus Point of this ellipse equation is (%.2f,%.2f) and (%.2f,%.2f)"%(a_ellipse_2, focus_ellispe_2_k1, a_ellipse_2,focus_ellispe_2_k2))
            print()
            print("The Point end of Minor Axis of this ellipse equation is (%.2f,%.2f) and (%.2f,%.2f)"%(pointminor_ellispe_2_h1, b_ellipse_2, pointminor_ellispe_2_h2, b_ellipse_2))
            print()
            print("The Major Axis Length of this ellipse equation is %.2f"%(major_lenght))
            print()
            print("The Minor Axis Length of this ellipse equation is %.2f"%(minor_lenght))
            print()
            print("The Latus Lectrum Length of this ellipse equation is %.2f"%(latus_lectum_e2))
        except:
            print("Your Equation can't make ellipse!")
    
#_____________________________________END ELLIPSE_______________________________________________________________________________________________________
def line_made2(num):
    """PRINT LINE"""
    num = num*-1
    if num >= 0:
        printnum =  "+"+str(num)
    elif num < 0: 
        printnum = str(num)
    return printnum

    
def hyperbola_equation():
    """FIND CENTER POINT, FOCUS POINT, VERTEX POINT, MAJOR AXIS LENGTH\
        , MINOR AXIS LENGTH, LATUS LECTUM LENGTH, ASYMTOTE"""
    delay(0.5)
    print("Welcome to Hyperbola Conic topic!")
    print("This Topic will find Center Point, Vertex, Focus Point, Length of Major/Minor Axis,Length of Latus Lectum and Asymtotefor you")
    delay(0.5)
    print()
    print("What form of Equation do you have? (\"^\" mean Exponential, \"/\" mean Divided)")
    print()
    print("1) (x-A)^2/C-(y-B)^2/D = 1 (Horizonal)\t\t2) (y-B)^2/C-(x-A)^2/D = 1 (Vertical)")
    print("Answer the number(1 or 2): ", end="")
    hyperbola_equa_type = int(input())
    if hyperbola_equa_type == 1:
        print()
        print("From \"((x-A)^2/C-(y-B)^2)/D (Horizonal)\"")
        print("\t• Input \"A\": ", end="")
        a_hyperbola_1 = float(input())
        print("\t• Input \"B\": ", end="")
        b_hyperbola_1 = float(input())
        print("\t• Input \"C\"(>0 or <0): ", end="")
        c_hyperbola_1 = float(input())
        print("\t• Input \"D\"(>0 or <0): ", end="")
        d_hyperbola_1 = float(input())
        try:
            c_cal_1 = math.sqrt(c_hyperbola_1+d_hyperbola_1)
            vertex_hyperbola_1_h1 = a_hyperbola_1-math.sqrt(c_hyperbola_1)
            vertex_hyperbola_1_h2 = a_hyperbola_1+math.sqrt(c_hyperbola_1)
            focus_hyperbola_1_h1 = a_hyperbola_1-c_cal_1
            focus_hyperbola_1_h2 = a_hyperbola_1+c_cal_1
            transverse_lenght = 2*math.sqrt(c_hyperbola_1)
            conjugate_lenght = 2*math.sqrt(d_hyperbola_1)
            latus_lectum_hy1 = (2*d_hyperbola_1)/math.sqrt(c_hyperbola_1)
            print()
            print("The Center Point of this hyperbola equation is (%.2f,%.2f)"%(a_hyperbola_1, b_hyperbola_1))
            print()
            print("The Vertex of this hyperbola equation is (%.2f,%.2f) and (%.2f,%.2f)"%(vertex_hyperbola_1_h1,b_hyperbola_1,vertex_hyperbola_1_h2,b_hyperbola_1))
            print()
            print("The Focus Point of this hyperbola equation is (%.2f,%.2f) and (%.2f,%.2f)"%(focus_hyperbola_1_h1,b_hyperbola_1,focus_hyperbola_1_h2,b_hyperbola_1))
            print()
            print("The Transverse Axis Length of this hyperbola equation is %.2f"%(transverse_lenght))
            print()
            print("The Conjugate Axis Length of this hyperbola equation is %.2f"%(conjugate_lenght))
            print()
            print("The Latus Lectrum Length of this hyperbola equation is %.2f"%(latus_lectum_hy1))
            print()
            asym_plus = math.sqrt(d_hyperbola_1)/math.sqrt(c_hyperbola_1)
            asym_min = -1*math.sqrt(d_hyperbola_1)/math.sqrt(c_hyperbola_1)
            print("The Asymtote of this hyperbola equation is \"y%s = %.2f(x%s)\" and \"y%s = %.2f(x%s)\""%(line_made2(b_hyperbola_1), asym_plus, line_made2(a_hyperbola_1)\
                , line_made2(b_hyperbola_1), asym_min, line_made2(a_hyperbola_1) ))
        except:
            print("Your Equation can't make hyperbola!")
    elif hyperbola_equa_type == 2:
        print()
        print("From \"(y-B)^2)/C-((x-A)^2/D (Vertical)\"")
        print("\t• Input \"A\": ", end="")
        a_hyperbola_2 = float(input())
        print("\t• Input \"B\": ", end="")
        b_hyperbola_2 = float(input())
        print("\t• Input \"C\"(>0 or <0): ", end="")
        c_hyperbola_2 = float(input())
        print("\t• Input \"D\"(>0 or <0): ", end="")
        d_hyperbola_2 = float(input())
        try:
            c_cal_2 = math.sqrt(c_hyperbola_2+d_hyperbola_2)
            vertex_hyperbola_2_k1 = b_hyperbola_2-math.sqrt(c_hyperbola_2)
            vertex_hyperbola_2_k2 = b_hyperbola_2+math.sqrt(c_hyperbola_2)
            focus_hyperbola_2_k1 = b_hyperbola_2-c_cal_2
            focus_hyperbola_2_k2 = b_hyperbola_2+c_cal_2
            transverse_lenght = 2*math.sqrt(c_hyperbola_2)
            conjugate_lenght = 2*math.sqrt(d_hyperbola_2)
            latus_lectum_hy2 = (2*d_hyperbola_2)/math.sqrt(c_hyperbola_2)
            print()
            print("The Center Point of this hyperbola equation is (%.2f,%.2f)"%(a_hyperbola_2, b_hyperbola_2))
            print()
            print("The Vertex of this hyperbola equation is (%.2f,%.2f) and (%.2f,%.2f)"%(a_hyperbola_2, vertex_hyperbola_2_k1, a_hyperbola_2, vertex_hyperbola_2_k2))
            print()
            print("The Focus Point of this hyperbola equation is (%.2f,%.2f) and (%.2f,%.2f)"%(a_hyperbola_2, focus_hyperbola_2_k1, a_hyperbola_2,focus_hyperbola_2_k2))
            print()
            print("The Transverse Axis Length of this hyperbola equation is %.2f"%(transverse_lenght))
            print()
            print("The Conjugate Axis Length of this hyperbola equation is %.2f"%(conjugate_lenght))
            print()
            print("The Latus Lectrum Length of this hyperbola equation is %.2f"%(latus_lectum_hy2))
            print()
            asym_plus = math.sqrt(c_hyperbola_2)/math.sqrt(d_hyperbola_2)
            asym_min = -1*math.sqrt(c_hyperbola_2)/math.sqrt(d_hyperbola_2)
            print("The Asymtote of this hyperbola equation is \"y%s = %.2f(x%s)\" and \"y%s = %.2f(x%s)\""%(line_made2(b_hyperbola_2), asym_plus, line_made2(a_hyperbola_2)\
                , line_made2(b_hyperbola_2), asym_min, line_made2(a_hyperbola_2) ))
        except:
            print("Your Equation can't make hyperbola!")
    
#_____________________________________END hyperbola______________________________________
def conic():
    """Main Function"""
    print()
    print("CONIC SECTION")
    print()
    print("► Distance between Point and Point\t\t► Distance between Point and Line")
    print("► Distance between Parallel Line\t\t► Middle point between 2 points")
    print("► Circle Equation\t► Parabola Equation\t► Ellipse Equation\t► Hyperbola Equation")
    print()
    print("What topic do you want to find?: ", end="")
    type_input_conic = input().upper()
    if type_input_conic == "DISTANCE BETWEEN POINT AND POINT":
        distance_ptop()
    elif type_input_conic == "DISTANCE BETWEEN POINT AND LINE":
        distance_ptol()
    elif type_input_conic == "DISTANCE BETWEEN PARALLEL LINE":
        distance_parallel()
    elif type_input_conic == "MIDDLE POINT BETWEEN 2 POINTS":
        half_2p()
    elif type_input_conic == "CIRCLE EQUATION":
        circle_equation()
    elif type_input_conic == "PARABOLA EQUATION":
        parabola_equation()
    elif type_input_conic == "ELLIPSE EQUATION":
        ellipse_equation()
    elif type_input_conic == "HYPERBOLA EQUATION":
        hyperbola_equation()

