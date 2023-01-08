from controller import controller

class Router():
    
    def initS3Router():
        return controller.awsModulationController.createS3()