import unittest


def find_unique_delivery_id(delivery_ids):

    # Find the one unique ID in the list
    resultId = delivery_ids[0]
    lengthofIds = len(delivery_ids)
    for i in range(1,lengthofIds):
        resultId = resultId ^ delivery_ids[i]
    return resultId
