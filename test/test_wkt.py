from test.test_data import basic_wkt, basic_noheader_wkt


from reshape import wkt_source


def test_normal_file():
    src = wkt_source(basic_wkt)

    for row in src:
        print(row)


def test_noheader_with_fieldnames():
    src = wkt_source(basic_noheader_wkt, header=False, fieldnames=['id', 'value'])

    for row in src:
        assert len(row['properties']) == 2


def test_noheader_no_fieldnames():
    src = wkt_source(basic_noheader_wkt, header=False)

    for row in src:
        assert len(row['properties']) == 0
