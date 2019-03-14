from .i_package_wrapper import IPackageWrapper
# Internal
from src.common.decorators import override


class MavlinkPackageWrapper(IPackageWrapper):

    @override
    def toDict(self):

        result = []

        for i in range(len(self.package.fieldnames)):

            data = {}

            data.update({'name': self.package.fieldnames[i]})
            data.update({'value': getattr(self.package, self.package.fieldnames[i])})
            data.update({'type': self.package.fieldtypes[i]})

            result.append(data)

        return result


    def __eq__(self, other):

        return all((getattr(self.package, self.package.fieldnames[i]) == getattr(other, self.package.fieldnames[i])
                    for i in range(len(self.package.fieldnames))))



