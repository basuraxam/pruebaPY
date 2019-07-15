from gi.repository import Gtk
from gi.repository import Pango
import sys

list_of_dvd = [("The Usual Suspects", "111"),
               ("Gilda", "111"),
               ("The Godfather", "111"),
               ("Pulp Fiction", "111"),
               ("Once Upon a Time in the West", "111"),
               ("Rear Window", "111")]


class MyWindow(Gtk.ApplicationWindow):

    def __init__(self, app):
        Gtk.Window.__init__(self, title="My DVDs", application=app)
        self.set_default_size(250, 100)
        self.set_border_width(10)

        # the data are stored in the model
        # create a liststore with one column
        self.listmodel = Gtk.ListStore(str,str)
        for lista in list_of_dvd:
            self.listmodel.append(list(lista))

        # a treeview to see the data stored in the model
        view = Gtk.TreeView(model=self.listmodel)

        # cellrenderer for the first column
        cell = Gtk.CellRendererText()
        cell2= Gtk.CellRendererText()
  
        col = Gtk.TreeViewColumn("Title", cell, text=0)
        view.append_column(col)

        col2 = Gtk.TreeViewColumn("Descrip", cell2, text=1)
        view.append_column(col2)


        # a grid to attach the widgets
        grid = Gtk.Grid()
        grid.attach(view, 0, 0, 4, 1)

        # add the grid to the window
        self.add(grid)


class MyApplication(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
