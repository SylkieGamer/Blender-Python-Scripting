import bpy

class OBJECT_OT_add_sphere(bpy.types.Operator):
    """Add a sphere to the scene"""
    bl_idname = "object.add_sphere"
    bl_label = "Add Sphere"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0, 0, 0))
        return {'FINISHED'}

class VIEW3D_PT_sphere_panel(bpy.types.Panel):
    """Creates a Panel in the 3D View toolbar"""
    bl_label = "Sphere Tools"
    bl_idname = "VIEW3D_PT_sphere_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Add"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("object.add_sphere", text="Add Sphere")

def register():
    bpy.utils.register_class(OBJECT_OT_add_sphere)
    bpy.utils.register_class(VIEW3D_PT_sphere_panel)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_add_sphere)
    bpy.utils.unregister_class(VIEW3D_PT_sphere_panel)

if __name__ == "__main__":
    register()