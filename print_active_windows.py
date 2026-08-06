import win32gui

def enum_handler(hwnd, results):
    if win32gui.IsWindowVisible(hwnd):
        title = win32gui.GetWindowText(hwnd)
        cls = win32gui.GetClassName(hwnd)
        if title or cls:
            results.append((hwnd, title, cls))

windows = []
win32gui.EnumWindows(enum_handler, windows)
for hwnd, title, cls in windows:
    print(hwnd, f"[{title}]", cls)