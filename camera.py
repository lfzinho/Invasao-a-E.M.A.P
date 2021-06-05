import pygame

char = {
	"pos": [10, 10],
	"color": (0, 0, 0)}

class camera:
    def __init__(self, pos, props):
        self._pos = pos
        self._props = props
    
    def render(self, o_coord):
        n_coord = [0, 0]
    
        n_coord[0] = o_coord[0] - self._pos[0] + self._props[0]/2
        n_coord[1] = o_coord[1] - self._pos[1] + self._props[1]/2
        return n_coord
    
    @property
    def pos(self):
        return self._pos
    
    @property
    def props(self):
        return self._props
	
    @pos.setter
    def pos(self, pos):
        self._pos = pos


         
cam = camera([0, 0], (400, 400))


pygame.init()

win = pygame.display.set_mode(cam.props)

pygame.display.set_caption("Game")

run = True
while run:

    for event in pygame.event.get():
        
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            run = False

    if keys[pygame.K_LEFT]:
        char['pos'][0] -= 0.03
    
    if keys[pygame.K_RIGHT]:
        char['pos'][0] += 0.03
        
    if keys[pygame.K_UP]:
        char['pos'][1] -= 0.03
    
    if keys[pygame.K_DOWN]:
        char['pos'][1] += 0.03
	
    cam.pos = [char['pos'][0]+5+(pygame.mouse.get_pos()[0]-cam.props[0]/2)/5, \
                      char['pos'][1]+5+(pygame.mouse.get_pos()[1]-cam.props[1]/2)/5]
    
    win.fill((156, 132, 109))
    pygame.draw.circle(win, (120, 91, 76), cam.render((50, 50)), 20)
    pygame.draw.circle(win, char["color"], cam.render(char["pos"]), 10)
    pygame.draw.rect(win, (50, 252, 108), (5, 5, 150, 10))

    pygame.display.update()

pygame.quit()
	
