import json
import git
import os
import uuid
from git.repo import Repo

urlRepository = "https://github.com/albuquerquealdry/terraform-dabura"
class GitService():
    def gitClone():
        git.Git("~/dabura").clone(urlRepository)
    def gitAdd():
        os.system("cd ~/dabura/terraform-dabura && git add . && git push")

class AwsModulationService():
    def createS3StateTerraform():
        uuids = uuid.uuid4()
        GitService.gitClone()
        os.system("mkdir ~/dabura/terraform-dabura/s3")
        os.system("cp ~/dabura/terraform/modules/s3.tf ~/dabura/terraform-dabura/s3")
        os.system(f"sed -i s/NAME_S3/{uuids}-bucket-state/g ~/dabura/terraform-dabura/s3/s3.tf")
        GitService.gitAdd()
        return {"message": "S3 STATE CREATE"}