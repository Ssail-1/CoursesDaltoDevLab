# ---------------------------------------------------------------
# game.py — Primer contacto con Pygame
# Este archivo crea una ventana simple con un mensaje.
# Todo está comentado para que entiendas el propósito de cada línea.
# ---------------------------------------------------------------

import pygame      # Motor de videojuegos 2D
import sys         # Usado para salir limpiamente del programa

def main():
    """
    Función principal del juego.
    Aquí inicia el programa REAL.
    """

    # -----------------------------------------------------------
    # 1. Inicializar pygame
    #    Esto configura video, audio, fuentes, eventos, etc.
    # -----------------------------------------------------------
    pygame.init()

    # -----------------------------------------------------------
    # 2. Crear una ventana (Surface principal)
    #    - ANCHO y ALTO se definen en pixeles.
    #    - display.set_mode() devuelve una superficie donde dibujar.
    # -----------------------------------------------------------
    ANCHO, ALTO = 800, 500
    screen = pygame.display.set_mode((ANCHO, ALTO))

    # -----------------------------------------------------------
    # 3. Título de la ventana
    # -----------------------------------------------------------
    pygame.display.set_caption("Hola Pygame — Seed del Challenge")

    # -----------------------------------------------------------
    # 4. Reloj interno para controlar FPS (cuadros por segundo)
    # -----------------------------------------------------------
    clock = pygame.time.Clock()

    # -----------------------------------------------------------
    # 5. Colores (R, G, B)
    # -----------------------------------------------------------
    COLOR_FONDO = (20, 20, 28)  # un gris oscuro elegante
    COLOR_TEXTO = (240, 240, 240)

    # -----------------------------------------------------------
    # 6. Fuente para el texto en pantalla
    #    pygame.font.get_default_font() devuelve una fuente genérica.
    # -----------------------------------------------------------
    fuente = pygame.font.Font(pygame.font.get_default_font(), 26)

    # -----------------------------------------------------------
    # 7. Crear un texto renderizado como Surface
    #    Este texto se puede "blittear" (dibujar) en la pantalla.
    # -----------------------------------------------------------
    texto = fuente.render(
        "Instalación exitosa. Presiona ESC para salir.",
        True, 
        COLOR_TEXTO
    )

    # -----------------------------------------------------------
    # 8. Bucle principal del juego
    #    Este bucle corre mientras el juego esté activo.
    # -----------------------------------------------------------
    while True:

        # -------------------------------------------------------
        # 8.1 Procesamiento de eventos
        #     Aquí detectamos teclas, clicks, cerrar ventana, etc.
        # -------------------------------------------------------
        for event in pygame.event.get():

            # Si cerraron la ventana (X)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Si se presiona una tecla...
            if event.type == pygame.KEYDOWN:

                # Si esa tecla es ESC → cerrar juego
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # -------------------------------------------------------
        # 8.2 Dibujar en pantalla
        # -------------------------------------------------------

        screen.fill(COLOR_FONDO)        # Rellenar toda la ventana con un color
        screen.blit(texto, (20, 20))     # Dibujar el texto en la posición x=20, y=20

        # -------------------------------------------------------
        # 8.3 Actualizar pantalla
        # -------------------------------------------------------
        pygame.display.flip()

        # -------------------------------------------------------
        # 8.4 Ajustar la velocidad del bucle (60 FPS)
        # -------------------------------------------------------
        clock.tick(60)


# ---------------------------------------------------------------
# 9. Punto de entrada
#    Esto asegura que "main()" sólo corra si este archivo se ejecuta directamente.
# ---------------------------------------------------------------
if __name__ == "__main__":
    main()
