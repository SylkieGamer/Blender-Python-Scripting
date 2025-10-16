##Header
#The connect 4 game in python using blender

##Brief description
#I'm going to create the connect 4 game in blender using python to create a player controller
#a bot that will place a ball of a different color in a rand spot

##Actual code
import bpy, random
##I need to learn more about this
from mathutils import bvhtree

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

#I need to switch to the cycles render engine for the rigidbody
bpy.context.scene.render.engine = 'CYCLES'



##What is my code going to do then sudo code

#Create the connect 4 ball holder
bpy.ops.mesh.primitive_cube_add(size=2)
bpy.ops.transform.translate(value=(0, 0, 1))

bpy.ops.object.editmode_toggle()
bpy.ops.mesh.subdivide()
bpy.ops.mesh.delete(type='ONLY_FACE')
bpy.ops.object.editmode_toggle()

bpy.ops.object.convert(target='CURVE')
bpy.context.object.data.bevel_depth = 0.1
bpy.context.object.data.use_fill_caps = True
bpy.ops.object.shade_smooth()

box_copies = 4
box_copied = 1
list_o_boxes = []

while box_copied < box_copies:
    box_copied += 1
    bpy.context.object.scale[2] = 4
    bpy.context.object.location[2] = 4
    ob = bpy.context.active_object
    list_o_boxes.append(ob)
    if ob:
        if not ob.data.materials:
            mat = bpy.data.materials.new(name="ObjectColor1")
            ob.data.materials.append(mat)
        else:
            mat = ob.data.materials[0]
        
        mat.diffuse_color = (0.54, 0.17, 0.89 ,1.0)
        mat.metallic = .85
        
        ob.material_slots[0].link = 'OBJECT'
        
    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(2, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(True, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "use_duplicated_keyframes":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False, "translate_origin":False})

for scale in list_o_boxes:
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    bpy.ops.object.convert(target='MESH')

    
    
bpy.ops.object.light_add(type='AREA', radius=1, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
bpy.ops.transform.resize(value=(8, 1, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False)
#bpy.ops.transform.rotate[0] = (value=3.141)
bpy.ops.transform.rotate(value=3.14159, orient_axis='X')






#Create a menu pannel that has a slider of the y/x axis to pick a spot/button to add mesh

#Create a mesh ball that is a rigidbody that works with the holder, and material

#Connect the mesh ball to the slider and button

#Create a script that is player placed ball wait 3sec, place ball, rand x/y

###Detect similar ball next to it or detect the color? Maybe I could do a version of
### Godot group name, like assign it to this group, if group, add 1, if 2 collission
### and detect simmilar mat and value 2 you win.


##Thoughts
#For the holder
#I'll create a box with a certain ammount of subdivisions, delete faces, convernt lines
#to mesh or to curve? extrude the normals to create my grid? but then the colums have to 
#have walls... Create 1 box siez up on the x, turn it into a grid, create linked duplicates.
#and turn it into a static body?

#For the ball
#It'll be a simple sphere with a material assigned to red or blue and made into a rigid body.
#Wait am I going to have to create an animation keyframe to do a simple simulation?

#The player controller 
#Will be simple enough, slide on the y or x access a button to drop it.
#Maybe some settings the player controls for performance on the simulation

#Bot controller
#I'll be able to use the player controller and basically automate the placment of the ball
#with a random number in the x or y access

#Problem
#I have no idea ho I'm going to do collission detection or create a win senario
#Plus if I make a win senario I'll need a pop up to say if you or the bot won

#stretch goal
#Difficulty levels or a dynamic grid to place the balls in, or a Start game button in editor

##Notes
##I need to learn more about this chat GPT says it's really useful. mathutils is a fast
##module of math structures that for 3d operations, and BVHTree Bounding Volume Hierarchy
##is a data structure used to test if two meshes are overlapping or ray hits them.
#from mathutils import BVHTree

##creating a mesh light in blender is not performant, It's better to create an actual light.
##but depending on hardware(my potato laptop), flat shadding without light might be perferred
##There is a way to create baked lighing for evee but that would mean creating script to
##bake at runtime witch also could be a problem.
#bpy.ops.mesh.primitive_plane_add(size=10)
#plane_light = bpy.context.active_object
#mat = bpy.data.materials.new(name="ObjectPlane")
#plane_light.data.materials.append(mat)
#plane_light.material_slots[0].link = 'OBJECT'
#bpy.data.materials["ObjectPlane"].node_tree.nodes["Principled BSDF"].inputs[28].default_value = 1