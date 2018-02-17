from drawingManageApp.models import Drawing
from django.db.models import Q
from django.http import HttpResponse

# some helper list
onlyValue = []
normalDict = dict()
rangeList = []


def addToRangeList(num1, num2):
    rangeList.append(int(num1))
    rangeList.append(int(num2))

# handle multiple request
def init_settings():
    onlyValue = []
    normalDict = dict()
    rangeList = []


def DrawingSearch(request):
    keywords = request.GET["request"]
    onlyValue = []
    normalDict = dict()
    rangeList = []
    # split by comma
    keywords = keywords.split(",")
    for i in range(len(keywords)):
        if(":" in keywords[i]):
            keywords[i] = keywords[i].split(":")

    # multiple keywords

    for i in range(len(keywords)):
        #case 1, only have single value
        if(len(keywords[i]) != 2):
            print "the keyword #" + str(i+1) + " only has a value "\
            + keywords[i]
            onlyValue.append(keywords[i])



        #case 2 not range value
        elif(len(keywords[i]) == 2 and "[" not in keywords[i][1]):
            print "the keyword #" + str(i+1) + " uses attribute name "\
            + keywords[i][0] + ", and has a value " + keywords[i][1]
            normalDict[keywords[i][0]] = keywords[i][1]




        #case 3 range value
        elif (len(keywords[i]) == 2 and "[" in keywords[i][1]):
            years = keywords[i][1]
            years = years.strip("[")
            years = years.strip("]")
            years = years.split("-")
            num1 = years[0]
            num2 = years[1]
            print "the keyword #" + str(i + 1) + " uses attribute name "\
            + keywords[i][0] + ", and has a ranged value with lower boundary "\
            + num1 + " and upper boundary " + num2
            # addToRangeList(num1, num2)
            rangeList.append(int(num1))
            rangeList.append(int(num2))

        # case 4 Invalid string
        else:
            print "Invalid string"


    # search end, start filtering
    result = filterQuery(onlyValue, normalDict, rangeList)
    return result




# return all the Query Set
def AllQuerySet():
    drawings = Drawing.objects.all()
    return drawings

# return filtered Query Set
def filterQuery(onlyValue, normalDict, rangeList):

    drawings = Drawing.objects.all()
    # print drawings
    # 1. ConstructedYear Query
    if(len(rangeList) != 0):
        q = drawings.filter(ConstructedYear__gte=rangeList[0])
        q = q.filter(ConstructedYear__lte=rangeList[1])
        # unable to find correct building with given construction year
        if(len(q) == 0):
            return HttpResponse("Failed")
        # 2. have attribute name
        for key in normalDict:
            if(key == "DrawingID"):
                q = q.filter(DrawingID = normalDict[key])
            if (key == "BuildingName"):
                q = q.filter(BuildingName=normalDict[key])
            if (key == "Contractor"):
                q = q.filter(Contractor=normalDict[key])
            if (key == "Floor"):
                q = q.filter(Floor=normalDict[key])
            if (key == "Shop"):
                q = q.filter(Shop=normalDict[key])

        # 3. handle single value
        for i in range(len(onlyValue)):
            q = q.filter(Q(DrawingID=onlyValue[i])|Q(BuildingName=onlyValue[i])|\
                         Q(Contractor=onlyValue[i])|Q(Floor=onlyValue[i])| \
                         Q(Shop=onlyValue[i]))


    # 1. No ConstructedYear Query
    else:
        q = drawings
        # 2. have attribute name
        for key in normalDict:
            if (key == "DrawingID"):
                q = q.filter(DrawingID=normalDict[key])
            if (key == "BuildingName"):
                q = q.filter(BuildingName=normalDict[key])
            if (key == "Contractor"):
                q = q.filter(Contractor=normalDict[key])
            if (key == "Floor"):
                q = q.filter(Floor=normalDict[key])
            if (key == "Shop"):
                q = q.filter(Shop=normalDict[key])
        # 3. handle single value
        for i in range(len(onlyValue)):
            q = q.filter(Q(DrawingID=onlyValue[i]) | Q(BuildingName=onlyValue[i]) | \
                         Q(Contractor=onlyValue[i]) | Q(Floor=onlyValue[i]) | \
                         Q(Shop=onlyValue[i]))


    # print q
    #end of Query Line, prepare JSON String
    result = ""
    for drawing in q:
        result = result + drawing.DrawingID + ","
        result = result + drawing.BuildingName + ","
        result = result + str(drawing.ConstructedYear) + ","
        result = result + drawing.Contractor + ","
        result = result + drawing.Floor + ","
        result = result + drawing.Shop + ";"

    if(len(result) != 0):
        result = result[:-1]


    if(len(result) != 0):
        return HttpResponse(result)
    else:
        return HttpResponse("Failed")
