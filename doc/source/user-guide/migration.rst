Migrate to PySTK
################

This topic provides details on migrating your code to PySTK.

.. raw:: html

    <link rel="stylesheet" href="https://cdn.datatables.net/2.1.8/css/dataTables.dataTables.css" />
    <script src="https://cdn.datatables.net/2.1.8/js/dataTables.js"></script>

    <table class="datatable table dataTable no-footer" id="migration-table" role="grid" aria-describedby="DataTables_{{ module | replace('.', '_') }}_info">
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

                // Initialize the table if it doesn't exist
                if (!$.fn.dataTable.isDataTable('#migration-table')) {
                    migrationTable = $("#migration-table").DataTable({
                       ordering: false,
                       language: {
                           emptyTable: "Loading..."
                       }
                    });
                } 
                else {
                    // If DataTable is already initialized, just assign the instance
                    migrationTable = $('#migration-table').DataTable();
                }

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
