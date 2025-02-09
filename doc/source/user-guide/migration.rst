Migrate to PySTK
################

You might have existing Python scripts based on the `STK API for Python <https://help.agi.com/stkdevkit/Content/python/pythonIntro.htm>`_ currently shipped with the STK install. This page describes how you can migrate your code to PySTK to benefit from the improvements provided by the new API. 

In general, the overall logic of the code is unchanged, but namespaces, classes, interfaces, enumerations, methods, and arguments have been renamed. Migrating your code consists in replacing the old names with the new names. The :ref:`migration table <Migration table>` provided on this page contains the mappings between the old names and the new names. Updating your code manually by looking up the mappings one at a time can be time consuming. The :ref:`API Migration Assistant <API migration assistant>` included with the PySTK package facilitates that process.

API migration assistant
=======================

The API migration assistant automates migrating your code to the new API. It relies on a mix of dynamic and static analysis to locate the symbols that need to be updated in your code, and then perform the required edits. The dynamic analysis phase consists in running your application while recording the calls performed to the STK API. The static analysis phase uses the information recorded in the first phase to identify the methods and types that need to be renamed. It also renames imports, enumerations, and type hints by inspecting the source code.

.. warning::
    Before making changes to your existing code, make sure that all changes have been committed to your source control system.

The following steps are recommended:

1. Upgrade your code to STK version 12.10.0.
2. Test your code using STK version 12.10.0 to make sure it works properly.
3. Run the API migration assistant in recording mode. Repeat to cover all the code paths.
4. Run the API migration assistant to apply the changes.
5. Review the changes.
6. If you are satisfied with the changes, rename the migrated files to overwrite the original files.
7. Test the migrated application.

This workflow is depicted in the following diagram.

.. mermaid::

    flowchart LR
        A[Start] --> B(Record trace)
        B --> C[/Are all the code paths covered?/]
        C -->|No| B
        C -->|Yes| D[Apply the changes]
        D --> E[Review *.py-migrated files]
        E --> F[Overwrite the original files]
        F --> G[Done!]

To illustrate this process, the examples below use a script in a filename named `snippet.py`:

.. vale off

.. code-block:: python
    :linenos:

    import sys
    from agi.stk12.stkengine import STKEngine
    from agi.stk12.stkobjects import *
    from agi.stk12.stkutil import *


    def main():
        stk = STKEngine.StartApplication(noGraphics=True)

        stkRoot = stk.NewObjectRoot()
        stkRoot.NewScenario("test")
        scenario = stkRoot.CurrentScenario

        facility = scenario.Children.New(AgESTKObjectType.eFacility, "MyFacility")
        facility.Position.AssignGeodetic(28.62, -80.62, 0.03)

        stk.ShutDown()

    if __name__ == "__main__":
        sys.exit(main())

.. vale on

Recording traces
~~~~~~~~~~~~~~~~

The first phase of the process is to record one or multiple traces of the execution of your Python application using the old API. Start the recording by invoking the API migration assistant with the following options:

.. code-block:: console

   $ pystk-migration-assistant record --recordings-directory=... snippet.py
   INFO: Recording ... snippet.py

The recordings are saved in the specified directory. Therefore, make sure to specify an empty directory if starting from scratch on migrating a new application.

By default, the API migration assistant executes the provided script and invokes `main` as an entry point. If you want to trigger the execution of a different entry point, use the `--entry-point` command line option.

If the `--recordings-directory=` option is not specified, a sub-directory named `recordings` is created in the current directory.

This creates an XML file in the recordings directory. That file contains the calls made by your script to the STK API. Here is how it looks in the case of the snippet used for this example:

.. code-block:: XML

    <!-- ... -->
    <recording root_directory="D:\Dev\api_migration_interceptor">
    <call filename="snippet.py" lineno="8" end_lineno="8" col_offset="10" end_col_offset="53" type_name="STKEngine" member_name="StartApplication"/>
    <call filename="snippet.py" lineno="10" end_lineno="10" col_offset="14" end_col_offset="33" type_name="STKEngineApplication" member_name="NewObjectRoot"/>
    <call filename="snippet.py" lineno="11" end_lineno="11" col_offset="4" end_col_offset="31" type_name="IAgStkObjectRoot" member_name="NewScenario"/>
    <call filename="snippet.py" lineno="12" end_lineno="12" col_offset="15" end_col_offset="38" type_name="IAgStkObjectRoot" member_name="CurrentScenario"/>
    <call filename="snippet.py" lineno="14" end_lineno="14" col_offset="15" end_col_offset="32" type_name="IAgStkObject" member_name="Children"/>
    <call filename="snippet.py" lineno="14" end_lineno="14" col_offset="15" end_col_offset="78" type_name="IAgStkObjectCollection" member_name="New"/>
    <call filename="snippet.py" lineno="15" end_lineno="15" col_offset="4" end_col_offset="21" type_name="IAgFacility" member_name="Position"/>
    <call filename="snippet.py" lineno="15" end_lineno="15" col_offset="4" end_col_offset="57" type_name="IAgPosition" member_name="AssignGeodetic"/>
    <call filename="snippet.py" lineno="17" end_lineno="17" col_offset="4" end_col_offset="18" type_name="STKEngineApplication" member_name="ShutDown"/>
    </recording>

There are also other options available to tweak recording. Use the `--help` command line argument to display them.

