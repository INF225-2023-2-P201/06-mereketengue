import dearpygui.dearpygui as dpg
import PLN, os

fullscreen_bool = 0

def borrar_historial():
    if dpg.does_item_exist("Pupup_historial"):
        children_dict = dpg.get_item_children("Pupup_historial")
        for key in children_dict.keys():
            for child in children_dict[key]:
                dpg.delete_item(child)

        dpg.delete_item("Pupup_historial")
    else:
        with dpg.window(
                tag="Pupup_historial",
                width=200,
                height=200,
                pos=[150, 25],
                autosize=True,
                no_move=False,
                no_title_bar=True,
                no_collapse=True,
                no_focus_on_appearing=True,
                no_bring_to_front_on_focus=False,
                no_close=False):

            dpg.add_text("¿Seguro que desea borrar el historial?", bullet = True)
            with dpg.group(horizontal=True, pos = [100,50]):
                dpg.add_button(label="Si", width=50, callback = borrar_historial_hijo)
                dpg.add_button(label="No", width=50, callback = borrar_historial)

def on_window_close(sender):
    children_dict = dpg.get_item_children(sender)
    for key in children_dict.keys():
        for child in children_dict[key]:
            dpg.delete_item(child)

    dpg.delete_item(sender)

def add_text(tupl_text):
    for e in tupl_text:
        if e[1] == 2:
            add_text_to_console(e[0])
        elif e[1] == 0:
            add_goog_msg_to_console(e[0])
        else:
            add_error_msg_to_console(e[0])

def add_text_to_console(text):
    dpg.add_text(text, parent="console_window")
    dpg.set_y_scroll("console_window", dpg.get_y_scroll_max("console_window"))

def add_error_msg_to_console(text):
    dpg.add_text("[error] " + text , parent="console_window", color=(196, 43, 43))
    dpg.set_y_scroll("console_window", dpg.get_y_scroll_max("console_window"))
    
def add_goog_msg_to_console(text):
    dpg.add_text(text, parent="console_window", color=(69, 214, 69))
    dpg.set_y_scroll("console_window", dpg.get_y_scroll_max("console_window"))

def borrar_historial_hijo():    
    for filename in os.listdir('Historial'):
        if os.path.isfile(os.path.join('Historial', filename)):
            os.remove(os.path.join('Historial', filename))
    borrar_historial()

def analisis():
    frase_ingresada = dpg.get_value("string_value")
    tupl_text = PLN.analisis_texto(frase_ingresada)
    add_text(tupl_text)

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
            dpg.add_menu_item(label="Borrar Historial", callback=borrar_historial)
             
        with dpg.menu(label="Ayuda"):
            dpg.add_menu_item(label="Documentacion")

    dpg.add_input_text(label="Ingrese su frase", tag="string_value", on_enter = True, width = 500, callback=analisis)
    dpg.add_button(label="Ok", callback=analisis)
    with dpg.child_window(label="Console", pos = [7,73], horizontal_scrollbar=True, width=500, height=300, tag="console_window"):
        pass

dpg.create_viewport(title='Interpretador Mereketengue', width=1280, height=720)
dpg.set_primary_window("Main Window", True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
