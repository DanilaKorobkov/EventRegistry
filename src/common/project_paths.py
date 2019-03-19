# Python
import os


projectName = 'EventRegistry'

currentFile = __file__

pathToProject = currentFile[: currentFile.index(projectName) + len(projectName)]

pathToSrc = os.path.join(pathToProject, 'src')

pathToConfig = '/var/pilotb/tmi'
pathToRuntimeGeneratedDialects = os.path.join(pathToSrc, 'domain', 'mavlink', 'runtime_dialects')

