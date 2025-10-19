###Header
#Testing blender scripting

###Description
#I'm creating a script inspired by CG Pythons helper script, it will help with debugging,
#cleaning extraneus data, and general good to have scripts.

###Breakdown
#This script comes from a lot of places, I modified CG Pythons helper script to work
#within a class, I also started looking for other things they may be helpful if working
#in bpy, I was able to find through documentation and forums a starting point for getting
#the os and other details, after the scripts were working chat gpt was able to suggest
#the class structure for it and to add @staticmethod and @classmethod.

###Code
import bpy
from bpy.types import Operator, Panel
import random, math
import sys, platform


#CGPython helper functions I bundled into a class
class CGPythonHelper():
    #OT classes need a bl_idname with a period. It's category.name
    #this method is supper helpful it checks version and then wipes old data in system
    @staticmethod
    def purge_orphans():
        if bpy.app.version >= (3,0,0):
            bpy.ops.outliner.orphans_purge(
                do_local_ids=True, do_linked_ids=True, do_recursive=True
                )
        else:
            result = bpy.ops.outliner.orphans_purge()
            if result.pop() != "CANCELED":
                purge_orphans()
                
    @staticmethod
    def clean_whole_scene():
        bpy.ops.ed.undo_push(message="Restore point 1")
        #makes sure we aren't in edit mode
        if bpy.context.active_object and bpy.context.active_object.mode == 'EDIT':
            bpy.ops.object.editmode_toggle()
            
        #favorite code select all/delete
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=False)
        
        #makes sure nothing is hidden
        for obj in bpy.data.objects:
            obj.hide_set(False)
            obj.hide_select = False
            obj.hide_viewport = False
        
        #creates a list of any colllections you have and deletes them
        collection_names = [col.name for col in bpy.data.collections]
        for name in collection_names:
            bpy.data.collections.remove(bpy.data.collections[name])

        #creates a list of any world shaders you've made and removes them before creating new.
        world_names = [world.name for world in bpy.data.worlds]
        for name in world_names:
            bpy.data.worlds.remove(bpy.data.worlds[name])
        #creates new world block
        bpy.ops.world.new()
        bpy.context.scene.world = bpy.data.worlds["World"]
    @staticmethod
    def reset_it_all():
        CGPythonHelper.clean_whole_scene()
        CGPythonHelper.purge_orphans()
        return {'FINISHED'}
        


#Class that gathers and prints information about your system
#created from a mix of documentation, forums, and advice.
class OSInfoHelper:
    @staticmethod
#    using sys and platform import we can get information from the computer
    def get_os_info():
        platform_id = sys.platform
        os_version = platform.version()
        os_release = platform.release()
        full_platform = platform.platform()

        if platform_id.startswith("win"):
            os_name = "Windows"
        elif platform_id.startswith("linux"):
            os_name = "Linus"
        elif platform_id == "darwin":
            os_name = "Mac"
        else:
            os_name = f"unknow os {platform_id}"    
        return {
    "full platform": full_platform,
    "name": os_name,
    "release": os_release,
    "version": os_version,
    "platform_id": platform_id
    }
    
    #actual print statments, I don't have to call self, context because of @staticmethod
    @staticmethod
    def print_os_info():
        info = OSInfoHelper.get_os_info()
        print(f"OS Name: {info['name']}")
        print(f"OS Type: {info['platform_id']}")
        print(f"OS Version: {info['release']}")
        print(f"OS Version All: {info['version']}")
        print(f"IDK but it scares me: {info['full platform']}")
        print("Windows-10-10.0.22631 is a legacy convention meaning windows 11")
        print("If Windows version is followed by SP0 it may need a security update")

#I'm going to try a new system, actions are handled by a custom class with static methods
#the actions class is basically a list of functions to call
#the actions class is then called by the operator class to execute the actions
#the Operator class that is performing the action is called by the panel class
#and all the blender format classes are called in register. with the static method I can
#also probably clean up my script by extracting the actions list class to another script.
#Class Actions holds defs, operator executes the actions, panel draws the execution point.

