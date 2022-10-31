# farm_animals = {'cow', 'sheep', 'hen', 'goat', 'horse'}
# wild_animals = {'lion', 'elephant', 'tiger', 'goat', 'panther', 'horse'}
# # print(farm_animals)
#
# # for animal in farm_animals:
# #     print(animal)
#
# all_animals_1 = farm_animals | wild_animals
# print(all_animals_1)
#

from presc_data import adverse_interactions

meds_to_watch = set()

# for interaction in adverse_interactions:
    # meds_to_watch = meds_to_watch | interaction
    # meds_to_watch.update(interaction)
    # meds_to_watch |= interaction
meds_to_watch.update(*adverse_interactions)

# print(sorted(meds_to_watch))
print(*sorted(meds_to_watch),sep='\n')