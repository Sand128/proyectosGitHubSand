import pygame
import sys

#Inicializar Pygame 
pygame.init()

#Configuración de la pantalla
width, height =800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mi Juego")

#Colores
black =(0,0,0)
white =(255,255,255)

#Jugador
player_size = 50
player_x = width // 2 -player_size // 2
player_y = height - 2 * player_size
player_speed = 5 

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

    #Bucle principal del juego 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #Obtener las teclas presionadas
        keys = pygame.key.get_pressed()

        #Mover al jugador
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -=player_speed
        if keys[pygame.K_RIGHT] and player_x < width - player_size:
            player_x +=player_speed

        #Limpiar la pantalla
        screen.fill(black)
        
        #Dibujar al jugador
        pygame.draw.rect(screen, white, (player_x, player_y, player_size, player_size))

        #Actualizar la pantalla
        pygame.display.flip()

        #Controlar l avelocidad de actualizacion
        pygame.time.Clock().tick(30)