#dictionary with addon details
bl_info = {
    "name": "my Custom Panel",
    "author": "Syl",
    "version": (0,0,1),
    "blender": (4,5,3),
    "location": "3D Viewport > Sidebar > My Custom Panel category",
    "description": "My custom operator buttons",
    "category": "Development",
}

#access python
import bpy

class VIEW3D_PT_my_custom_panel(bpy.types.Panel): #naming convention 'CATEGORY_PT_name' PT:PanelType
    pass

    #where to add the panel #panels and types on blender Python API docs
    bl_space_type = "VIEW_3D" #3D viewprt area
    bl_region_type = "UI" #Sidebar region

    #add labels
    bl_category = "My Custom Panel Category" #found in sidebar
    bl_label = "My Custom Panel label" #found at top of the panel
    
    #
    def draw(self, context):
        """define the layout of the panel"""
        row = self.layout.row()
        row.operator("object.select_all", text="Select All")
        row = self.layout.row()
        row.operator("mesh.primitive_cube_add", text="Add Cube")
        row = self.layout.row()
        row.operator("object.shade_smooth", text="Shade Smooth")


#register the panel in blender
def register():
    bpy.utils.register_class(VIEW3D_PT_my_custom_panel)

def unregister():
    bpy.utils.unregister_class(VIEW3D_PT_my_custom_panel)

if __name__ == "__main__":
    register()

##Notes
#Were creating a python script to create a button in the blender panel, and bundeling it into an addon! I'm kind of excite! I didn't think we would turn it into an addon.
#Probably a little advanced for me but I love the challenge, and this will be so seful for me!