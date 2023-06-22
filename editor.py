import flet as ft # Installez avec "pip install flet"
import flet.canvas as cv

OFFSET_X, OFFSET_Y = 100, 100
COLORMAP = {
    "rouge": "#FF0000",
    "noir": "#000000",
    "jaune": "#FFFF00",
    "bleu": "#0000FF",
    "vert": "#00FF00",
}

x,y = None, None
mouse_x, mouse_y = 0, 0
map = []
canvas = None
color = None

def set_red(_):
    global color
    color = "rouge"

def set_blue(_):
    global color
    color = "bleu"

def set_green(_):
    global color
    color = "vert"

def set_yellow(_):
    global color
    color = "jaune"

def set_color_None(_):
    global color
    color = None

def read_map(path):
    global map
    if map is None:
        map = []
    map[:] = []
    with open(path, "r", encoding="utf-8") as f:
        lines = [l for l in f.read().splitlines() if l.strip()]
        for line in lines:
            color = None
            try:
                name, xmin, ymin, xmax, ymax = line.split()
            except ValueError:
                name, xmin, ymin, xmax, ymax, color = line.split()
            map.append([int(xmin), int(ymin), int(xmax), int(ymax), color])
    draw_map()

def draw_map():
    global canvas
    canvas.shapes[:] = []
    for xmin, ymin, xmax, ymax, color in map:
        if color:
            canvas.shapes.append(
                cv.Rect(
                    xmin + OFFSET_X,
                    ymin + OFFSET_Y,
                    xmax - xmin,
                    ymax - ymin,
                    paint=ft.Paint(
                        stroke_width=3,
                        style=ft.PaintingStyle.FILL,
                        color=COLORMAP[color],
                    ),
                )
            )
        canvas.shapes.append(
            cv.Rect(
                xmin + OFFSET_X,
                ymin + OFFSET_Y,
                xmax - xmin,
                ymax - ymin,
                paint=ft.Paint(
                    stroke_width=3,
                    style=ft.PaintingStyle.STROKE,
                    color=ft.colors.BLACK,
                ),
            )
        )
    canvas.update()

def open_map(_):
    file_picker.pick_files(initial_directory=".", allow_multiple=False)

def save_map(_):
    file_saver.save_file()

def on_result(_):
    global map
    path = file_picker.result.files[0].path
    read_map(path)

def on_save(_):
    path = file_saver.result.path
    with open(path, "w", encoding="utf-8") as file:
        for i, (xmin, ymin, xmax, ymax, color) in enumerate(map):
            if color:
                file.write(f"P{i} {xmin} {ymin} {xmax} {ymax} {color} \n")
            else:
                file.write(f"P{i} {xmin} {ymin} {xmax} {ymax} \n")            

def round_10(x):
    return int(round(x/10)*10)

def main(page: ft.Page):
    global canvas, file_picker, file_saver
    page.title = "Flet Map Editor"

    def hover(e):
        global mouse_x, mouse_y
        mouse_x, mouse_y = e.local_x, e.local_y

    def tap(e):
        x, y = mouse_x - OFFSET_X, mouse_y - OFFSET_Y
        #print(x, y)
        for i, pays in enumerate(map):
            xmin, ymin, xmax, ymax, _ = pays
            # print(f"{i} -------------------")
            # print(xmin, x, xmax)
            # print(ymin, y, ymax)
            if xmin <= x <= xmax and ymin <= y <= ymax:
                if color:
                    map[i][-1] = color
                    draw_map()

    def pan_start(e: ft.DragStartEvent):
        global x, y
        x = round_10(e.local_x)
        y = round_10(e.local_y)
        canvas.shapes.append(
            cv.Rect(x, y, 0, 0, paint=ft.Paint(stroke_width=3))
        )

    def pan_update(e: ft.DragUpdateEvent):
        canvas.shapes[-1].width = round_10(e.local_x - x)
        canvas.shapes[-1].height = round_10(e.local_y - y)
        canvas.update()

    def pan_end(e: ft.DragEndEvent):
        shape = canvas.shapes[-1]
        shape.paint = ft.Paint(
            stroke_width=3,
            style=ft.PaintingStyle.STROKE,
            color=ft.colors.BLACK,
        )
        x, y, width, height = shape.x - OFFSET_X, shape.y - OFFSET_Y, shape.width, shape.height
        xmin, xmax = x, x + width  
        xmin, xmax = min(xmin, xmax), max(xmin, xmax)
        ymin, ymax = y, y + height
        ymin, ymax = min(ymin, ymax), max(ymin, ymax)
        map.append([xmin, ymin, xmax, ymax, None])
        
        canvas.update()

    canvas = cv.Canvas(
        [
            cv.Fill(
                ft.Paint(
                    gradient=ft.PaintLinearGradient(
                        (0, 0), (600, 600), colors=[ft.colors.WHITE, ft.colors.WHITE]
                    )
                )
            ),
        ],
        content=ft.GestureDetector(
            on_hover=hover,
            on_tap = tap,
            on_pan_start=pan_start,
            on_pan_update=pan_update,
            on_pan_end=pan_end,
            drag_interval=10,
        ),
        expand=False,
    )

    canvas.width = 600
    canvas.height = 600

    file_picker = ft.FilePicker(on_result=on_result)
    page.overlay.append(file_picker)
    file_saver = ft.FilePicker(on_result=on_save)
    page.overlay.append(file_saver)
    
    page.add(ft.Container(
            canvas,
            border_radius=5,
            width=float("inf"),
            expand=True,
        )

    )
    page.add(
        ft.Row([
        ft.ElevatedButton(
            "Open map ...", 
            on_click=open_map,
        ),
        ft.ElevatedButton(
            "Save map ...", 
            on_click=save_map,
        ),
        ft.IconButton(icon=ft.icons.FORMAT_COLOR_FILL, icon_color="red", on_click=set_red),
        ft.IconButton(icon=ft.icons.FORMAT_COLOR_FILL, icon_color="blue", on_click=set_blue),
        ft.IconButton(icon=ft.icons.FORMAT_COLOR_FILL, icon_color="yellow", on_click=set_yellow),
        ft.IconButton(icon=ft.icons.FORMAT_COLOR_FILL, icon_color="green", on_click=set_green),
        ft.IconButton(icon=ft.icons.CROP_SQUARE, icon_color="black", on_click=set_color_None)])
    )

ft.app(main)
