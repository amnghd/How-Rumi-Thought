input = "hydrochloric"

def acidNaming(acid_name):
    if (acid_name[0:5] == "hydro") & (acid_name[-2:]=='ic'):
        print('non-metal acid')
    elif (acid_name[0:5] != "hydro") & (acid_name[-2:]=='ic'):
        print('polyatomic acid')
    else:
        print("not an acid")

acidNaming(input)