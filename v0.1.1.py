import dearpygui.dearpygui as dpg
import PLN  

dpg.create_context()
dpg.create_viewport(title='Interpretador Mereketengue', width=1280, height=720)
dpg.setup_dearpygui()

fullscreen_bool = 0

def analisis():
    frase_ingresada = dpg.get_value("string_value")
    print(PLN.analisis_texto(frase_ingresada))

def change_to_fullscreen():
    dpg.toggle_viewport_fullscreen()
    global fullscreen_bool
    fullscreen_bool = 1

def change_resolution(width_int, height_int):
    dpg.configure_viewport('Interpretador Mereketengue', width = width_int, height = height_int)
    global fullscreen_bool
    if fullscreen_bool == 1:    
        dpg.toggle_viewport_fullscreen()
        fullscreen_bool = 0



with dpg.viewport_menu_bar():
    with dpg.menu(label="Configuracion"):
        with dpg.menu(label="Resolucion"):
            dpg.add_menu_item(label="Pantalla Completa", callback=lambda:change_to_fullscreen())
            dpg.add_menu_item(label="1280x720", callback=lambda:change_resolution(1280,720))
            dpg.add_menu_item(label="1920x1080", callback=lambda:change_resolution(1920,1080))

    with dpg.window(label="Entrada de texto",autosize = True, no_move = True, no_close = True):

        dpg.add_input_text(label="Ingrese su frase", tag="string_value")
        dpg.add_button(label="Ok", callback=analisis)



dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
    
