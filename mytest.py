import unreal
from unreal import Vector
from unreal import Vector
lst_actors = unreal.EditorLevelLibrary.get_all_level_actors()
print("place actor at 0 z")
for act in lst_actors:
	print(act)
	print(act.actor_guid)
	print(act.get_actor_location())
print("size=",len(lst_actors))
testactor=lst_actors[3]
#print("general",testactor.get_editor_property("General"))
testactor.set_actor_location(Vector(5,0.0,0.5),False,False)