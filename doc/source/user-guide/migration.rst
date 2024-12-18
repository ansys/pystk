Migrate to PySTK
################

This topic provides details on migrating your code to PySTK.

.. raw:: html

    <link rel="stylesheet" href="https://cdn.datatables.net/2.1.8/css/dataTables.dataTables.css" />
    <script src="https://cdn.datatables.net/2.1.8/js/dataTables.js"></script>

.. jinja:: migration_tables

    {% for module, table in tables %}

    The old ``{{ module }}``
    =========={{ "=" * module|length }}==

    {% set tableID = "DataTables_" + module.replace('.', '_') %}

    .. raw:: html

        <table class="datatable table dataTable no-footer" id="{{ tableID }}" role="grid" aria-describedby="DataTables_{{ module | replace('.', '_') }}_info">
          <thead>
            <tr class="row-odd" role="row">
              <th class="head sorting_asc" tabindex="0" aria-controls="{{ tableID }}" rowspan="1" colspan="1" aria-sort="ascending" aria-label="Old name activate to sort column descending" style="width: 153.312px;">
                <p>Old name</p>
              </th>
              <th class="head sorting" tabindex="0" aria-controls="{{ tableID }}" rowspan="1" colspan="1" aria-label="New name activate to sort column ascending" style="width: 153.312px;">
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

            fetch("../_static/migration-tables/{{ table }}")
                .then(function (response) {
                    return response.json();
                })
                .then(function (data) {

                    // Initialize the table if it doesn't exist
                    if (!migrationTable) {
                        migrationTable = $("#{{ tableID }}").DataTable();
                    }

                    // Clear previous content
                    migrationTable.clear();

                    // Add new rows
                    function addRows(items) {
                        Object.entries(items).forEach(([item, values]) => {
                            console.log(item, values.new_name);
                            migrationTable.row.add([
                                item,
                                values.new_name || ''
                            ]);
                        });
                    }

                    // Populate the table
                    if (data.interfaces) addRows(data.interfaces);
                    if (data.classes) addRows(data.classes);
                    if (data.enums) addRows(data.enums);

                    // Update the display
                    migrationTable.draw();

                });
        </script>

    {% endfor %}
