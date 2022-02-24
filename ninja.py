import pygame

if __name__ == '__main__':
    pygame.init()
    size = width,height = 501,501
    screen = pygame.display.set_mode(size)
    board = Board(5,7)
    running = True
    pygame.display.flip()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0,0,0))
        board.render(screen)
        board.set_view(100, 100, 50)
        pygame.display.flip()
    pygame.quit()