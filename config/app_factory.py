from app_dev_env import AppDevEnvironment
from app_prod_env import AppProdEnvironment

FOR_ENV_DEV = "dev"
FOR_ENV_PROD = "prod"


class AppFactory:

    @staticmethod
    def produce(env):
        if env == FOR_ENV_DEV:
            return AppDevEnvironment()
        elif env == FOR_ENV_PROD:
            return AppProdEnvironment()
        else:
            return AppProdEnvironment()


MyAPP = AppFactory.produce(FOR_ENV_DEV)
