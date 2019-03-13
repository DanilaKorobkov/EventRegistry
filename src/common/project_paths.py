"""Пути к разным папкам проекта"""

# Python

import os, sys

def __getSlash():

    return os.path.join('1', '2')[1]

projectName = 'EventRegistry'

slash = __getSlash()

executableScriptDir = os.path.abspath(os.curdir)

pathToProject = executableScriptDir[: executableScriptDir.index(projectName) + len(projectName)]

pathToSrc = os.path.join(pathToProject, 'src')

pathToProject = pathToSrc[: pathToSrc.rfind(slash)]

pathToConfig = pathToSrc

pathToRuntimeGeneratedDialects = os.path.join(pathToSrc, 'domain', 'mavlink', 'runtime_dialects')