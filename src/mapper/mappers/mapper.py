

class Mapper:

    def __init__(self, dbConnection):

        self.dbConnection = dbConnection


    def abstractFind(self, sqlQuery, *args):

        cursor = self.dbConnection.cursor()

        dataSets = cursor.execute(sqlQuery, *args)

        return dataSets


    def handleDataSets(self, dataSets):

        results = [self.handleDataSet(dataSet) for dataSet in dataSets]
        return results


    def handleDataSet(self, dataSet):
        raise NotImplementedError
