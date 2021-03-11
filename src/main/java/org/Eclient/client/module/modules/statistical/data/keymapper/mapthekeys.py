from PIL import Image
from PIL import ImageDraw, ImageEnhance
import sys
import os
import numpy

keymapperpath = (os.getenv('AppData')+'\\.minecraft\\mcpipy\\src\\main\\java\\org\\Eclient\\client\\module\\modules\\statistical\\data\\keymapper\\')
keyboard = (keymapperpath+'keyboard.jpg')
keyboardwithmouse = (keymapperpath+'keyboardwithmouse.png')
keyboardcpy = (keymapperpath+'keyboard.jpg')

rangearr = []

A = 0
B = 0
C = 0
D = 0
E = 0
F = 0
G = 0
H = 0
I = 0
J = 0
K = 0
L = 0
M = 0
N = 0
O = 0
P = 0
Q = 0
R = 0
S = 0
T = 0
U = 0
V = 0
W = 0
X = 0
Y = 0
Z = 0
ONE = 0
TWO = 0
THREE = 0
FOUR = 0
FIVE = 0
SIX = 0
SEVEN = 0
EIGHT = 0
NINE = 0
ZERO = 0

EQUALS = 0
MINUS = 0
LBRACE = 0
RBRACE = 0
BKWDSLASH = 0
SEMICOLON = 0
SINGLEQUOTE = 0
COMMA = 0
PERIOD = 0
SLASH = 0

#Virtual Keys
TAB = 0
CAPS = 0
ESCAPE = 0
SHIFT = 0
RETURN = 0
CONTROL = 0
SPACE = 0
SELECT = 0
PRINT = 0
EXECUTE = 0
SNAPSHOT = 0
INSERT = 0
DELETE = 0
HELP = 0
LWIN = 0
RWIN = 0
APPS = 0
SLEEP = 0
NUMPAD0 = 0
NUMPAD1 = 0
NUMPAD2 = 0
NUMPAD3 = 0
NUMPAD4 = 0
NUMPAD5 = 0
NUMPAD6 = 0
NUMPAD7 = 0
NUMPAD8 = 0
NUMPAD9 = 0
MULTIPLY = 0
ADD = 0
SEPERATOR = 0
SUBTRACT = 0
DECIMAL = 0
DIVIDE = 0
F1 = 0
F2 = 0
F3 = 0
F4 = 0
F5 = 0
F6 = 0
F7 = 0
F8 = 0
F9 = 0
F10 = 0
F11 = 0
F12 = 0
NUMLOCK = 0
SCROLL = 0
BACKSPACE = 0

ARROWUP = 0
ARROWDOWN = 0
ARROWLEFT = 0
ARROWRIGHT = 0

#Mouse
LBUTTON = 0
RBUTTON = 0
MBUTTON = 0


