import mailbox_counter

def test_mbox_long_output(capfd, monkeypatch):
    input = ['mbox-long.txt']
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    mailbox_counter.mailbox_counter()
    out, err = capfd.readouterr()

    assert "There were 1797 lines in the file with From as the first word" in out
    assert "dlhaines@umich.edu" in out


def test_mbox_short_output(capfd, monkeypatch):
    input = ['mbox-short.txt']
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    mailbox_counter.mailbox_counter()
    out, err = capfd.readouterr()

    assert "There were 27 lines in the file with From as the first word" in out
    assert "cwen@iupui.edu" in out
