# Ham tinh do dai cac canh:
if kiem_tra_tam_giac(AB, CA) is True:
    def goc_canh_tamgiac(AB, BC, CA):
        import math
        a = list()
        canhAB = round(math.sqrt(AB[0] * AB[0] + AB[1] * AB[1]), 2)
        canhBC = round(math.sqrt(BC[0] * BC[0] + BC[1] * BC[1]), 2)
        canhCA = round(math.sqrt(CA[0] * CA[0] + CA[1] * CA[1]), 2)
        a.append(canhAB)
        a.append(canhBC)
        a.append(canhCA)

        cosA = (AB[0] * (-1) * CA[0] + AB[1] * (-1) * CA[1]) / (
                    math.sqrt(pow(AB[0], 2) + pow(AB[1], 2)) * math.sqrt(pow(CA[0], 2) + pow(CA[1], 2)))
        gocA = round(math.degrees(math.acos(cosA)), 2)
        a.append(gocA)

        cosB = (BC[0] * (-1) * AB[0] + BC[1] * (-1) * AB[1]) / (
                    math.sqrt(pow(BC[0], 2) + pow(BC[1], 2)) * math.sqrt(pow(AB[0], 2) + pow(AB[1], 2)))
        gocB = round(math.degrees(math.acos(cosB)), 2)
        a.append(gocB)

        cosC = (CA[0] * (-1) * BC[0] + CA[1] * (-1) * BC[1]) / (
                    math.sqrt(pow(CA[0], 2) + pow(CA[1], 2)) * math.sqrt(pow(BC[0], 2) + pow(BC[1], 2)))
        gocC = round(math.degrees(math.acos(cosC)), 2)
        a.append(gocC)

        return a


    print(goc_canh_tamgiac(AB, BC, CA))


