bl_info ={
    "name": "Curve & Light Exporter",
    "author": "Sylvia",
    "version": (0,1),
    "blender": (4,5,3),
    "location": "Preferences right side pannel under tools",
    "category": "Import-Export",
}
#Modules we'll need
##todo: import only specific parts of modules
import bpy
from bpy.types import Operator as Op
from bpy.types import Panel as Pt
import json
import mathutils

#Keeping things semi organized until I split things into different spcripts

#  V Functions V
def export_curve_data(obj):
    #creating a list for curve data
    curve_data = []
    
    #access the curves blender file data
    curve = obj.data
    world = obj.matrix_world
    
    for spline in curve.splines:
        
        if spline.type == 'BEZIER':
            for point in spline.bezier_points:
                #position to world space
                pos = world @ point.co
                
                left = world @ point.handle_left
                right = world @ Point.handle_right
                
                curve_data.append({
                "position":list(pos),
                "tangent_left":list(left),
                "tangent_right":list(right),
                })
                
        elif spline.type == 'POLY':
            for point in spline.points:
                pos = world @ point.co.xyz
                curve_data.append({
                "position": list(pos),
                "tangent_left": None,
                "tangent_right": None,
                })
        return {
            "name": obj.name,
            "points": curve_data
            }

def export_light_data(light_obj):
    light = light_obj.name
    world = light_obj.matrix_world
    
    loc = world.translation
    rot = world.to_euler()
    
    return{
        "name":light_obj.name,
        "type":light.type,
        "position":list(loc),
        "rotation":list(rot),
        "color":list(light_color),
        "energy":light.energy,
        "spot_size":getattr(light, "spot_size", None),
        "area_size":getattr(light, "size", None)
            }


#I'm going to seperate the classes and functions for now
#I'll go back and consolidate the functions later

#  V CLASSES V

class EXPORT_OT_CurvesLights(Op):
    bl_idname = "exp.curves_lights_json"
    bl_label = "Export Curves and Lights"
    
    def execute(self, context):
        export_data = {
            "curves":[],
            "lights":[]
            }
        
        for obj in bpy.context.scene.objects:
            if obj.type =='CURVE':
                export_data["curves"].append(export_curve_data(obj))
            
            if obj.type == 'LIGHT':
                export_data["lights"].append(export_light_data(obj))
            
#            JSON
        filepath = bpy.path.abspath("//unreal_export.json")
        with open(filepath, "w") as f:
            json.dump(export_data, f, indent=4)
            
        return {finished}

class EXPORT_PT_Panel(Pt):
    bl_label = "Exporting Curves and Lights"
    bl_idname = "EXPORT_PT_Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Json File Export"
    
    def draw(self, context):
        layout = self.layout
        layout.operator("exp.curves_lights_json", text="Exporting Curves")
        


def register():
    bpy.utils.register_class(EXPORT_OT_CurvesLights)
    bpy.utils.register_class(EXPORT_PT_Panel)
    
def unregister():
    bpy.utils.unregister_class(EXPORT_OT_CurvesLights)
    bpy.utils.unregister_class(EXPORT_PT_Panel)

if __name__ == "__main__":
    register()