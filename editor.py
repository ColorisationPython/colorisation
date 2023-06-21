import flet as ft
import flet.canvas as cv

OFFSET_X, OFFSET_Y = 100, 100

x,y = None, None
map = []
canvas = None

def read_map(path):
    global map
    if map is None:
        map = []
    map[:] = []
    with open(path, "r", encoding="utf-8") as f:
        lines = [l for l in f.read().splitlines() if l.strip()]
        for line in lines:
            name, xmin, ymin, xmax, ymax = line.split()
            map.append([int(xmin), int(ymin), int(xmax), int(ymax)])
    draw_map()

def draw_map():
    global canvas
    canvas.shapes[:] = []
    for xmin, ymin, xmax, ymax in map:
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
        for i, (xmin, ymin, xmax, ymax) in enumerate(map):
            file.write(f"P{i} {xmin} {ymin} {xmax} {ymax} \n")            

def round_10(x):
    return int(round(x/10)*10)

def main(page: ft.Page):
    global canvas, file_picker, file_saver
    page.title = "Flet Map Editor"

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
        map.append([xmin, ymin, xmax, ymax])
        
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
        )
        ])
    )

ft.app(main)