with open(keymapperpath+'keymap.txt') as keymap:
    for key in keymap:
        #Letters and numbers
        if key == 'A\n':
            A += 1
        elif key == "B\n":
            B += 1
        elif key == "C\n":
            C += 1
        elif key == "D\n":
            D += 1
        elif key == "E\n":
            E += 1
        elif key == "F\n":
            F += 1
        elif key == "G\n":
            G += 1
        elif key == "H\n":
            H += 1
        elif key == "I\n":
            I += 1
        elif key == "J\n":
            J += 1
        elif key == "K\n":
            K += 1
        elif key == "L\n":
            L += 1
        elif key == "M\n":
            M += 1
        elif key == "N\n":
            N += 1
        elif key == "O\n":
            O += 1
        elif key == "P\n":
            P += 1
        elif key == "Q\n":
            Q += 1
        elif key == "R\n":
            R += 1
        elif key == "S\n":
            S += 1
        elif key == "T\n":
            T += 1
        elif key == "U\n":
            U += 1
        elif key == "V\n":
            V += 1
        elif key == "W\n":
            W += 1
        elif key == "X\n":
            X += 1
        elif key == "Y\n":
            Y += 1
        elif key == "Z\n":
            Z += 1

        elif key == "1\n":
            ONE += 1
        elif key == "2\n":
            TWO += 1
        elif key == "3\n":
            THREE += 1
        elif key == "4\n":
            FOUR += 1
        elif key == "5\n":
            FIVE += 1
        elif key == "6\n":
            SIX += 1
        elif key == "7\n":
            SEVEN += 1
        elif key == "8\n":
            EIGHT += 1
        elif key == "9\n":
            NINE += 1
        elif key == "0\n":
            ZERO += 1

        elif key == "=\n":
            EQUALS += 1
        elif key == "-\n":
            MINUS += 1
        elif key == "[\n":
            LBRACE += 1
        elif key == "]\n":
            RBRACE += 1
        elif key == "\\\n":
            BKWDSLASH += 1
        elif key == ";\n":
            SEMICOLON += 1
        elif key == "'\n":
            SINGLEQUOTE += 1
        elif key == ",\n":
            COMMA += 1
        elif key == ".\n":
            PERIOD += 1
        elif key == "/\n":
            SLASH += 1


        #Virtual Keys
        elif key == "[TAB]\n":
            TAB += 1
        elif key == "[CAPS]\n":
            CAPS += 1
        elif key == "[ESCAPE]\n":
            ESCAPE += 1
        elif key == "[SHIFT]\n":
            SHIFT += 1
        elif key == "[RETURN]\n":
            RETURN += 1
        elif key == "[CONTROL]\n":
            CONTROL += 1
        elif key == "[SPACE]\n":
            SPACE += 1
        elif key == "[SELECT]\n":
            SELECT += 1
        elif key == "[PRINT]\n":
            PRINT += 1
        elif key == "[EXECUTE]\n":
            EXECUTE += 1
        elif key == "[SNAPSHOT]\n":
            SNAPSHOT += 1
        elif key == "[INSERT]\n":
            INSERT += 1
        elif key == "[DELETE]\n":
            DELETE += 1
        elif key == "[HELP]\n":
            HELP += 1
        elif key == "[LWIN]\n":
            LWIN += 1
        elif key == "[RWIN]\n":
            RWIN += 1
        elif key == "[APPS]\n":
            APPS += 1
        elif key == "[SLEEP]\n":
            SLEEP += 1
        elif key == "[NUMPAD0]\n":
            NUMPAD0 += 1
        elif key == "[NUMPAD1]\n":
            NUMPAD1 += 1
        elif key == "[NUMPAD2]\n":
            NUMPAD2 += 1
        elif key == "[NUMPAD3]\n":
            NUMPAD3 += 1
        elif key == "[NUMPAD4]\n":
            NUMPAD4 += 1
        elif key == "[NUMPAD5]\n":
            NUMPAD5 += 1
        elif key == "[NUMPAD6]\n":
            NUMPAD6 += 1
        elif key == "[NUMPAD7]\n":
            NUMPAD7 += 1
        elif key == "[NUMPAD8]\n":
            NUMPAD8 += 1
        elif key == "[NUMPAD9]\n":
            NUMPAD9 += 1
        elif key == "[MULTIPLY]\n":
            MULTIPLY += 1
        elif key == "[ADD]\n":
            ADD += 1
        elif key == "[SEPERATOR]\n":
            SEPERATOR += 1
        elif key == "[SUBTRACT]\n":
            SUBTRACT += 1
        elif key == "[DECIMAL]\n":
            DECIMAL += 1
        elif key == "[DIVIDE]\n":
            DIVIDE += 1
        elif key == "[F1]\n":
            F1 += 1
        elif key == "[F2]\n":
            F2 += 1
        elif key == "[F3]\n":
            F3 += 1
        elif key == "[F4]\n":
            F4 += 1
        elif key == "[F5]\n":
            F5 += 1
        elif key == "[F6]\n":
            F6 += 1
        elif key == "[F7]\n":
            F7 += 1
        elif key == "[F8]\n":
            F8 += 1
        elif key == "[F9]\n":
            F9 += 1
        elif key == "[F10]\n":
            F10 += 1
        elif key == "[F11]\n":
            F11 += 1
        elif key == "[F12]\n":
            F12 += 1
        elif key == "[NUMLOCK]\n":
            NUMLOCK += 1
        elif key == "[SCROLL]\n":
            SCROLL += 1
        elif key == "[BACK]\n":
            BACKSPACE += 1

        elif key == "[UP]\n":
            ARROWUP += 1
        elif key == "[DOWN]\n":
            ARROWDOWN += 1
        elif key == "[ARROWLEFT]\n":
            ARROWLEFT += 1
        elif key == "[ARROWRIGHT]\n":
            ARROWRIGHT += 1

        #Mouse
        elif key == "[LBUTTON]\n":
            LBUTTON += 1
        elif key == "[RBUTTON]\n":
            RBUTTON += 1
        elif key == "[MBUTTON]\n":
            MBUTTON += 1

rangearr.append(A)
rangearr.append(B)
rangearr.append(C)
rangearr.append(D)
rangearr.append(E)
rangearr.append(F)
rangearr.append(G)
rangearr.append(H)
rangearr.append(I)
rangearr.append(J)
rangearr.append(K)
rangearr.append(L)
rangearr.append(M)
rangearr.append(N)
rangearr.append(O)
rangearr.append(P)
rangearr.append(Q)
rangearr.append(R)
rangearr.append(S)
rangearr.append(T)
rangearr.append(U)
rangearr.append(V)
rangearr.append(W)
rangearr.append(X)
rangearr.append(Y)
rangearr.append(Z)

