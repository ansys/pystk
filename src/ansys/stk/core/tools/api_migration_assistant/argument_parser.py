"""Command line arguments for the API migration assistant."""

import argparse

from pathlib import Path


class ArgumentParser:
    """Parser for the command line arguments supported by the API migration assistant."""

    @staticmethod
    def create_parser(record_handler, apply_handler):
        """Create the argparse parser for the command line arguments."""
        # Create the top-level parser
        parser = argparse.ArgumentParser(
            description="API Migration Assistant",
            add_help=True,
        )

        parser.add_argument(
            "--log",
            action="store",
            dest="log_level",
            metavar="<level>",
            help="sets the level for logging (one of DEBUG, INFO [default], WARNING, ERROR)",
            default="INFO",
            choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        )

        subparsers = parser.add_subparsers(help="action to execute", required=True)

        # Create the parser for the "record" command
        record_parser = subparsers.add_parser(
            "record",
            help="record the execution of the specified script to identify the API calls to migrate",
        )
        record_parser.add_argument("script", type=str, help="the script to record")
        record_parser.add_argument(
            "--entry-point",
            action="store",
            default="main",
            dest="entry_point",
            help="entry point to invoke (default: main)",
        )
        record_parser.add_argument(
            "--root-directory",
            action="store",
            dest="root_directory",
            help="only migrate files under this directory (default: script directory)",
        )
        default_mappings_directory = str((Path(__file__).parent / "api-mappings").resolve())
        default_recordings_directory = str((Path(__file__).parent / "recordings").resolve())
        record_parser.add_argument(
            "--mappings-directory",
            action="store",
            dest="mappings_directory",
            default=default_mappings_directory,
            help=f"directory containing the XML API mappings (default: {default_mappings_directory})",
        )
        record_parser.add_argument(
            "--recordings-directory",
            action="store",
            dest="recordings_directory",
            default=default_recordings_directory,
            help=f"directory receiving the XML recordings (default: {default_recordings_directory})",
        )
        record_parser.add_argument(
            "script_args",
            help="remaining arguments are forwarded to the script",
            nargs=argparse.REMAINDER,
        )
        record_parser.set_defaults(handler=record_handler)

        # Create the parser for the "apply" command
        apply_parser = subparsers.add_parser("apply", help="migrate the calls previously recorded to the new API")
        apply_parser.add_argument(
            "--mappings-directory",
            action="store",
            dest="mappings_directory",
            default=default_mappings_directory,
            help=f"directory containing the XML API mappings (default: {default_mappings_directory})",
        )
        apply_parser.add_argument(
            "--recordings-directory",
            action="store",
            dest="recordings_directory",
            default=default_recordings_directory,
            help=f"directory receiving the XML recordings (default: {default_recordings_directory})",
        )
        apply_parser.set_defaults(handler=apply_handler)

        return parser
