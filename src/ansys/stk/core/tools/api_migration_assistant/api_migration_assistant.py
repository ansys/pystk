"""The API migration assistant applies code transformations to upgrade code to a new version of an API."""

import datetime
import importlib.util
import logging
import sys

from pathlib import Path

from .argument_parser import ArgumentParser
from .code_editor import CodeEditor
from .mappings import Mappings
from .recorder import Recorder
from .recording import Recording


def record(
    mappings_directory,
    root_directory,
    recordings_directory,
    program,
    entry_point,
    run_as_module=False,
    program_args=None,
):
    """Invoke the specified entry point for the specified script or module, and record its execution."""
    mappings = Mappings.load_from(mappings_directory)
    if root_directory is None:
        if run_as_module:
            raise RuntimeError("root_directory argument is mandatory when running as a module")
        else:
            root_directory = str(Path(program).parent)
    recorder = Recorder(
        program,
        entry_point,
        root_directory,
        is_member_name_of_interest_func=mappings.is_member_name_of_interest,
        run_as_module=run_as_module,
        program_args=program_args,
    )
    recording = recorder.record()

    recordings_directory_path = Path(recordings_directory)
    date_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")[:-3]
    recordings_directory_path.mkdir(parents=True, exist_ok=True)
    recordings_file = recordings_directory_path / f"recording_{date_time}.xml"
    recording.save_to_xml(str(recordings_file.resolve()), f"{Path.cwd()}> {' '.join(sys.argv)}")


def _invoke_record(parser, args):
    """Invoke the record function above with the parameters extracted from the arguments."""
    if args.root_directory is None and args.run_as_module:
        parser.error("[--root-directory <directory>] must be specified when executing a module with [-m]")
    record(
        args.mappings_directory,
        args.root_directory,
        args.recordings_directory,
        args.program,
        args.entry_point,
        args.run_as_module,
        args.program_args,
    )


def apply(mappings_directory, recordings_directory):
    """Apply the migrations previously recorded."""
    logging.info(f"Applying changes from {recordings_directory}")
    if not importlib.util.find_spec("libcst"):
        logging.error("The libcst library is required. Please install it and re-run.")
    else:
        mappings = Mappings.load_from(mappings_directory)
        recording = Recording.load_from_xml_recordings_in_directory(recordings_directory)
        editor = CodeEditor(recording, mappings)
        editor.apply_changes()


def _invoke_apply(parser, args):
    """Invoke the apply function above with the parameters extracted from the arguments."""
    apply(args.mappings_directory, args.recordings_directory)


def main(argv=None):
    """Parse the command line argument and invoke the corresponding action."""
    if argv is None:
        argv = sys.argv[1:]

    argument_parser = ArgumentParser.create_parser(record_handler=_invoke_record, apply_handler=_invoke_apply)
    args = argument_parser.parse_args(argv)
    _configure_logging(args)
    if hasattr(args, "handler"):
        args.handler(args)


def _configure_logging(args):
    """Configure logging as specified through the command line."""
    if args.log_level == "DEBUG":
        log_level = logging.DEBUG
    elif args.log_level == "WARNING":
        log_level = logging.WARNING
    elif args.log_level == "ERROR":
        log_level = logging.ERROR
    else:
        log_level = logging.INFO
    logging.basicConfig(level=log_level, format="%(levelname)s: %(message)s")


if __name__ == "__main__":
    sys.exit(main())
