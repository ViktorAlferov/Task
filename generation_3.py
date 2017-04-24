# coding: utf-8
import collections
import sys

ID, GENDER, PRODUCT, CLASP_TYPE, POCKET_TYPE, SEAM_LENGHT, CUTTING, DESIGN_EFFECTS, SEASON = range(9)

Description = collections.namedtuple("Description",
            ['gender', 'product', 'clas_type', 'pocket_type', 'seam_lenght', 'cutting', 'design_effects', 'season', 'id'])


def main():

    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print("usage: {0} file1 [file2 [... fileN]]".format(sys.argv[0])) 
        sys.exit()
    filenames = sys.argv[1:]
    descriptions = create_discriptions(filenames)
    save_discriptions(descriptions)
    print(descriptions)
    

def create_discriptions(filenames):
    descriptions = {}
    for filename in filenames:
        for line in open(filename, encoding="utf8"):
            line = line.rstrip()
            if line:
            	fields = line.split(":")
            	description = Description(fields[GENDER], fields[PRODUCT], [CLASP_TYPE], fields[POCKET_TYPE], 
            		fields[SEAM_LENGHT], fields[CUTTING], fields[DESIGN_EFFECTS], fields[SEASON], fields[ID])

            descriptions[(description.id)] = description
    return descriptions
    

def save_discriptions(descriptions):


    for key in sorted(descriptions):
        descript = descriptions[key]

        with open('data/descriptions_out.txt', 'a') as file:
        	print(descript.gender[:5] + "ие", descript.product, "на", descript[CLASP_TYPE][:7] + "ах", "декорированные", 
        	      descript.pocket_type[:6] + "ми", "карманами. Длинные брючины", descript.seam_lenght, 
    	          "Крой типа", descript.cutting, "позволяет подчеркнуть вашу фигуру, а эффект", 
    	          descript.design_effects, "создает небрежный образ. Подходит на", descript.season, "сезон.", file=file)

        


main()

#todo без сортировки итерироваться
#todo с сортировкой
# format вместо print
# 24 на with
# create_description на две функции