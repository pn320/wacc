import wacc.console


def test_print_help(capsys):
    wacc.console.main(["-h"])
    out, err = capsys.readouterr()
    assert out == "Usage: wacc [source_file]"
    assert err == ""
