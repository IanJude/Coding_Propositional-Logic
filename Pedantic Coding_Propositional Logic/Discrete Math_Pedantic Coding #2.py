def transfer_to_resource(rain,gauge,pool):
    if pool>=10 or rain_gauge>=10:
        pool +=2
        rain_gauge +=10
    return pool, rain_gauge
