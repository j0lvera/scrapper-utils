import logging
import coloredlogs


# Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Colors (optional)
coloredlogs.install(level='INFO', logger=logger)

handler = logging.FileHandler('scraper.log')
handler.setLevel(logging.DEBUG)

# Logger formatting
formatter = logging.Formatter('%(asctime)s - %(name)s - '
                              '%(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add file handler to logger
logger.addHandler(handler)
