import dearpygui.dearpygui as dpg
import PLN, os  

fullscreen_bool = 0

def analisis():
    frase_ingresada = dpg.get_value("string_value")
    PLN.analisis_texto(frase_ingresada)

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

def abrir_historial():
    dir_f = os.getcwd() + "\Historial"
    os.system(f'start {os.path.realpath(dir_f)}')

dpg.create_context()


with dpg.window(tag="Main Window",):
    with dpg.menu_bar():
        with dpg.menu(label="Opciones"):
            with dpg.menu(label="Resolucion"):
                dpg.add_menu_item(label="Pantalla Completa", callback=lambda:change_to_fullscreen())
                dpg.add_menu_item(label="1280x720", callback=lambda:change_resolution(1280,720))
                dpg.add_menu_item(label="1920x1080", callback=lambda:change_resolution(1920,1080))

        with dpg.menu(label="Historial"):
            dpg.add_menu_item(label="Abrir en Ubicacion", callback=abrir_historial)
            dpg.add_menu_item(label="Borrar Historial")
             
        with dpg.menu(label="Ayuda"):
            dpg.add_menu_item(label="Documentacion")

    dpg.add_input_text(label="Ingrese su frase", tag="string_value", on_enter = True, width = 500, callback=analisis)
    dpg.add_button(label="Ok", callback=analisis)


dpg.create_viewport(title='Interpretador Mereketengue', width=1280, height=720)
dpg.set_primary_window("Main Window", True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
