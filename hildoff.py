#!/usr/bin/python

# Based on C code from:
# "Hildon Tutorial" version 2009-04-28
# Example 2.1, "Example of stackable windows"

# https://wiki.maemo.org/PyMaemo/UI_tutorial/Windows_and_dialogs

# sudo apt install python-hildon

import gtk
import hildon

class TouchWidgets:
    def __init__(m):
        pass

    def big(m, s):
        return '<span size="x-large">%s</span>' % s

    def middle(m, s):
        return '<span size="medium">%s</span>' % s
    
    def small(m, s):
        return '<small>%s</small>' % s

    def font_label(m, s):
        w = gtk.Label(s)
        w.set_use_markup(True)
        return w
        
    def font_button(m, s):
        w = m.font_label(s)
        w1 = gtk.Button()
        w1.add(w)
        return w, w1

    def font_entry(m, size = 32, font=""):
        e = gtk.Entry()
        e.modify_font(pango.FontDescription("sans "+str(size)))
        return e

    def big_button(m, big, small):
        return m.font_button(m.big(big) + '\n' + m.small(small))

class TouchWindow(TouchWidgets):
    def __init__(m):
        m.main_window = 0
        m.window = None

    def close(m):
        m.window.destroy()
        if m.main_window:
            gtk.main_quit()

    def basic_main_window(m):
        m.basic_window()
        m.main_window = 1

    def gtk_main(m):
        gtk.main()

    def basic_window(m):
        window = hildon.StackableWindow()
        window.set_border_width(3)
        #window.maximize()
        m.window = window
        table = m.interior()

        window.add(table)
        window.show_all()
        m.window.connect("delete-event", lambda _, _1: m.close())

class SetupWindow(TouchWindow):
    def root_command(m, s):
        os.system("osso-xterm 'sudo %s'" % s)

    def action(m, title, action, descripton):
        box = gtk.HBox()
        _, button = m.font_button(title)
        button.connect("clicked", action)
        label = m.font_label(descripton)
        label.set_line_wrap(True)
        box.add(button)
        box.add(label)
        return box, button, label
        
    def interior(m):
        table = gtk.Table(10, 6, False)

        l, b = m.font_button(m.big("Close"))
        b.connect("clicked", lambda _: m.close())
        table.attach(b, 8, 10, 0, 1)

        img = gtk.Image()
        img.set_from_file("logo.png")
        img.set_size_request(120, 120)
        table.attach(img, 8, 10, 2, 3)

        welcome = ("""Welcome to the Maemo Leste; Maemo Leste continues the legacy of Maemo. We aim to provide a free Maemo experience on mobile phones and tablets like the Nokia N900, Motorola Droid 4, Allwinner Tablets and more.

More information is at https://maemo-leste.github.io/

""")
        details = ""

        l = m.font_label(m.big("Maemo Leste")+"\n"+
                         "Version 20190324\n\n"+welcome+details)
        #l.set_justify(GTK_JUSTIFY_CENTER)
        l.set_line_wrap(True)

        t = gtk.VBox()
        t.add(l)

        box, label, button = m.action(m.big("Grow\n")+"SD partition",
        	lambda _: m.root_command("/etc/expandcard.sh"),
                "Installation images use small fixed partition size. Press the button to grow partition to the available space."
        )
        t.add(box)

        box, label, button = m.action("Set\n"+m.big("root\n")+"password",
		lambda _: m.root_command("passwd"),
 	        "User account username is 'user'. When you connect USB cable, and you can connect to 192.168.2.XXX using ssh."
        )
        t.add(box)

        scrolled = gtk.ScrolledWindow()
        scrolled.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)
        scrolled.add_with_viewport(t)
        #scrolled.set_kinetic_scrolling(True)
        table.attach(scrolled, 0, 8, 0, 6)
        return table

 
def show_new_window(widget):

    test = SetupWindow()
    test.basic_main_window()
 
def main():
    program = hildon.Program.get_instance()
 
    # Create the main window
    win = hildon.StackableWindow()
    win.set_title("Welcome to Maemo Leste")

    
 
    button = gtk.Button("Go to subview")
    win.add(button)
 
    button.connect("clicked", show_new_window)
 
    win.connect("destroy", gtk.main_quit, None)
 
    # This call show the window and also add the window to the stack
    win.show_all()
    gtk.main()
 
if __name__ == "__main__":
    main()
    show_new_window(None)
    test.gtk_main()

