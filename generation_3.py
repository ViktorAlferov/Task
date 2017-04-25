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
                description = process_line(line)
                descriptions[(description.id)] = description
    return descriptions

def process_line(line):
    fields = line.split(":")
    description = Description(fields[GENDER], fields[PRODUCT], fields[CLASP_TYPE],
                              fields[POCKET_TYPE], fields[SEAM_LENGHT], fields[CUTTING],
                              fields[DESIGN_EFFECTS], fields[SEASON], fields[ID])
    return description

def save_discriptions(descriptions):
    for key in sorted(descriptions):
        descript = descriptions[key]
        with open('data/descriptions_out.txt', 'a') as file:

            print("{0:.5}ие {1} на {2:.7}ах декорированные {3:.6}ми карманами."
                  "Длинные брючины {4}. Крой типа {5} позволяет подчеркнуть вашу фигуру,"
                  "а эффект {6} создает небрежный образ."
                  "Подходит на {7} сезон.:{8}".format(descript.gender, descript.product, descript.clas_type,
                                                      descript.pocket_type, descript.seam_lenght, descript.cutting,
                                                      descript.design_effects, descript.season, descript.id), file=file)


main()

#todo без сортировки итерироваться
#todo с сортировкой
# format вместе с print
# create_description на две функции
