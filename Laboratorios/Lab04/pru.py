import pygame, math, sys, random

#variables
bgColour = (0,0,0)
width, height = 1280, 720
globalGravity = 1000
FPS = 500
totalParticles = 444
particleTrail = True
maxVelocity = 1

#setup
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Gravity Sim')
screen.fill(bgColour)
mainClock = pygame.time.Clock()

#classes and functions
class Particle:
    def __init__(self, x, y, size, e, gravity = globalGravity): #e is coefficient of restitution 
        self.x = x
        self.y = y
        self.size = size
        self.e = e
        self.velocity = 0
        self.maxVelocity = math.sqrt(2*gravity*(height-y-size))
        self.gravity = gravity
            
    def render(self):
        self.colourVelocity = 255 - round(math.fabs(self.velocity) / maxVelocity * 255)
        if self.colourVelocity > 255:
            self.colourVelocity = 255
        if self.colourVelocity < 0:
            self.colourVelocity = 0
        pygame.draw.circle(screen, (random.randint(1,255),self.colourVelocity,self.colourVelocity), (self.x, round(self.y)), self.size)
    
    def delete(self):
        pygame.draw.circle(screen, (0,0,0), (self.x, round(self.y)), self.size)
    



def terminate():
    pygame.quit()
    sys.exit()
   
def createParticles():
    particleList = []    
    for n in range(1,1+totalParticles):
        particle = Particle(int(width/(1+totalParticles) * (n)), random.randint(10,50), random.randint(1,3),  random.random(), random.randint(500,2000))
        particleList.append(particle)
    for particle in particleList:
        particle.render()
    return particleList


#begin
particleList = createParticles()

#running loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.KEYDOWN:
            if event.key == ord('r'): #reset
                screen.fill(bgColour)
                particleList = createParticles()    
    for particle in particleList:
        if particle.maxVelocity > maxVelocity:
            maxVelocity = particle.maxVelocity
        if not particleTrail:
            particle.delete()
        if particle.y < height - (particle.size):
            particle.velocity += (1/FPS) * particle.gravity            
        else:
            particle.y = height - particle.size
            particle.velocity = -1 * particle.velocity * particle.e
        particle.y += particle.velocity * (1/FPS)
        particle.render()
    pygame.display.update()
    mainClock.tick(FPS)
    

