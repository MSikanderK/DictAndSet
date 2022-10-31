from presc_data import *

trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]

# remove warfarin and add edoxaban
for patient in trial_patients:
    prescription = patients[patient]
    try:
        prescription.remove(warfarin)
        prescription.add(edoxaban)
    except KeyError:
        print(f"Patient {patient} is not taking Warfarin. "
              f"Please remove {patient} from trial.")
    print(patient, prescription)
