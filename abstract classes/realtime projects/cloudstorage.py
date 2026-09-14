from abc import ABC, abstractmethod

class CloudStorage(ABC):

    @abstractmethod
    def storage(self):
        pass


class GoogleDrive(CloudStorage):

    def storage(self):
        print("Google Drive storage")


class AWSStorage(CloudStorage):

    def storage(self):
        print("AWS storage")


class AzureStorage(CloudStorage):

    def storage(self):
        print("Azure storage")


GoogleDrive().storage()
AWSStorage().storage()
AzureStorage().storage()