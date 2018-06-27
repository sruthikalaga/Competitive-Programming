
def RectangleCut(r1, r2):

    xaxis1 = r1['left_x'] + r1['width']
    
    xaxis2=r2['left'] + r2['width']
    
    yaxis1=r1['bot'] + r1['height']
    
    yaxis2=r2['bot'] + r2['height']
    
    xaxis0=max(r1['left'], r2['left'])
    
    yaxis0=max(r1['bot'], r2['bottom'])
    
    width=min(xaxis1,xaxis2)-xaxis0
    
    height=min(yaxis1,yaxis2)-yaxis0
    
    if((xaxis1<=r2['left'] and yaxis1<=r2['bot'])
    
        or ((yaxis1 or r1['bot'])==r2['bot'])
        
        or (xaxis1 or r1['left'] )==r2['left']):
        return{
        
            'left': None,
            'bot': None,
            'width': None,
            'height': None,
        }

    return {
    
            'left': xaxis0,
            'bottom': yaxis0,
            'width': width,
            'height': height,
        }