class DEBUG_OT_CGPython(Operator):
    bl_idname = "ot.clean_scene"
    bl_label = "Clean all data in scene"
    bl_description = "This cleans the world shaders, scene objects, and orphaned data."
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        CGPythonHelper.reset_it_all()
        return {'FINISHED'}
        

###This is copied edited from one of blenders templates
class OSINFO_OT_ShowSysteminfo(Operator):
    #OT classes need a bl_idname with a period. It's category.name
    bl_idname = "wm.show_os_info"
    bl_label = "Show My OS"
    bl_description = "Print's to the console your operating system"
    bl_options = {'REGISTER', 'UNDO'}

#    scale: FloatVectorProperty(
#        name="scale",
#        default=(1.0, 1.0, 1.0),
#        subtype='TRANSLATION',
#        description="scaling",
#    )

    def execute(self, context):
        OSInfoHelper.print_os_info()
        return {'FINISHED'}
    
class OSINFO_PT_Panel(Panel):
    bl_label = "Debugging"
    bl_idname = "OSINFO_PT_Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    #this will place in the tool menu panel that already exists... if I can stop misspelling it
    bl_category = 'Bug Tools'
    
    def draw(self, context):
        layout= self.layout
        layout.operator(OSINFO_OT_ShowSysteminfo.bl_idname, text="Print OS Info To Console")
#        layout.operator(CGPythonHelper.purge_orphans(), text ="Purge Unused data")
        
        #creates variables to house context, and predefined splits in the panel
        scene = context.scene
        split = layout.split(factor=0.2)
        col = split.column()
        
        layout.operator(DEBUG_OT_CGPython.bl_idname, text ="Purge Unused data")
        
#        scene = context.scene
#        split = layout.split(factor=0.2)
#        col = split.column()
#        
#        #Just creates a label with that text
#        col.label(text='Slider')
#        
#        #we are basically assigning a new split colum to the col attribute
#        col = split.column()
#        
#        #uses predefined blender UI to create a slider
#        col.prop(scene, "frame_start", text='hello')

##weird popup menu I guess lets try
class POPUP_OT_SystemInfoPopoup(Operator):
    bl_idname = "popup.systeminfopopup"
    bl_label = "System Info Popup"
    bl_description = "Demonstrates draw, invoke, and execute in one operator script"
    
    #properties in popup
    my_text: bpy.props.StringProperty(name="Name", default="Cube")
    my_value: bpy.props.FloatProperty(name="Scale", default=1.0, min=0.1)
    
    #defines the popup UI layout
    def draw(self, context):
        layout = self.layout
        layout.label(text="Enter your settings")
        layout.prop(self, "my_text")
        layout.prop(self, "my_value")
    #invoke method decides how the operator starts
    def invoke(self, context, event):
        #show dialouge popup with draw call
        return context.window_manager.invoke_props_dialog(self, width=250)
    #execute method runs after user clicks okay
    def execute(self, context):
        ob = bpy.data.objects.get(self.my_text)
        if ob:
            ob.scale *= self.my_value
        return {'FINISHED'}

class POPUP_PT_Popupmanager(Panel):
    bl_label="Popup Panel"
    bl_idname="POPUP_PT_Popupmanager"
    bl_space_type='VIEW_3D'
    bl_region_type='UI'
    bl_category='My Addon'
    def draw(self, context):
        layout =self.layout
        layout.operator("popup.systeminfopopup", text="Popup")
    
    
def register():
    bpy.utils.register_class(OSINFO_OT_ShowSysteminfo)
    bpy.utils.register_class(OSINFO_PT_Panel)
    bpy.utils.register_class(DEBUG_OT_CGPython)
    bpy.utils.register_class(POPUP_OT_SystemInfoPopoup)
    bpy.utils.register_class(POPUP_PT_Popupmanager)


def unregister():
    bpy.utils.unregister_class(OSINFO_OT_ShowSysteminfo)
    bpy.utils.unregister_class(OSINFO_PT_Panel)
    bpy.utils.unregister_class(DEBUG_OT_CGPython)
    bpy.utils.unregister_class(POPUP_OT_SystemInfoPopoup)
    bpy.utils.unregister_class(POPUP_PT_Popupmanager)


if __name__ == "__main__":
    register()

###Notes
#