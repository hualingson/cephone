from src import gui

GOLDEN_SECTION_RATIO = 0.618

class MainFrame(gui.Frame):
    def __init__(self):
        gui.Frame.__init__(self, None, title="CephOne", style=gui.DEFAULT_FRAME_STYLE)
        w, h = gui.DisplaySize()
        self.SetSizeWH(w*GOLDEN_SECTION_RATIO, h*GOLDEN_SECTION_RATIO)
        self.SetIcon(gui.Icon('../../picture/co_64px.ico', gui.BITMAP_TYPE_ICO))
        gui.Panel(self)
        mb = gui.MenuBar()
        gui.Menu()
        gui.MenuItem()
        self.SetMenuBar(mb)

class App(gui.App):
    
    def OnInit(self):
        self.mf = MainFrame()
        self.mf.CenterOnScreen()
        self.mf.Show()
        return True

if __name__ == '__main__':
    from src import platform
    print platform.getcwd()
    cephonew = App()
    cephonew.MainLoop()
