def http_status(status):

    match status:

        case 200:
            return "Unknown error"
        
        case 400:
            return "Error!!!"
        
        case 505:
            return "Can't open this site"
        
        case _:
            return "Something else happened"
        
                
print(http_status(300))