.. code-block:: console

    $ pystk-migration-assistant record --help
    usage: pystk-migration-assistant record [-h] [--entry-point <entry point>]
                                            [--root-directory <directory>]
                                            [--mappings-directory <directory>]
                                            [--recordings-directory <directory>] [-m]
                                            program ...

    positional arguments:
    program               script file or module (if -m flag) to record
    ...                   arguments passed to program in sys.argv[1:]

    options:
    -h, --help            show this help message and exit
    --entry-point <entry point>
                            entry point to invoke (default: main)
    --root-directory <directory>
                            only migrate files under this directory (default: program directory)
    --mappings-directory <directory>
                            directory containing the XML API mappings (default: D:\Dev\github_root\pyst
                            k\src\ansys\stk\core\tools\api_migration_assistant\api-mappings)
    --recordings-directory <directory>
                            directory receiving the XML recordings (default:
                            D:\Dev\github_root\pystk\recordings)
    -m                    invoke the specified program as a module

Note that the `-m` option is required if your program is a library module. Here is an example using `pytest`:

.. code-block:: console

    $ pystk-migration-assistant record --root-directory=. -m pytest .
    INFO: Recording -m pytest .
    ================================== test session starts =================================
    platform win32 -- Python 3.12.7, pytest-8.3.4, pluggy-1.5.0
    rootdir: d:\Dev\api_migration_interceptor\test_stk
    plugins: cov-6.0.0, xdist-3.6.1
    collected 1 item

    test.py .                                                                         [100%]

    ================================== 1 passed in 17.95s ==================================


Applying the changes
~~~~~~~~~~~~~~~~~~~~

Once you have accumulated one or more traces to cover all the paths in your Python application, you can apply the changes using the following command line:

.. code-block:: console

    $ pystk-migration-assistant record apply --recordings-directory=... snippet.py
    INFO: Applying changes from ...
    INFO: Writing ... snippet.py-migrated

This generates one `.py-migrated` file for each Python file in your application. Compare those files with the original files and tweak if needed. With the example, the diff looks like this:

.. image:: img/migration_diff.png

There are additional options available to control how the changes are applied. Use the `--help` command line argument to display them.

.. code-block:: console

    $ pystk-migration-assistant apply --help
    usage: pystk-migration-assistant apply [-h] [--mappings-directory <directory>]
                                        [--recordings-directory <directory>]

    options:
    -h, --help            show this help message and exit
    --mappings-directory <directory>
                            directory containing the XML API mappings (default: ...)
    --recordings-directory <directory>
                            directory receiving the XML recordings (default:...)

Review, tweak, and accept
~~~~~~~~~~~~~~~~~~~~~~~~~

Review the suggested code changes. Once you are satisfied with the results, rename the `.py-migrated` files and overwrite your original files. Then retest the migrated application to ensure that the migration completed successfully.
            

Migration table
===============

The table below lists the interface, classes, enumerations, and method names that have been updated in PySTK. You can look up a specific name using the Search box to only display the rows that contain that symbol. Note that the root of the namespace has also changed from :py:attr:`agi.stk[version]` to :py:attr:`ansys.stk.core`.

.. raw:: html

    <table class="datatable table dataTable no-footer display" id="js-migration-table" role="grid" aria-describedby="DataTables_{{ module | replace('.', '_') }}_info">
      <thead>
        <tr class="row-odd" role="row">
          <th class="head sorting_asc" tabindex="0" aria-controls="migration-table" rowspan="1" colspan="1" aria-sort="ascending" aria-label="Old name activate to sort column descending" style="width: 153.312px;">
            <p>Old name</p>
          </th>
          <th class="head sorting" tabindex="0" aria-controls="migration-table" rowspan="1" colspan="1" aria-label="New name activate to sort column ascending" style="width: 153.312px;">
            <p>New name</p>
          </th>
        </tr>
      </thead>
      <tbody id="{{ module | replace('.', '_') }}_body">
        <!-- Rows will be dynamically added here. -->
      </tbody>
    </table>

    <script>
        let migrationTable;

        fetch("../_static/migration-tables/main.json")
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {

                // If DataTable is already initialized, destroy it first to reset the table
                if ($.fn.dataTable.isDataTable('#js-migration-table')) {
                    $('#js-migration-table').DataTable().clear().destroy();
                }

                // Initialize the table with desired options
                migrationTable = $("#js-migration-table").DataTable({
                    ordering: true,
                    language: {
                        emptyTable: "Loading..."
                    },
                    scrollX: true,
                });

                // Clear previous content
                migrationTable.clear();

                function addRows(items) {
                    Object.entries(items).forEach(([oldTypeName, content]) => {

                        // Ignore private types
                        if (oldTypeName.startsWith("_")) {
                            return;
                        }

                        // Add the main row for the type
                        let rowData = [
                            `<b>${oldTypeName}</b>`,
                            `<b>${content.new_name || ''}</b>` // Corrected to handle null or undefined
                        ];
                
                        // Check if the content has members and handle it
                        if (content.members) {
                            let memberOldNames = '';
                            let memberNewNames = '';
                
                            if (Array.isArray(content.members)) {
                                // If members is an array, iterate with map
                                content.members.forEach(member => {
                                    memberOldNames += `<br>${member.oldName}<br>`;
                                    memberNewNames += `<br>${member.newName || ''}<br>`;
                                });
                            } else if (typeof content.members === 'object') {
                                // If members is an object, use Object.entries to iterate over key-value pairs
                                Object.entries(content.members).forEach(([oldName, newName]) => {
                                    memberOldNames += `<br>${oldName}<br>`;
                                    memberNewNames += `<br>${newName || ''}<br>`;
                                });
                            }
                
                            // Add the member data next to the main type row
                            rowData[0] += `<div style="padding-left: 2em;">${memberOldNames}</div>`;
                            rowData[1] += `<div style="padding-left: 2em;">${memberNewNames}</div>`;
                        }
                
                        // Add the row to the table
                        migrationTable.row.add(rowData);
                    });
                }
                addRows(data);

                // Update the display
                migrationTable.draw();

            });
    </script>
