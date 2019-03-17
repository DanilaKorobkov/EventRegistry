# Python
import os


projectName = 'EventRegistry'

executableScriptDir = os.path.abspath(os.curdir)

pathToProject = executableScriptDir[: executableScriptDir.index(projectName) + len(projectName)]

pathToSrc = os.path.join(pathToProject, 'src')
pathToRuntimeGeneratedDialects = os.path.join(pathToSrc, 'domain', 'mavlink', 'runtime_dialects')