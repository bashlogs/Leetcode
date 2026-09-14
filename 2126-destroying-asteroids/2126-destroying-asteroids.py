class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()

        for asteroid in asteroids:
            if mass >= asteroids[-1]:
                return True
            elif mass >= asteroid:
                mass += asteroid
            else:
                return False
        
        return True