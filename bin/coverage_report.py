#!/usr/bin/env python3

import argparse
import os
import shutil

import pandas as pd

# HTML + DataTables JavaScript with column filters and fixed header
html_code = """
<html>
<head>
    <link rel="stylesheet"
          href="https://cdn.datatables.net/1.13.4/css/jquery.dataTables.min.css">
    <link rel="stylesheet"
          href="https://cdn.datatables.net/fixedheader/3.2.0/css/fixedHeader.dataTables.min.css">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js"></script>
    <script src="https://cdn.datatables.net/fixedheader/3.2.0/js/dataTables.fixedHeader.min.js"></script>
    <script>
        $(document).ready(function() {{
            // Add input fields to each column header
            $('#myTable thead tr').clone(true).appendTo('#myTable thead');
            $('#myTable thead tr:eq(1) th').each(function (i) {{
                var title = $(this).text();
                $(this).html('<input type="text" placeholder="Filter ' + title + '" />');

                // Enable per-column filtering
                $('input', this).on('keyup change', function () {{
                    if (table.column(i).search() !== this.value) {{
                        table.column(i).search(this.value).draw();
                    }}
                }});
            }});

            // Initialize DataTable with ordering, fixed header, and per-column search
            var table = $('table').DataTable({{
                orderCellsTop: true,  // Allow column headers to remain fixed
                fixedHeader: true      // Enable the fixed header functionality
            }});
        }});
    </script>
</head>
<body>
    <h2>{title}</h2>
    {html_table}
</body>
</html>
"""

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate HTML report from JSON coverage data.")
    parser.add_argument(
        "--path", type=str, help="Path to the directory to search for coverage JSON files."
    )
    parser.add_argument("--output", type=str, help="Output directory name.", default="html")
    parser.add_argument("--merge", action="store_true", help="Generate Merged coverage.")
    parser.add_argument("--rank", action="store_true", help="Generate Ranked coverage.")

    args = parser.parse_args()

    # Remove old HTML directory
    if os.path.exists(args.output):
        print(f"Removing old HTML directory: {args.output}")
        shutil.rmtree(args.output)

    # Create new HTML directory
    print(f"Creating new HTML directory: {args.output}")
    os.makedirs(args.output, exist_ok=True)

    # Read JSON files into DataFrames
    tables = {}
    print(f"Reading JSON files from: {args.path}")
    json_files = [f for f in os.listdir(args.path) if f.endswith(".json")]
    for f in sorted(json_files):
        print(f"\tReading {f}")
        tables[f] = pd.read_json(os.path.join(args.path, f)).fillna(0)

        # Convert to HTML with table ID
        title = f"Coverage Report : {f}"
        html_table = tables[f].to_html(classes="display", index=False, table_id="myTable")

        # Save to HTML file
        with open(
            os.path.join(args.output, f.replace(".json", ".html")), "w", encoding="utf-8"
        ) as html_file:
            html_file.write(html_code.format(title=title, html_table=html_table))

    # Generate index.html
    index_data = pd.DataFrame({"name": [], "total bins": [], "covered bins": [], "coverage": []})
    for k, v in tables.items():
        # Sub-frame only of hit bins
        hit = v[v["count"] >= v["at_least"]]
        name = k.replace(".json", "")
        fname = f'<a href="{name}.html">{name}</a>'
        total = len(v["bin"])
        covered = len(hit["bin"])
        coverage = (covered / total) * 100 if total > 0 else 0
        t_pd = pd.DataFrame(
            {
                "name": [fname],
                "total bins": [total],
                "covered bins": [covered],
                "coverage": [coverage],
            }
        )
        index_data = pd.concat([index_data, t_pd], ignore_index=True)

        # Create a summary table
        html_table = index_data.to_html(
            classes="display", index=False, table_id="myTable", escape=False
        )

    # Generate merged coverage if requested
    if args.merge:
        print("Generating merged coverage report")
        merged_data = pd.concat(tables.values(), ignore_index=True)
        merged_data = merged_data.groupby(
            ["covergroup", "name", "bin", "at_least"], as_index=False
        ).sum("count")

        with open(os.path.join(args.output, "merged.html"), "w", encoding="utf-8") as html_file:
            html_file.write(
                html_code.format(
                    title="Merged Coverage Report",
                    html_table=merged_data.to_html(
                        classes="display", index=False, table_id="myTable", escape=False
                    ),
                )
            )

        # Add merged coverage to index.html
        t_pd = pd.DataFrame(
            {
                "name": ['<a href="merged.html">Merged Coverage</a>'],
                "total bins": [len(merged_data["bin"])],
                "covered bins": [
                    len(merged_data[merged_data["count"] >= merged_data["at_least"]]["bin"])
                ],
                "coverage": [
                    (
                        len(merged_data[merged_data["count"] >= merged_data["at_least"]]["bin"])
                        / len(merged_data["bin"])
                    )
                    * 100
                ],
            }
        )

        html_table += f"""

<h2>Merged Coverage Report</h2>
{t_pd.to_html(classes="display", index=False, table_id="mergedTable", escape=False)}

        """

    # Generate ranked coverage if requested
    if args.rank:
        print("Generating ranked coverage report")
        filtered = {}
        ranked = pd.DataFrame({"covergroup": [], "name": [], "bin": [], "contributor": []})

        for k, v in tables.items():
            filtered_rows = v[v["count"] >= v["at_least"]]

            if not filtered_rows.empty:
                t_pd = filtered_rows[["covergroup", "name", "bin"]].copy()
                t_pd["contributor"] = k
                ranked = pd.concat([ranked, t_pd], ignore_index=True)

        ranked = ranked.groupby(["covergroup", "name", "bin"], as_index=False)["contributor"].agg(
            list
        )

        with open(
            os.path.join(args.output, "contributors.html"), "w", encoding="utf-8"
        ) as html_file:
            html_file.write(
                html_code.format(
                    title="Merged Coverage Report (By Contributor)",
                    html_table=ranked.to_html(
                        classes="display", index=False, table_id="myTable", escape=False
                    ),
                )
            )

        # Walk over the json files again to get the count
        scores = []
        for k in tables.keys():
            scores.append([k, 0, 0, 0, 0])

            for row in ranked.iterrows():
                if k in row[1]["contributor"]:
                    scores[-1][4] += 1
                    if len(row[1]["contributor"]) == 1:
                        scores[-1][1] += 1000
                        scores[-1][2] += 1
                    elif len(row[1]["contributor"]) < 10:
                        scores[-1][1] += 10
                        scores[-1][3] += 1
                    else:
                        scores[-1][1] += 1

        scores.sort(key=lambda x: x[1], reverse=True)
        t_pd = pd.DataFrame(
            scores, columns=["name", "score", "unique rows", "rare rows", "total rows"]
        )

        with open(os.path.join(args.output, "ranked.html"), "w", encoding="utf-8") as html_file:
            html_file.write(
                html_code.format(
                    title="Ranked Coverage Report",
                    html_table=t_pd.to_html(
                        classes="display", index=False, table_id="myTable", escape=False
                    ),
                )
            )

        html_table += """

<h2>Ranked Coverage Report</h2>
<ul>
    <li><a href="ranked.html">Ranked Coverage</a></li>
    <li><a href="contributors.html">Merged Coverage (By Contributor)</a></li>
</ul>

        """

    # Save index.html
    with open(os.path.join(args.output, "index.html"), "w", encoding="utf-8") as html_file:
        html_file.write(html_code.format(title="Coverage Report", html_table=html_table))
