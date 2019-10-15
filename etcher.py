import gfxhat
import PIL
from gfxhat import lcd,  fonts
from PIL import Image, ImageFont, ImageDraw

#this function will display text on the gfxhat that will say "Etch a Sketch" somewhere on the screen

def clearScreen(lcd):
    lcd.clear()
    lcd.show()

def displayText(text,lcd,x,y):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 24)
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show() 


#this function will turn on the pixel that the x and y cordinates are set on

def drawPixel(x,y)
    x = range(0,128)
    y = range(0,64)
    lcd.clear()
    lcd.set_pixel(x,y,1)
    lcd.show() 

from gfxhat import lcd

#this function will make a range of cordinates on the gfxhat and makes it so 
#if you go off the left side of the screen you would continue drawing on the right side

def rangeOfScreen(x,y)
    x = range(0,128)
    y = range(0,64)
    for x = >127
      set x = 0
    for x = <0 
      set x = 127
    for y = >63
      set y = 0
    for y = <0
      set y = 63
  
import click

#this function will draw a pixel one unit up when you press the up arrow

def up(\x1b[A)
click.echo('\x1b[A')

#this function will draw a pixel one unit to the left when you press the left arrow

def left(\x1b[D)
click.echo('\x1b[D')

#this function will draw a pixel one unit to the right when you press the right arrow

def right(\x1b[C) 
click.echo('\x1b[C')

#this function will draw a pixel one unit down when you press the down arrow

def down(\x1b[B)
click.echo('\x1b[B')

#this function will reset the screen when you click the s key

def reset()
click.echo()

# this function will quit the program when you click the q key

def quit()
click.echo()

#this function will display two diferent images on the gfxhat, it will promt you 
#too imput the cordinates of where you want the image to be there are 2 diferent images 

def displayObject(obj,x1,y1,x2,y2)

x1 = range(0,128)
y1 = range(0,64)

x1 = input("enter x cordinate here for 1st image")
y1 = input("enter y cordinate here for 1st image")

def f1(x1,y1)

f1 =  [
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,0],
[1,0,1,1,1,1,0,1],
[1,0,0,1,1,0,0,1],
[1,0,0,1,1,0,0,1],
[0,0,0,1,1,0,0,0],
[0,0,0,0,0,0,0,0]
]

x2 = range(0,128)
y2 = range(0,64)

x2 = input("enter x cordinate here for 2nd image")
y2 = input("enter y cordinate here for 2nd image")

def pm(x2,y2)
pm = [[0,0,0,1,1,1,1,1,0,0,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[1,1,1,1,1,1,1,1,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,1,1,0,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,0,0,1,1,1,1,1,0,0,0]
]