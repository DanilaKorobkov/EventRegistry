# Internal
from src.common.decorators import *
from src.common.project_paths import pathToRuntimeGeneratedDialects
# Python
import os, time, tempfile
import pymavlink.generator.mavgen as mavlink


class MavlinkDialectGenerator:

    def generateUsing(self, metadata: str):

        xmlDialect = self.writeToXmlAndGetPath(metadata)

        pathToDialect = os.path.join(pathToRuntimeGeneratedDialects, self.getDialectFileName())

        try:
            os.mkdir(pathToRuntimeGeneratedDialects)

        except FileExistsError:
            pass

        options = mavlink.Opts(pathToDialect)
        mavlink.mavgen(options, [xmlDialect])

        self.replaceWrongImportInDialectFile(pathToDialect)
        return self.translateTostringSuitableForImport(pathToDialect)


    @private
    def getDialectFileName(self):
        return 'dialect{}.py'.format(format(time.time() * 10e9, '.0f'))


    @private
    def writeToXmlAndGetPath(self, metadata):

        xmlFullPath = os.path.join(tempfile.gettempdir(), 'tmp.xml')

        with open(xmlFullPath, 'w+') as xmlFile:

            if type(metadata) is bytes:
                metadata = metadata.decode('utf-8')

            xmlFile.write(metadata)

        return xmlFullPath


    @private
    def translateTostringSuitableForImport(self, pathToDialect):

        module = pathToDialect[pathToDialect.index('src'): -3]
        module = module.replace('/', '.')
        return module


    @private
    def replaceWrongImportInDialectFile(self, dialectFile):

        with open(dialectFile) as dialectPythonFile:
            newText = dialectPythonFile.read().replace('...generator', 'pymavlink.generator')

        with open(dialectFile, "w") as dialectPythonFile:
            dialectPythonFile.write(newText)
