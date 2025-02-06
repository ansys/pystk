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


def record(mappings_directory, root_directory, recordings_directory, script, entry_point):
    """Invoke the specified entry point for the specified script, and record its execution."""
    mappings = Mappings.load_from(mappings_directory)
    if root_directory is None:
        root_directory = str(Path(script).parent)
    recorder = Recorder(
        script,
        entry_point,
        root_directory,
        is_member_name_of_interest_func=mappings.is_member_name_of_interest,
    )
    recording = recorder.record()

    recordings_directory_path = Path(recordings_directory)
    date_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")[:-3]
    recordings_directory_path.mkdir(parents=True, exist_ok=True)
    recordings_file = recordings_directory_path / f"recording_{date_time}.xml"
    recording.save_to_xml(str(recordings_file.resolve()), f"{Path.cwd()}> {' '.join(sys.argv)}")


def _invoke_record(args):
    """Invoke the record function above with the parameters extracted from the arguments."""
    record(
        args.mappings_directory,
        args.root_directory,
        args.recordings_directory,
        args.script,
        args.entry_point,
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


def _invoke_apply(args):
    """Invoke the apply function above with the parameters extracted from the arguments."""
    apply(args.mappings_directory, args.recordings_directory)


def _main(argv=None):
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
    sys.exit(_main())
