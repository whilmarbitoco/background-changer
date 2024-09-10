import ctypes
path = "C:/omalay.jpg"
SPI_SETDESKWALLPAPER = 20


ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path , 0)