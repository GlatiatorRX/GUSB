# import the pygame module, so you can use it
import pygame

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

    x = 50
    y = 425
    width = 40
    height = 60
    vel = 5

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
        if keys[pygame.K_RIGHT] and x < 500 - width - vel:
            x += vel
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < 500 - height - vel:
            y += vel

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
        pygame.display.update()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
