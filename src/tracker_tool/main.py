""" main entry point to the tracker tool """

import logging

import dotenv


def main():
    """main function"""
    config = dotenv.dotenv_values(".env")

    # getting client info
    client_no = str(
        input(f'Enter a client No : [{config["CLIENT_NO"]}]') or {config["CLIENT_NO"]}
    )
    client_domain = str(
        input(f'Enter a client domain: [{config["CLIENT_DOMAIN"]}]')
        or {config["CLIENT_DOMAIN"]}
    )

    # setting up logger
    log = logging.getLogger(__name__)
    stream_logger = logging.StreamHandler()
    formatter = logging.Formatter("[%(levelname)s] %(name)s: %(message)s")
    stream_logger.setFormatter(formatter)
    log.addHandler(stream_logger)
    log.setLevel(logging.DEBUG)

    log.debug("TrackerTool initialized with %s and %s", client_no, client_domain)


if __name__ == "__main__":
    raise SystemExit(main())
