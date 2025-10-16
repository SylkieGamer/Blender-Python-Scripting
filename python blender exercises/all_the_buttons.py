#__Title__
#Buttons Everywhere

#__Head__
#A blender addon to create all the different buttons even if they do nothing.

#__Code__
import bpy, math, random

#favorite code select all delete
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

#Let's make a button
#Operator class creates actions to be performed
class SIMPLE_OT_ButtonOperator(bpy.types.Operator):
    bl_idname = "wm.simple_button"
    bl_label = "Click Me!"
    
    def execute(self, context):
        return{'FINISHED'}

##GPT wants me to put a properties class in here
class SimpleUIProperties(bpy.types.PropertyGroup):
    toggle_option:
        bpy.types.BoolProperty(
        name=""
        description=""
        default=False
        )
        
    check_option:
        bpy.types.BoolProperty(
        name=""
        description=""
        default=False
        )
        
    enum_option:
        bpy.types.EnumProperty(
        name=""
        description=""
        List=[
        ()
        ()
        ()
        ]
        default='OPT_A'
        )

#Panel class creates the button to be created
class VIEW3D_PT_Firstbutton(bpy.types.Panel):
    bl_label = "Custom Panel Buncha Buttons"
    bl_idname = "VIEW3D_PT_Firstbutton"
    bl_space_type ='VIEW_3D'
    bl_region_type = 'UI'
    bl_category ="Demo Buttons"
    
    #I don't need __init__ because this is a class type of blender
    def draw(self, context):
        #I forget
        layout = self.layout
        props = context.scene.simple_ui_props
        
        #operator button
        layout.label(text="Basic Buttons:")
        layout.operator("wm.simple_button", text="Operator Button")
    


#addon code. It worked without me looking up anything!!

def register():
    bpy.utils.register_class(VIEW3D_PT_Firstbutton)
    bpy.utils.register_class(SIMPLE_OT_ButtonOperator)
    bpy.utils.register_class(SimpleUIProperties)

def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_Firstbutton)
    bpy.utils.unregister_class(SIMPLE_OT_ButtonOperator)
    bpy.utils.unregister_class(SimpleUIProperties)

if __name__ == "__main__":
    register()