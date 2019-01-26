# import the pygame module, so you can use it
import pygame


def redrawGameWindow(screen, x, y, width, height, walkCount):
    # screen.blit(bg, (0, 0))  # if we have the floor/background
    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        screen.blit(walkCount//3)
    pygame.display.update()

# define a main function


def main():

    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Big weiner game")

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((500, 500))

    # define a variable to control the main loop
    running = True

    # add more to the array if you want frames
    walkLeft = [pygame.image.load('Sprites/Player/Player_Left.png')]
    walkRight = [pygame.image.load('Sprites/Player/Player_Right.png')]
    walkUp = [pygame.image.load('Sprites/Player/Player_Up.png')]
    walkDown = [pygame.image.load('Sprites/Player/Player_Down.png')]
    #char = pygame.image.load('standing.png')

    x = 50
    y = 425
    width = 64
    height = 64
    vel = 5
    left = False
    right = False
    up = False
    down = False
    walkCount = 0

    # main loop
    while running:
        pygame.time.delay(100)
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x > vel:
            x -= vel
            left = True
            right = False
        elif keys[pygame.K_RIGHT] and x < 500 - width - vel:
            x += vel
            left = False
            right = True
        if keys[pygame.K_UP] and y > vel:
            up = True
            down = False
        elif keys[pygame.K_DOWN] and y < 500 - height - vel:
            up = False
            down = True

        redrawGameWindow(screen, x, y, width, height, walkCount)


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
