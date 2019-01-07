

def drawLine(x0,y0,x1,y1):

    steep = abs(y1 - y0) > abs(x1 - x0)
    
    if steep:
        swap(x0, y0)
        swap(x1, y1)
    if x0 > x1:
        swap(x0, x1)
        swap(y0, y1)
    
    
    dx = x1 - x0
    dy = y1 - y0
    gradient = dy / dx
    if dx == 0.0:
        gradient = 1.0


    #  handle first endpoint
    x_pair = modf(x0)
    y_pair = modf(y0)
    x_pair[1] = int(x_pair[1])
    y_pair[1] = int(y_pair[1])
    xend = x_pair[1]
    yend = y0 + gradient * (xend - x0)
    xgap =  + 0.5)
    xpxl1 = xend #  this will be used in the main loop
    ypxl1 = ipart(yend)
    if steep:
        plot(ypxl1,   xpxl1, rfpart(yend) * xgap)
        plot(ypxl1+1, xpxl1,  fpart(yend) * xgap)
    else:
        plot(xpxl1, ypxl1  , rfpart(yend) * xgap)
        plot(xpxl1, ypxl1+1,  fpart(yend) * xgap)
    
    intery = yend + gradient #  first y-intersection for the main loop
    
    #  handle second endpoint
    xend = math.round(x1)
    yend = y1 + gradient * (xend - x1)
    xgap = fpart(x1 + 0.5)
    xpxl2 = xend # this will be used in the main loop
    ypxl2 = ipart(yend)
    if steep:
        plot(ypxl2  , xpxl2, rfpart(yend) * xgap)
        plot(ypxl2+1, xpxl2,  fpart(yend) * xgap)
    else:
        plot(xpxl2, ypxl2,  rfpart(yend) * xgap)
        plot(xpxl2, ypxl2+1, fpart(yend) * xgap)

    
    #  main loop
    if steep:
        for x in range(xpxl1 + 1 to xpxl2):
                plot(ipart(intery)  , x, rfpart(intery))
                plot(ipart(intery)+1, x,  fpart(intery))
                intery = intery + gradient
           end
    else:
        for x in range(xpxl1 + 1, xpxl2):
                plot(x, ipart(intery),  rfpart(intery))
                plot(x, ipart(intery)+1, fpart(intery))
                intery = intery + gradient


