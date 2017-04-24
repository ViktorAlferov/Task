# coding: utf-8
import collections
import sys

ID, GENDER, PRODUCT, CLASP_TYPE, POCKET_TYPE, SEAM_LENGHT, CUTTING, DESIGN_EFFECTS, SEASON = range(9)

Description = collections.namedtuple("Description",
            "descriptionname gender product clasp_type pocket_type seam_lenght cutting design_effects season id")


def main():

    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print("usage: {0} file1 [file2 [... fileN]]".format(sys.argv[0])) 
        sys.exit()

    descriptionnames = set() 
    descriptions = {}        
    for filename in sys.argv[1:]:
        for line in open(filename, encoding="utf8"):
            line = line.rstrip()
            if line:
                description = process_line(line, descriptionnames)
                descriptions[(description.gender.lower(), description.product.lower(), description.id)] = description
    print_description(descriptions)

def process_line(line, descriptionnames):
    fields = line.split(":")
    
    description = Description(fields[GENDER], fields[PRODUCT], [CLASP_TYPE], fields[POCKET_TYPE], 
        fields[SEAM_LENGHT], fields[CUTTING], fields[DESIGN_EFFECTS], fields[SEASON], fields[ID])
    
    return description
    



def print_description(descriptions):


    for key in sorted(descriptions):
        description = descriptions[key]
        print("{0}".format(description.gender)[:5] + "ие", "на", CLASP_TYPE, "декорированные", POCKET_TYPE, 
              "карманами. Длинные брючины", SEAM_LENGHT, 
              "Крой типа", CUTTING, "позволяет подчеркнуть вашу фигуру, а эффект", DESIGN_EFFECTS, 
              "создает небрежный образ. Подходит на", SEASON, "сезон.")



main()

'''
if description.product:
            initial = " " + description.product[0]
        name = "{0.gender}, {0.product}{1}".format(description, initial)
        print("{0:.<{nw}} ({1.id:4}) {1.product:{uw}}".format(
              name, description, nw=namewidth, uw=usernamewidth))

'''