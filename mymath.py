class Math:
    
    def tri(self, height, base):
        result = height * base / 2
        return result
    
    def cir(self, radius):
        result = 3.14  * radius ** 2
        return result
    
    def cub(self, width, height, depth):
        return 2 * (width * height + width * depth + height * depth)
