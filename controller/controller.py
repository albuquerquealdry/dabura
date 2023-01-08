from service import service

class awsModulationController():

    def createS3():
        return service.AwsModulationService.createS3StateTerraform()