##Header
#Testing different actions in blender

##description
#my playground for blender operations to understand how they work
import bpy

#The consol toggle has to be called to open the blender windows console
#but it also has to be called to close it as well. Hitting the x will close blender.
#bpy.ops.wm.console_toggle()

#will print the full list of the undo history to the console or...
##it should but it's only returning the class 'CANCELED' call
#okay for some reason it works now the undo_history only returns the 'cancelled'though

#history =[bpy.ops.ed.undo_history()]
#print(history)

##I just read, apparently there's an issue with the python api that doesn't actually allow
##access to the list so this operation actually calls to the C backend to get it
#also interesting I can use Windows Manager to add a timer event
#this works
#bpy.context.window_manager.print_undo_steps()

#this does not work
#for his in bpy.ops.ed.undo_history():
#    print(his)

print(bpy.types.WindowManager.operators)