rangearr.append(ONE)
rangearr.append(TWO)
rangearr.append(THREE)
rangearr.append(FOUR)
rangearr.append(FIVE)
rangearr.append(SIX)
rangearr.append(SEVEN)
rangearr.append(EIGHT)
rangearr.append(NINE)
rangearr.append(ZERO)

rangearr.append(TAB)
rangearr.append(SHIFT)
rangearr.append(RETURN)
rangearr.append(EQUALS)
rangearr.append(MINUS)
rangearr.append(LBRACE)
rangearr.append(RBRACE)
rangearr.append(BKWDSLASH)
rangearr.append(SEMICOLON)
rangearr.append(SINGLEQUOTE)
rangearr.append(COMMA)
rangearr.append(PERIOD)
rangearr.append(SLASH)

rangearr.append(CAPS)
rangearr.append(ESCAPE)
rangearr.append(CONTROL)
rangearr.append(SPACE)
rangearr.append(SELECT)
rangearr.append(PRINT)
rangearr.append(EXECUTE)
rangearr.append(SNAPSHOT)
rangearr.append(INSERT)
rangearr.append(DELETE)
rangearr.append(HELP)
rangearr.append(LWIN)
rangearr.append(RWIN)
rangearr.append(APPS)
rangearr.append(SLEEP)
rangearr.append(NUMPAD0)
rangearr.append(NUMPAD1)
rangearr.append(NUMPAD2)
rangearr.append(NUMPAD3)
rangearr.append(NUMPAD4)
rangearr.append(NUMPAD5)
rangearr.append(NUMPAD6)
rangearr.append(NUMPAD7)
rangearr.append(NUMPAD8)
rangearr.append(NUMPAD9)
rangearr.append(MULTIPLY)
rangearr.append(ADD)
rangearr.append(SEPERATOR)
rangearr.append(SUBTRACT)
rangearr.append(DECIMAL)
rangearr.append(DIVIDE)
rangearr.append(F1)
rangearr.append(F2)
rangearr.append(F3)
rangearr.append(F4)
rangearr.append(F5)
rangearr.append(F6)
rangearr.append(F7)
rangearr.append(F8)
rangearr.append(F9)
rangearr.append(F10)
rangearr.append(F11)
rangearr.append(F12)
rangearr.append(NUMLOCK)
rangearr.append(SCROLL)
rangearr.append(BACKSPACE)

rangearr.append(ARROWUP)
rangearr.append(ARROWDOWN)
rangearr.append(ARROWLEFT)
rangearr.append(ARROWRIGHT)

rangelimitint = (max(rangearr))/510

keyboardimg = Image.open(keyboardwithmouse)
keyboardimgcpy = Image.open(keyboardwithmouse)

def overlaySQR(img, letter, coords1):
    coords2 = tuple(numpy.add(coords1, (23, 23)))
    letter = int(letter/rangelimitint)
    rgb2 = 255
    rgb3 = 255
    if letter > 255:
        rgb2 = 255-(letter-255)
        rgb3 = 0
    else:
        rgb2 = 255
        rgb3 = 255-letter
    img = ImageDraw.Draw(keyboardimg)
    img.rectangle(coords1 + coords2, fill=(255, rgb2, rgb3))

def overlayGEN(img, letter, coords1, coords2):
    letter = int(letter/rangelimitint)
    rgb2 = 255
    rgb3 = 255
    if letter > 255:
        rgb2 = 255-(letter-255)
        rgb3 = 0
    else:
        rgb2 = 255
        rgb3 = 255-letter
    img = ImageDraw.Draw(keyboardimg)
    img.rectangle(coords1 + coords2, fill=(255, rgb2, rgb3))

yellow = (255,255,0)
orange = (255, 165, 0)
red = (255,0,0)

draw = ImageDraw.Draw(keyboardimg)

