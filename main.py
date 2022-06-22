from loguru import logger
from utils.config_manager import get_config

logger.add("data/runtime.log", retention="1 week")


def main():
    logger.info('Starting')
    client_data = get_config('Client')
    strict_sla = client_data['sla_strict']
    print(type(strict_sla))
    logger.info('Finalising')

if __name__ == '__main__':
    main()