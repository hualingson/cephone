from src import gui

MENU_MODE = "&Mode"
MENU_ITEM_MODE_SERVER = 0x1001
MENU_TOOL = "&Tool"
MENU_ITEM_TOOL_CONFIG = 0x2001
MENU_ITEM_TOOL_CRUSH = 0x2002
MENU_HELP = "&Help"
MENU_ITEM_HELP_ABOUT = 0x3001
MENU_ITEM_HELP_LICENSE = 0x3002

GOLDEN_SECTION_RATIO = 0.618

class MainFrame(gui.Frame):
    def __init__(self):
        gui.Frame.__init__(self, None, title="CephOne", style=gui.DEFAULT_FRAME_STYLE)
        
        w, h = gui.DisplaySize()
        self.SetSizeWH(w*GOLDEN_SECTION_RATIO, h*GOLDEN_SECTION_RATIO)
        self.SetIcon(gui.Icon('../../picture/co_64px.ico', gui.BITMAP_TYPE_ICO))
        
        mb = gui.MenuBar()
        
        m = gui.Menu()
        mi = gui.MenuItem(m, MENU_ITEM_MODE_SERVER, "&Server", "enable web client")
        m.AppendItem(mi)
        mb.Append(m, MENU_MODE)
        
        m = gui.Menu()
        mi = gui.MenuItem(m, MENU_ITEM_TOOL_CONFIG, "c&Onfig", "customize option")
        m.AppendItem(mi)
        mi = gui.MenuItem(m, MENU_ITEM_TOOL_CRUSH, "c&Rush", "visual assignment")
        m.AppendItem(mi)
        mb.Append(m, MENU_TOOL)
        
        m = gui.Menu()
        mi = gui.MenuItem(m, MENU_ITEM_HELP_ABOUT, "&About", "what is this")
        m.AppendItem(mi)
        mi = gui.MenuItem(m, MENU_ITEM_HELP_LICENSE, "&License", "copyright declaration")
        m.AppendItem(mi)
        mb.Append(m, MENU_HELP)
        
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
