import pygame

with open ("text", "r") as f:
    sheet = f.read()

arr = sheet.split(" ")

linelimit = 50

cheat = []

au = 0
for i in range((len(arr)//linelimit)+1):
    sheet = (" ".join(arr[au:au+linelimit]))
    au += linelimit
    cheat.append(sheet)

cheat = "\n".join(cheat)

# Initialize pygame
pygame.init()
# clock
clock = pygame.time.Clock()

# Create the screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


def blit_text(surface, text, pos, font, color=pygame.Color('white')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

#main loop
while True:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # fill the screen with black
    screen.fill((0, 0, 0))
    
    #detect if G is pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_g]:
        # paint text
        font = pygame.font.SysFont(None, 25)
        text = font.render(str(cheat), True, (255, 255, 255))
        blit_text(screen, cheat, (0, 0), font)

    #use clock to limit the fps
    clock.tick(60)
    # Update the screen
    pygame.display.update()