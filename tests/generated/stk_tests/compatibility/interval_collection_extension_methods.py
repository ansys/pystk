from test_util import *

# <copyright file="IntervalCollectionExtensionMethods.cs" company="Analytical Graphics Inc.">
#     Copyright (c) Analytical Graphics Inc. All rights reserved.
# </copyright>


class IntervalCollectionExtensionMethods(object):
    @staticmethod
    def GetIntervalHelper(intervalCollection: "IntervalCollection", index: int):
        (start, stop) = intervalCollection.get_interval(index)
        return (start, stop)

    @staticmethod
    def GetIntervalHelper2(intervalCollection: "ImmutableIntervalCollection", index: int):
        (start, stop) = intervalCollection.get_interval(index)
        return (start, stop)
