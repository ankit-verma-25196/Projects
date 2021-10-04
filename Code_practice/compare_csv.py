def parse_csv_1():
    fields = []
    rows = []
    with open(CSV_FILE) as csvfile:
        csv_data = csv.reader(csvfile)

        fields = next(csv_data)

        for row in csv_data:
            rows.append(row)

        log.info("Total no. of rows: %d"%(csv_data.line_num))
        log.info("Fields Names are:"+', '.join(field for field in fields))

        log.info("First 5 rows are:")
        for row in rows[:5]:
            for col in row:
                print("%10s"%col),
            print("\n")

