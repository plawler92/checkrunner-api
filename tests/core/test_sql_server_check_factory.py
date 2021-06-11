from checkrunner.core.factories import SQLServerCheckFactory

def test_database_not_found():
    dbs = {"TestDB": "adsf"}
    check_params = {
        "database": "nothing"
    }
    s = SQLServerCheckFactory(dbs)
    c = s.create_check(check_params)

    assert c == None