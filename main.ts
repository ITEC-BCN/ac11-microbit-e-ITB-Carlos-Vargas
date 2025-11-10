let end = false
let botonA = false
let botonB = false
let tem = 0
let x = 2
let y = 2
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    botonB = false
    botonA = true
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    botonA = false
    botonB = true
})
basic.forever(function on_forever() {
    let accX: number;
    let accY: number;
    
    tem = input.temperature()
    if (botonA) {
        led.plotBarGraph(tem, 50, true)
    } else if (botonB) {
        accX = input.acceleration(Dimension.X)
        accY = input.acceleration(Dimension.Y)
        //  Movimiento horizontal (X)
        if (accX <= 150 && x > 0) {
            x = x - 1
        } else if (accX > 150 && x < 4) {
            x = x + 1
        }
        
        //  Movimiento vertical (Y)
        if (accY <= 150 && y > 0) {
            y = y - 1
        } else if (accY > 150 && y < 4) {
            y = y + 1
        }
        
        basic.clearScreen()
        led.plot(x, y)
        basic.pause(100)
    }
    
})