overlaySQR(draw, A, (75, 125))
overlaySQR(draw, B, (230, 161))
overlaySQR(draw, C, (161, 161))
overlaySQR(draw, D, (144, 125))
overlaySQR(draw, E, (127, 89))
overlaySQR(draw, F, (178, 124))
overlaySQR(draw, G, (213, 125))
overlaySQR(draw, H, (248, 125))
overlaySQR(draw, I, (301, 88))
overlaySQR(draw, J, (283, 125))
overlaySQR(draw, K, (318, 125))
overlaySQR(draw, L, (352, 125))
overlaySQR(draw, M, (300, 161))
overlaySQR(draw, N, (265, 161))
overlaySQR(draw, O, (336, 88))
overlaySQR(draw, P, (371, 88))
overlaySQR(draw, Q, (57, 88))
overlaySQR(draw, R, (162, 88))
overlaySQR(draw, S, (110, 125))
overlaySQR(draw, T, (197, 88))
overlaySQR(draw, U, (266, 88))
overlaySQR(draw, V, (196, 161))
overlaySQR(draw, W, (93, 88))
overlaySQR(draw, X, (126, 161))
overlaySQR(draw, Y, (231, 88))
overlaySQR(draw, Z, (92, 161))

overlaySQR(draw, ONE, (40, 52))
overlaySQR(draw, TWO, (75, 52))
overlaySQR(draw, THREE, (110, 52))
overlaySQR(draw, FOUR, (145, 52))
overlaySQR(draw, FIVE, (180, 52))
overlaySQR(draw, SIX, (215, 52))
overlaySQR(draw, SEVEN, (250, 52))
overlaySQR(draw, EIGHT, (285, 52))
overlaySQR(draw, NINE, (320, 52))
overlaySQR(draw, ZERO, (355, 52))

overlaySQR(draw, EQUALS, (422, 52))
overlaySQR(draw, MINUS, (387, 52))
overlaySQR(draw, LBRACE, (405, 88))
overlaySQR(draw, RBRACE, (440, 88))
overlayGEN(draw, BKWDSLASH, (475, 88), (531, 111))
overlaySQR(draw, SEMICOLON, (387, 125))
overlaySQR(draw, SINGLEQUOTE, (422, 125))
overlaySQR(draw, COMMA, (335, 161))
overlaySQR(draw, PERIOD, (370, 161))
overlaySQR(draw, SLASH, (405, 161))

#Virtual Keys
overlayGEN(draw, TAB, (5, 88), (46, 112))
overlayGEN(draw, CAPS, (6, 125), (63, 148))
overlayGEN(draw, ESCAPE, (3, 26), (29, 42))
overlayGEN(draw, SHIFT, (6, 161), (80, 184))
overlayGEN(draw, SHIFT, (440, 161), (530, 183))
overlayGEN(draw, RETURN, (458, 125), (530, 148))
overlaySQR(draw, CONTROL, (5, 197))
overlaySQR(draw, CONTROL, (405, 197))
overlayGEN(draw, SPACE, (146, 197), (323, 220))
overlayGEN(draw, SNAPSHOT, (338, 2), (366, 19))
overlayGEN(draw, INSERT, (440, 2), (467, 19))
overlayGEN(draw, DELETE, (440, 26), (467, 42))
overlaySQR(draw, RWIN, (75, 197))
overlaySQR(draw, LWIN, (75, 197))
overlaySQR(draw, EXECUTE, (109, 197))
overlaySQR(draw, EXECUTE, (335, 197))
overlayGEN(draw, BACKSPACE, (458, 53), (531, 76))


overlayGEN(draw, F1, (36, 25), (63, 41))
overlayGEN(draw, F2, (69, 25), (96, 41))
overlayGEN(draw, F3, (103, 25), (130, 41))
overlayGEN(draw, F4, (137, 25), (164, 41))
overlayGEN(draw, F5, (170, 25), (197, 41))
overlayGEN(draw, F6, (204, 25), (231, 41))
overlayGEN(draw, F7, (238, 25), (265, 41))
overlayGEN(draw, F8, (271, 25), (298, 41))
overlayGEN(draw, F9, (305, 25), (332, 41))
overlayGEN(draw, F10, (338, 25), (365, 41))
overlayGEN(draw, F11, (372, 25), (399, 41))
overlayGEN(draw, F12, (405, 25), (432, 41))


overlayGEN(draw, ARROWUP, (473, 194), (498, 211))
overlayGEN(draw, ARROWDOWN, (473, 217), (498, 234))
overlayGEN(draw, ARROWLEFT, (441, 217), (466, 234))
overlayGEN(draw, ARROWRIGHT, (506, 217), (529, 234))

overlayGEN(draw, MBUTTON, (601, 80), (613, 95))
overlayGEN(draw, LBUTTON, (582, 80), (600, 100))
overlayGEN(draw, RBUTTON, (614, 76), (631, 100))

# Later use floodfill
# img2 = ImageDraw.Draw(keyboardimg)
# ImageDraw.floodfill(img2, (594, 89), LBUTTON, border=None, thresh=50)

alphaBlended = Image.blend(keyboardimg, keyboardimgcpy, alpha=.3)
alphaBlended.show()