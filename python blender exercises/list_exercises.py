###Header
#List comprehaension exercises

###Description
#I'm having trouble comprehending different lists, list comprehensions, one liners,( and classes).

###Code

import bpy

scene_obs = bpy.ops.object

scene_obs.select_all(action='SELECT')
scene_obs.delete(use_global=False)

bpy.ops.mesh.primitive_cube_add()
cube = bpy.context.active_object

num_colum = 4
colums = []
object = bpy.ops.mesh.primitive_cube_add(scale = (1,1,1))
new_ob = bpy.context.active_object
#new_ob.location = (1,1,1)
dupli_move = bpy.ops.object.duplicate_move(
        OBJECT_OT_duplicate={"linked":False,
        "mode":'TRANSLATION'},
        TRANSFORM_OT_translate={"value":(0, 0, 2)}
        )

for i in range(num_colum):
    bpy.ops.object.duplicate_move(
        OBJECT_OT_duplicate={"linked":False,
        "mode":'TRANSLATION'},
        TRANSFORM_OT_translate={"value":(0, 0, 2)}
        )
#object2 = bpy.ops.mesh.primitive_cube_add(location=(3,0,0), scale = (1,1,1))
#new_ob2 = bpy.context.active_object
#colum2 = [bpy.ops.object.duplicate_move(
#        OBJECT_OT_duplicate={"linked":False,
#        "mode":'TRANSLATION'},
#        TRANSFORM_OT_translate={"value":(0, 0, 2)}
#        ) for i in num_colum]

Colum3 = [for i in num_colum]
print(len(Colum3))

#    z = i*2
#    new_ob.location(0,0,z)
#    bpy.ops.mesh.primitive_cube_add(scale=(1, 1, 1), location=(0,0,z))
#    bpy.ops.object.transform_apply(location=True)

    


###Thoughts
#I think python one liners are kind of cool as a concept
#I would love to take sometime to just memorise a few of them, along my road map I
#would like to learn python comprehensions, match/case, and try/except

###Learning Notes