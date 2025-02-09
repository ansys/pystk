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
        ArgumentParser._add_record_sub_parser(subparsers, record_handler)
        ArgumentParser._add_apply_sub_parser(subparsers, apply_handler)

        return parser

    @staticmethod
    def _add_record_sub_parser(subparsers, record_handler):
        record_parser = subparsers.add_parser(
            "record",
            help="record the execution of the specified program to identify the API calls to migrate",
        )
        record_parser.add_argument(
            "--entry-point",
            action="store",
            default="main",
            metavar="<entry point>",
            dest="entry_point",
            help="entry point to invoke (default: main)",
        )
        record_parser.add_argument(
            "--root-directory",
            metavar="<directory>",
            action="store",
            dest="root_directory",
            help="only migrate files under this directory (default: program directory)",
        )

        ArgumentParser._add_mappings_recordings_directory_arguments(record_parser)

        record_parser.add_argument(
            "-m",
            action="store_true",
            default=False,
            dest="run_as_module",
            help="invoke the specified program as a module",
        )
        record_parser.add_argument(
            "program",
            type=str,
            help="script file or module (if -m flag) to record",
        )
        record_parser.add_argument(
            "program_args",
            metavar="...",
            help="arguments passed to program in sys.argv[1:]",
            nargs=argparse.REMAINDER,
        )
        record_parser.set_defaults(handler=lambda args: record_handler(record_parser, args))

    @staticmethod
    def _add_apply_sub_parser(subparsers, apply_handler):
        apply_parser = subparsers.add_parser("apply", help="migrate the calls previously recorded to the new API")
        ArgumentParser._add_mappings_recordings_directory_arguments(apply_parser)
        apply_parser.set_defaults(handler=lambda args: apply_handler(apply_parser, args))

    @staticmethod
    def _add_mappings_recordings_directory_arguments(parser):
        default_mappings_directory = str(
            (Path(__file__).parent / "api-mappings").resolve()
        )  # points to the mappings provided with the library
        default_recordings_directory = str((Path.cwd() / "recordings").resolve())

        parser.add_argument(
            "--mappings-directory",
            action="store",
            dest="mappings_directory",
            metavar="<directory>",
            default=default_mappings_directory,
            help=f"directory containing the XML API mappings (default: {default_mappings_directory})",
        )
        parser.add_argument(
            "--recordings-directory",
            action="store",
            dest="recordings_directory",
            metavar="<directory>",
            default=default_recordings_directory,
            help=f"directory receiving the XML recordings (default: {default_recordings_directory})",
        )
