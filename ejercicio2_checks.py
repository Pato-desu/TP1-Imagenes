def check(linea, n_car, n_pal):
    match linea:
        case 1:  
            if n_pal > 1 and n_car < 26:
                return True
            
        case 2:
            if n_pal == 1 and n_car in [2, 3]:
                return True
        
        case 3:
            if n_pal == 1 and n_car < 26:
                return True
                
        case 4:
            if n_pal == 1 and n_car == 8:
                return True
        # FALTA VER COMO HACER ESTE:
        case 5:                 
            # if n_pal == 2 and n_car < 26: 
                return True
                    
        case 6:
            if n_car < 26:
                return True       
            
    return False
        