import bpy

context = bpy.context
scene = context.scene
seq = scene.sequence_editor

def delete_object(name):
    # try to find the object by name
    if name in bpy.data.objects:
        # if it exists, select it and delete it
        obj = bpy.data.objects[name]
        obj.select_set(True)
        bpy.ops.object.delete(use_global=False)
        
# xoa        
delete_object('cam1')
delete_object('cam2')

cam1 = bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', 
                        location=(27.8435, -31.8384 ,14.728 ), 
                        rotation=(1.11352, 0.0387463, 1.17461), scale=(1, 1, 1))
cam1 = bpy.context.active_object
cam1.name = 'cam1'
start_frame1 = 0
start1 = cam1.keyframe_insert("location", frame = start_frame1)

marker = scene.timeline_markers.new('cam1', frame=start_frame1)
marker.camera = scene.objects.get('cam1')

last_frame1 = 40
cam1.location.y = 68.162
last1 = cam1.keyframe_insert("location", frame = last_frame1)

bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', 
                        location=(-1.1446, -29.067 ,0.75578 ), 
                        rotation=(1.483879, 0.013964, -0.193047), scale=(1, 1, 1))
cam2 = bpy.context.active_object
cam2.name = 'cam2'       
start_frame2 = 50
start2 = cam2.keyframe_insert("location", frame = start_frame2)

marker = scene.timeline_markers.new('cam2', frame=start_frame2)
marker.camera = scene.objects.get('cam2')

mid_frame2 = 100
cam2.location.y = 55.694
last2 = cam2.keyframe_insert("location", frame = mid_frame2)                 

last_frame2 = 150
cam2.location.y = -29.067
last2 = cam2.keyframe_insert("location", frame = last_frame2)  

for sound in seq.sequences:
   seq.sequences.remove(sound)
   
if not scene.sequence_editor:
    scene.sequence_editor_create()

#Sequences.new_sound(name, filepath, channel, frame_start)    
path = "F:/Downloads/blender/blender scence/music/dianguc.mp3"
soundstrip = scene.sequence_editor.sequences.new_sound("dianguc", path, 1, -10)

path = "F:/Downloads/blender/blender scence/music/cuoi.mp3"
soundstrip = scene.sequence_editor.sequences.new_sound("cuoi", path, 3, -10)

path = "F:/Downloads/blender/blender scence/music/kinhdi.mp3"
soundstrip = scene.sequence_editor.sequences.new_sound("kinhdi", path, 2, -10)

