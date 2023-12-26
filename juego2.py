import pygame
import sys
import random

pygame.init()

#configuracion de la pantalla
width,height=600,400
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake Game")

#colores
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)

#tamaño de la serpiente
block_size=20

snake=[(width//2,height//2)]
snake_direction=(1,0)

food=(random.randint(0,(width-block_size)//block_size)*block_size,
      random.randint(0,(height-block_size)//block_size)*block_size)

speed=10

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def main_menu():
    menu_font = pygame.font.Font(None, 36)
    title_font = pygame.font.Font(None, 72)

    while True:
        screen.fill(black)
        draw_text("Bienvenido a mi juego" , title_font , white, width // 2, height // 4)
        draw_text("Presiona Enter para empezar", menu_font, white, width // 2, height // 2)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

if __name__ == "__main__":
    main_menu()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys=pygame.key.get_pressed()

    if keys[pygame.K_UP] and snake_direction !=(0,1):
        snake_direction=(0,-1)
    elif keys[pygame.K_DOWN]and snake_direction !=(0,-1):
        snake_direction=(0,1)
    elif keys[pygame.K_LEFT]and snake_direction !=(1,0):
        snake_direction=(-1,0)
    elif keys[pygame.K_RIGHT]and snake_direction !=(-1,0):
        snake_direction=(1,0)
    
    new_head=(snake[0][0]+snake_direction[0]*block_size,
              snake[0][1]+snake_direction[1]*block_size)
    #comprobar colisiones con la pared
    if not(0<=new_head[0]<width and 0<=new_head[1]<height):
        pygame.quit()
        sys.exit()
    
    #comparar colisiones con la cola
    if new_head in snake[1:]:
        pygame.quit()
        sys.exit()

    #comprobar colisiones con la comida
    if new_head==food:
        food=(random.randint(0,(width-block_size)//block_size)*block_size,
        random.randint(0,(height-block_size)//block_size)*block_size)
    else:
        snake.pop()
    
    #actualizar la posicion de la serpiente
    snake.insert(0,new_head)

    #limpiar la pantalla
    screen.fill(black)

    #dibujar la serpiente
    for segment in snake:
        pygame.draw.rect(screen,white,(segment[0],segment[1],block_size,block_size))
    
    #dibujar la comida
    pygame.draw.rect(screen,red,(food[0],food[1],block_size,block_size))

    #actualizar pantalla
    pygame.display.flip()

    #Controlar la velicidad de la actualizacion
    pygame.time.Clock().tick(speed)
