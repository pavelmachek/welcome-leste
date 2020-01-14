#!/usr/bin/python

# Based on C code from:
# "Hildon Tutorial" version 2009-04-28
# Example 2.1, "Example of stackable windows"

# 

import gtk
import hildon
 
def show_new_window(widget):
    # Create the main window
    win = hildon.StackableWindow()
    win.set_title("Subview")
 
    # Setting a label in the new window
    label = gtk.Label("This is a subview")
 
    vbox = gtk.VBox(False, 0)
    vbox.pack_start(label, True, True, 0)
 
    win.add(vbox)
 
    # This call show the window and also add the window to the stack
    win.show_all()
 
def main():
    program = hildon.Program.get_instance()
 
    # Create the main window
    win = hildon.StackableWindow()
    win.set_title("Main window")
 
    button = gtk.Button("Go to subview")
    win.add(button)
 
    button.connect("clicked", show_new_window)
 
    win.connect("destroy", gtk.main_quit, None)
 
    # This call show the window and also add the window to the stack
    win.show_all()
    gtk.main()
 
if __name__ == "__main__":
    main()

