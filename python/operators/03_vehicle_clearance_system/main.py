has_license = True
has_experience = False
has_clean_record = True

can_drive_car = (has_license) and (has_clean_record)
can_drive_truck = (has_license and has_experience) and (has_clean_record)
cannot_drive_any = not(has_license or has_clean_record )