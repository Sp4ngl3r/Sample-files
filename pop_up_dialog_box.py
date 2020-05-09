import bpy

class Window_Manager_of_My_Operetion(bpy.types.Operator):
    
    """Opens a dialogue box"""
    
    bl_label = "Add Cube Dialogue Box"
    bl_idname = "wm.op"
    
    location = bpy.props.FloatVectorProperty(name = "Location " , default = (0,0,0))
    number_of_walls = bpy.props.IntProperty(name = "Number of Walls : ")
    
    wall_0_w = bpy.props.IntProperty(name = "Value for w of Wall 1 : ")
    wall_0_r = bpy.props.IntProperty(name = "Value for r of Wall 1 : ")
    wall_1_w = bpy.props.IntProperty(name = "Value for w of Wall 2 : ")
    wall_1_r = bpy.props.IntProperty(name = "Value for r of Wall 2 : ")
    wall_2_w = bpy.props.IntProperty(name = "Value for w of Wall 3 : ")
    wall_2_r = bpy.props.IntProperty(name = "Value for r of Wall 3 : ")
    wall_3_w = bpy.props.IntProperty(name = "Value for w of Wall 4 : ")
    wall_3_r = bpy.props.IntProperty(name = "Value for r of Wall 4 : ")       
        
        
    def execute(self, context):
        
        j = 0 
        l = self.location
        n = self.number_of_walls
        
        array_of_values_for_walls = []
        array_of_values_for_walls.append(self.wall_0_w)
        array_of_values_for_walls.append(self.wall_0_r)
        array_of_values_for_walls.append(self.wall_1_w)
        array_of_values_for_walls.append(self.wall_1_r)
        array_of_values_for_walls.append(self.wall_2_w)
        array_of_values_for_walls.append(self.wall_2_r)
        array_of_values_for_walls.append(self.wall_3_w)
        array_of_values_for_walls.append(self.wall_3_r)
        
        bpy.context.scene.cursor.location = (l[0],l[1],l[2])
        bpy.ops.mesh.archimesh_room()
        bpy.context.object.RoomGenerator[0].wall_num = n
        for i in range(n) :    
            
            if(array_of_values_for_walls[j] != "0"):
                bpy.context.object.RoomGenerator[0].walls[i].w = int(array_of_values_for_walls[j])
            
            j += 1
                
            if(array_of_values_for_walls[j] != "0"):
                bpy.context.object.RoomGenerator[0].walls[i].r = int(array_of_values_for_walls[j])
                
            j += 1
        
               
        return {'FINISHED'}
   
    def invoke(self, context, event):
       
        return context.window_manager.invoke_props_dialog(self)
    
    
    
def register():
    bpy.utils.register_class(Window_Manager_of_My_Operetion)
    
def unregister():
    bpy.utils.unregister_class(Window_Manager_of_My_Operetion)
    
if __name__ == "__main__":
    register()
    
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False, confirm=False)
    
    
    bpy.ops.wm.op('INVOKE_DEFAULT') 