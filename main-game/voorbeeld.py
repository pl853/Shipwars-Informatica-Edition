def mouse_button_pressed(x,y,w,h,ci,ca):
    click=pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(red,[x,y])
    else:
        pygame.draw.rect(black,[x,y])
