# INPUT: bitta qatorda matn
# VAZIFA: faqat raqam belgilarini ajrating (0-9)
# OUTPUT: raqamlar ketma-ketligi
# Agar raqam bo‘lmasa: BO'SH
matn = input()
raqamlar = "".join([belgi for belgi in matn if belgi.isdigit()])
if raqamlar:
    print(raqamlar)
else:
    print("BO'SH")