end = False
botonA = False
botonB = False
tem = 0
x = 2
y = 2


def on_button_pressed_a():
    global botonA, botonB
    botonB = False
    botonA = True
   
    
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global  botonA, botonB
    botonA = False
    botonB = True
   
   
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    global tem, botonA, botonB, x, y
    tem = input.temperature()
    if botonA: 
        led.plot_bar_graph(tem, 50, True)
    elif botonB:
        
        accX = input.acceleration(Dimension.X)
        accY = input.acceleration(Dimension.Y)
       
        # Movimiento horizontal (X)
        if accX <= 150 and x > 0:
            x = x - 1
        elif accX > 150 and x < 4:
            x = x + 1

        # Movimiento vertical (Y)
        if accY <= 150 and y > 0:
            y = y - 1
        elif accY > 150 and y < 4:
            y = y + 1
        basic.clear_screen()
        led.plot(x, y)
        basic.pause(50)

        

basic.forever(on_forever)
