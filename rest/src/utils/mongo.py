from bson.objectid import ObjectId

DATE_FORMAT = "%Y/%m/%d %H:%M:%S"
USERS = "Users"
VISIT_TYPES = "VisitTypes"
VISIT_ARCHIVE = "VisitArchive"

def convertObjectIdsToStr(object_):
    if isinstance(object_, ObjectId):
        return str(object_)
    if isinstance(object_, list):
        for i in range(len(object_)):
            if isinstance(object_[i], ObjectId):
                object_[i] = str(object_[i])
            else:
                convertObjectIdsToStr(object_[i])
    elif isinstance(object_, dict):
       for key in object_.keys():
            if isinstance(object_[key], ObjectId):
                object_[key] = str(object_[key])
            else:
                convertObjectIdsToStr(object_[key])
    return object_
